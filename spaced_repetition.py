"""Spaced repetition engine for Astra.
Tracks concept reviews and recommends topics for revision."""

import time
from database import get_db


def init_spaced_tables():
    """Create spaced repetition tables if they don't exist."""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS concept_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            concept_key TEXT NOT NULL,
            last_reviewed TEXT DEFAULT (datetime('now')),
            score REAL DEFAULT 0,
            review_count INTEGER DEFAULT 0,
            next_review TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, concept_key)
        )
    """)
    conn.commit()
    conn.close()


def record_review(user_id, concept_key, score):
    """Record a concept review and calculate next review time.
    Score: 0.0 (failed) to 1.0 (perfect).
    """
    conn = get_db()
    existing = conn.execute(
        "SELECT * FROM concept_reviews WHERE user_id=? AND concept_key=?",
        (user_id, concept_key)
    ).fetchone()
    
    if existing:
        count = existing["review_count"] + 1
        # Simple spaced repetition: interval doubles with good scores
        if score >= 0.8:
            interval_days = min(2 ** count, 30)  # Max 30 days
        elif score >= 0.5:
            interval_days = max(1, 2 ** (count - 1))
        else:
            interval_days = 1  # Review tomorrow
        
        conn.execute("""
            UPDATE concept_reviews 
            SET score=?, review_count=?, last_reviewed=datetime('now'),
                next_review=datetime('now', '+' || ? || ' days')
            WHERE user_id=? AND concept_key=?
        """, (score, count, interval_days, user_id, concept_key))
    else:
        conn.execute("""
            INSERT INTO concept_reviews (user_id, concept_key, score, review_count, next_review)
            VALUES (?, ?, ?, 1, datetime('now', '+1 day'))
        """, (user_id, concept_key, score))
    
    conn.commit()
    conn.close()


def get_due_reviews(user_id, limit=5):
    """Get concepts that are due for review."""
    conn = get_db()
    rows = conn.execute("""
        SELECT concept_key, score, review_count, last_reviewed
        FROM concept_reviews
        WHERE user_id=? AND next_review <= datetime('now')
        ORDER BY score ASC, last_reviewed ASC
        LIMIT ?
    """, (user_id, limit)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_weak_concepts(user_id, threshold=0.6, limit=5):
    """Get concepts where the user scored below threshold."""
    conn = get_db()
    rows = conn.execute("""
        SELECT concept_key, score, review_count, last_reviewed
        FROM concept_reviews
        WHERE user_id=? AND score < ?
        ORDER BY score ASC
        LIMIT ?
    """, (user_id, threshold, limit)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_mastered_concepts(user_id, threshold=0.8):
    """Get concepts the user has mastered."""
    conn = get_db()
    rows = conn.execute("""
        SELECT concept_key, score, review_count
        FROM concept_reviews
        WHERE user_id=? AND score >= ? AND review_count >= 2
        ORDER BY score DESC
    """, (user_id, threshold)).fetchall()
    conn.close()
    return [dict(r) for r in rows]
