import React from 'react';

export interface LogoItem {
  name: string;
  src: string;
  gradient: string;
}

export const LOGOS: LogoItem[] = [
  {
    name: 'Procure',
    src: 'https://svgl.app/library/procure.svg',
    gradient: 'linear-gradient(135deg, #2563eb 0%, #38bdf8 100%)',
  },
  {
    name: 'Shopify',
    src: 'https://svgl.app/library/shopify.svg',
    gradient: 'linear-gradient(135deg, #eab308 0%, #facc15 50%, #ca8a04 100%)',
  },
  {
    name: 'Blender',
    src: 'https://svgl.app/library/blender.svg',
    gradient: 'linear-gradient(135deg, #1d4ed8 0%, #3b82f6 50%, #f97316 100%)',
  },
  {
    name: 'Figma',
    src: 'https://svgl.app/library/figma.svg',
    gradient: 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #f43f5e 100%)',
  },
  {
    name: 'Spotify',
    src: 'https://svgl.app/library/spotify.svg',
    gradient: 'linear-gradient(135deg, #f43f5e 0%, #fb7185 50%, #e11d48 100%)',
  },
  {
    name: 'Lottielab',
    src: 'https://svgl.app/library/lottielab.svg',
    gradient: 'linear-gradient(135deg, #eab308 0%, #84cc16 50%, #22c55e 100%)',
  },
  {
    name: 'Google Cloud',
    src: 'https://svgl.app/library/google-cloud.svg',
    gradient: 'linear-gradient(135deg, #38bdf8 0%, #60a5fa 50%, #3b82f6 100%)',
  },
  {
    name: 'Bing',
    src: 'https://svgl.app/library/bing.svg',
    gradient: 'linear-gradient(135deg, #06b6d4 0%, #0d9488 50%, #14b8a6 100%)',
  },
];

export const MarqueeScroller: React.FC = () => {
  // Render the list twice inline to ensure a seamless loop
  const duplicatedLogos = [...LOGOS, ...LOGOS];

  return (
    <div className="w-full mt-10 overflow-hidden mask-marquee py-4">
      <div className="animate-marquee flex gap-4 items-center">
        {duplicatedLogos.map((logo, index) => (
          <div
            key={`${logo.name}-${index}`}
            className="group relative h-24 w-40 shrink-0 flex items-center justify-center rounded-full bg-white border border-slate-200/60 shadow-sm hover:border-slate-300 transition-all overflow-hidden cursor-pointer"
          >
            {/* Gradient background on hover */}
            <div
              className="absolute inset-0 scale-150 opacity-0 group-hover:scale-100 group-hover:opacity-100 transition-all duration-500 rounded-full pointer-events-none"
              style={{ background: logo.gradient }}
            />

            {/* Logo Image */}
            <img
              src={logo.src}
              alt={logo.name}
              loading="lazy"
              className="relative z-10 w-9 h-9 object-contain group-hover:brightness-0 group-hover:invert transition-all duration-300 select-none"
              onError={(e) => {
                // Fallback text if external image fails to load
                const target = e.currentTarget;
                target.style.display = 'none';
                const parent = target.parentElement;
                if (parent && !parent.querySelector('.fallback-label')) {
                  const span = document.createElement('span');
                  span.className =
                    'fallback-label relative z-10 font-medium text-xs text-slate-700 group-hover:text-white transition-colors';
                  span.innerText = logo.name;
                  parent.appendChild(span);
                }
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default MarqueeScroller;
