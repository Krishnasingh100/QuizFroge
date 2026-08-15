import React, { useId } from "react";

const LanguageIcon = ({
  slug = "",
  name = "",
  className = "w-16 h-16",
}) => {
  // Get a clean language key.
  const key = slug.toLowerCase().trim();

  // Unique ID prevents SVG gradient conflicts.
  const uniqueId = useId().replace(/:/g, "");

  // Common SVG properties.
  const commonProps = {
    viewBox: "0 0 64 64",
    role: "img",
    "aria-label": name || slug || "Programming language",
    className,
    xmlns: "http://www.w3.org/2000/svg",
  };

  const icons = {
    // C
    c: (
      <svg {...commonProps}>
        <circle cx="32" cy="32" r="28" fill="#A8B9CC" />

        <text
          x="32"
          y="43"
          textAnchor="middle"
          fontFamily="'Trebuchet MS', Arial, sans-serif"
          fontWeight="700"
          fontSize="30"
          fill="#00599C"
        >
          C
        </text>
      </svg>
    ),

    // C++
    cpp: (
      <svg {...commonProps}>
        <defs>
          <linearGradient
            id={`cpp-${uniqueId}`}
            x1="0"
            y1="0"
            x2="1"
            y2="1"
          >
            <stop offset="0" stopColor="#004482" />
            <stop offset="1" stopColor="#659AD2" />
          </linearGradient>
        </defs>

        <path
          d="M32 4 56 18v28L32 60 8 46V18L32 4Z"
          fill={`url(#cpp-${uniqueId})`}
        />

        <text
          x="26"
          y="41"
          textAnchor="middle"
          fontFamily="Arial, sans-serif"
          fontWeight="700"
          fontSize="19"
          fill="#fff"
        >
          C
        </text>

        <g
          stroke="#fff"
          strokeWidth="2.5"
          strokeLinecap="round"
        >
          <line x1="42" y1="26" x2="42" y2="34" />
          <line x1="38" y1="30" x2="46" y2="30" />

          <line x1="52" y1="26" x2="52" y2="34" />
          <line x1="48" y1="30" x2="56" y2="30" />
        </g>
      </svg>
    ),

    // Python
    python: (
      <svg {...commonProps}>
        <path
          d="M31.9 6c-3.1 0-6 .3-8.4.8-4.5.9-5.3 2.7-5.3 6.1v4.5h10.6v1.4H14.4c-3.4 0-6.4 2-7.3 5.9-1.1 4.5-1.1 7.3 0 12 .8 3.5 2.8 5.9 6.2 5.9h4v-5.3c0-3.9 3.4-7.3 7.4-7.3h10.6c3.3 0 5.9-2.7 5.9-6V13c0-3.2-2.7-5.6-5.9-6.1C33.6 6.2 33.7 6 31.9 6ZM26 10.5c1.1 0 2 .9 2 2.1s-.9 2.1-2 2.1-2-1-2-2.1.9-2.1 2-2.1Z"
          fill="#3776AB"
        />

        <path
          d="M32.1 58c3.1 0 6-.3 8.4-.8 4.5-.9 5.3-2.7 5.3-6.1v-4.5H35.2v-1.4h14.4c3.4 0 6.4-2 7.3-5.9 1.1-4.5 1.1-7.3 0-12-.8-3.5-2.8-5.9-6.2-5.9h-4v5.3c0 3.9-3.4 7.3-7.4 7.3H29c-3.3 0-5.9 2.7-5.9 6V51c0 3.2 2.7 5.6 5.9 6.1 1.9.6 1.7.9 3.1.9ZM38 53.5c-1.1 0-2-.9-2-2.1s.9-2.1 2-2.1 2 1 2 2.1-.9 2.1-2 2.1Z"
          fill="#FFD43B"
        />
      </svg>
    ),

    // JavaScript
    javascript: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          fill="#F7DF1E"
        />

        <text
          x="34"
          y="46"
          textAnchor="middle"
          fontFamily="Arial, sans-serif"
          fontWeight="700"
          fontSize="26"
          fill="#000"
        >
          JS
        </text>
      </svg>
    ),

    // TypeScript
    typescript: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          fill="#3178C6"
        />

        <text
          x="34"
          y="46"
          textAnchor="middle"
          fontFamily="Arial, sans-serif"
          fontWeight="700"
          fontSize="26"
          fill="#fff"
        >
          TS
        </text>
      </svg>
    ),

    // Java
    java: (
      <svg {...commonProps}>
        <rect
          x="4"
          y="4"
          width="56"
          height="56"
          rx="12"
          fill="#fff"
          stroke="#e5e7eb"
          strokeWidth="1"
        />

        <path
          d="M24 12c-2 2 2 3 0 5s-4 4 0 6"
          fill="none"
          stroke="#EA2D2E"
          strokeWidth="2"
          strokeLinecap="round"
        />

        <path
          d="M31 10c-2 2 2 3 0 5s-4 4 0 6"
          fill="none"
          stroke="#EA2D2E"
          strokeWidth="2"
          strokeLinecap="round"
        />

        <path
          d="M18 30h26c1 5-1 12-13 12S17 35 18 30Z"
          fill="#5382A1"
        />

        <path
          d="M44 32c4-1 7 1 7 4s-3 5-8 4"
          fill="none"
          stroke="#5382A1"
          strokeWidth="2.5"
        />

        <path
          d="M22 46c-3 2-3 4 2 5 7 2 15 2 20-1 2-1 2-3-1-4"
          fill="none"
          stroke="#EA2D2E"
          strokeWidth="2.5"
          strokeLinecap="round"
        />

        <path
          d="M20 51c-3 2 0 4 3 5 8 2 17 1 21-2"
          fill="none"
          stroke="#EA2D2E"
          strokeWidth="2.5"
          strokeLinecap="round"
        />
      </svg>
    ),

    // HTML
    html: (
      <svg {...commonProps}>
        <path
          d="M9 6h46l-4.2 47.5L32 59 12.2 53.5 9 6Z"
          fill="#E44D26"
        />

        <path
          d="M32 10v45.3l16.1-4.5L51.6 10H32Z"
          fill="#F16529"
        />

        <path
          d="M32 27.6H19.9l.5 5.7H32v5.6H15.9l1.4 15.6L32 58.4v-5.9l-.1.1-9-2.5-.6-6.7h5.9l.3 3.3 3.5 1v-6H16.6l-1.6-17.7H32v5.6Z"
          fill="#EBEBEB"
        />

        <path
          d="M32 27.6h11.6l-.5 5.7H32v5.6h10.6l-1 11.6-9.6 2.7v6l14.8-4.1L48.4 32l.5-4.4.6-6.9H32v5.6Z"
          fill="#fff"
        />
      </svg>
    ),

    // CSS
    css: (
      <svg {...commonProps}>
        <path
          d="M9 6h46l-4.2 47.5L32 59 12.2 53.5 9 6Z"
          fill="#1B73BA"
        />

        <path
          d="M32 10v45.3l16.1-4.5L51.6 10H32Z"
          fill="#1C88C7"
        />

        <path
          d="M32 27.6H19.7l.5 5.7H32v5.6H15.8l1.5 16.3 14.6 4.1.1-.1v-5.9l-.1.1-8-2.2-.5-5.8h5.9l.3 2.9 2.4.7v-6H16.7l-1.6-17.7H32v5.6Z"
          fill="#fff"
        />

        <path
          d="M32 27.6h11.9l-.5 5.7H32v5.6h10.9l-1 11.3-9.9 2.8v6l14.8-4.1 1.6-18.1.5-5.2.6-6.2H32v5.6Z"
          fill="#EBEBEB"
        />
      </svg>
    ),

    // Node.js
    nodejs: (
      <svg {...commonProps}>
        <path
          d="M32 4 8 17.5v29L32 60l24-13.5v-29L32 4Z"
          fill="#333"
        />

        <path
          d="M32 12 15 21.7v20.6L32 52l4-2.3c-2.7.3-3.7-1.2-3.7-3v-14c0-.4-.2-.6-.6-.6h-1.6c-.4 0-.6.2-.6.6v14c0 3 1.6 4.7 4.4 4.7 1 0 1.7-.1 2.3-.4l.3-.2 3.5-2V21.7L32 12Z"
          fill="#83CD29"
        />

        <path
          d="M32 12v9.7l4.5 2.6v6.5c0 1.6-.5 2.6-2.4 2.6-1.7 0-2.5-1-2.5-2.5v-1.3c0-.3-.2-.5-.5-.5h-1.7c-.3 0-.5.2-.5.5v1.4c0 3.3 1.8 5.2 5.3 5.2 3.6 0 5.4-1.9 5.4-5.4V24.3L32 21.7v-9.6Z"
          fill="#83CD29"
        />
      </svg>
    ),

    // React
    react: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="10"
          fill="#20232A"
        />

        <g
          stroke="#61DAFB"
          strokeWidth="2.3"
          fill="none"
        >
          <ellipse cx="32" cy="32" rx="20" ry="8" />

          <ellipse
            cx="32"
            cy="32"
            rx="20"
            ry="8"
            transform="rotate(60 32 32)"
          />

          <ellipse
            cx="32"
            cy="32"
            rx="20"
            ry="8"
            transform="rotate(120 32 32)"
          />
        </g>

        <circle
          cx="32"
          cy="32"
          r="4.5"
          fill="#61DAFB"
        />
      </svg>
    ),

    // Go
    go: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="10"
          fill="#fff"
          stroke="#e5e7eb"
          strokeWidth="1"
        />

        <text
          x="32"
          y="41"
          textAnchor="middle"
          fontFamily="'Arial Black', Arial, sans-serif"
          fontWeight="900"
          fontSize="22"
          fill="#00ADD8"
          letterSpacing="-1"
        >
          Go
        </text>
      </svg>
    ),

    // Rust
    rust: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="10"
          fill="#fff"
          stroke="#e5e7eb"
          strokeWidth="1"
        />

        <circle
          cx="32"
          cy="32"
          r="16"
          fill="none"
          stroke="#000"
          strokeWidth="2.4"
        />

        <text
          x="32"
          y="39"
          textAnchor="middle"
          fontFamily="Georgia, 'Times New Roman', serif"
          fontWeight="700"
          fontSize="17"
          fill="#000"
        >
          R
        </text>
      </svg>
    ),

    // Git
    git: (
      <svg {...commonProps}>
        <path
          d="M60.9 29.5 34.5 3.1a4 4 0 0 0-5.6 0l-5.7 5.7 7.2 7.2a4.7 4.7 0 0 1 6 6l6.9 6.9a4.7 4.7 0 1 1-2.8 2.7L33.4 24v17.9a4.7 4.7 0 1 1-3.9-.1V23.7a4.7 4.7 0 0 1-2.6-6.2l-7.1-7.1L3.1 26.9a4 4 0 0 0 0 5.6l26.4 26.4a4 4 0 0 0 5.6 0L60.9 35.1a4 4 0 0 0 0-5.6Z"
          fill="#F05033"
        />
      </svg>
    ),

    // GitHub
    github: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="10"
          fill="#181717"
        />

        <path
          d="M32 12.5c-10.8 0-19.5 8.8-19.5 19.5 0 8.6 5.6 15.9 13.3 18.5.9.2 1.3-.4 1.3-.9v-3.6c-5.4 1.2-6.6-2.6-6.6-2.6-.9-2.3-2.2-2.9-2.2-2.9-1.8-1.2.1-1.2.1-1.2 2 .1 3 2 3 2 1.7 3 4.6 2.1 5.7 1.6.2-1.3.7-2.1 1.2-2.6-4.3-.5-8.9-2.2-8.9-9.6 0-2.1.8-3.9 2-5.3-.2-.5-.9-2.5.2-5.3 0 0 1.6-.5 5.3 2 1.6-.4 3.2-.6 4.9-.6s3.3.2 4.9.6c3.7-2.5 5.3-2 5.3-2 1.1 2.8.4 4.8.2 5.3 1.2 1.4 2 3.2 2 5.3 0 7.4-4.6 9.1-8.9 9.6.7.6 1.3 1.9 1.3 3.8v5.6c0 .5.4 1.1 1.3.9C46.4 47.9 52 40.6 52 32c0-10.8-8.8-19.5-19.5-19.5Z"
          fill="#fff"
        />
      </svg>
    ),

    // SQL
    sql: (
      <svg {...commonProps}>
        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="10"
          fill="#fff"
          stroke="#e5e7eb"
          strokeWidth="1"
        />

        <ellipse
          cx="32"
          cy="18"
          rx="16"
          ry="6"
          fill="#00618A"
        />

        <path
          d="M16 18v9c0 3.3 7.2 6 16 6s16-2.7 16-6v-9"
          fill="none"
          stroke="#00618A"
          strokeWidth="2.6"
        />

        <path
          d="M16 27v9c0 3.3 7.2 6 16 6s16-2.7 16-6v-9"
          fill="none"
          stroke="#00618A"
          strokeWidth="2.6"
        />

        <path
          d="M16 36v9c0 3.3 7.2 6 16 6s16-2.7 16-6v-9"
          fill="none"
          stroke="#00618A"
          strokeWidth="2.6"
        />

        <path
          d="M22 46c2 5 4 8 8 8"
          fill="none"
          stroke="#E48E00"
          strokeWidth="2.6"
          strokeLinecap="round"
        />

        <path
          d="M30 50c1 2 2 3 4 3"
          fill="none"
          stroke="#E48E00"
          strokeWidth="2.2"
          strokeLinecap="round"
        />
      </svg>
    ),

    // PHP
    php: (
      <svg {...commonProps}>
        <ellipse
          cx="32"
          cy="32"
          rx="29"
          ry="18"
          fill="#787CB5"
        />

        <text
          x="32"
          y="38"
          textAnchor="middle"
          fontFamily="Georgia, serif"
          fontWeight="700"
          fontStyle="italic"
          fontSize="18"
          fill="#fff"
        >
          php
        </text>
      </svg>
    ),

    // Ruby
    ruby: (
      <svg {...commonProps}>
        <path
          d="M46 12 18 17l-9 17 25 22 28-22-4-16-12-6Z"
          fill="#9B111E"
        />

        <path
          d="M46 12 25 19l9 3 12-10Z"
          fill="#E0115F"
        />

        <path
          d="M18 17 9 34l16-13-7-4Z"
          fill="#E0115F"
        />

        <path
          d="M34 44 9 34l25 22 20-17-6-8-15 5-9-8Z"
          fill="#9B111E"
        />
      </svg>
    ),

    // Swift
    swift: (
      <svg {...commonProps}>
        <defs>
          <linearGradient
            id={`swift-${uniqueId}`}
            x1="0"
            y1="0"
            x2="1"
            y2="1"
          >
            <stop offset="0" stopColor="#F88B37" />
            <stop offset="1" stopColor="#F0513A" />
          </linearGradient>
        </defs>

        <rect
          x="2"
          y="2"
          width="60"
          height="60"
          rx="14"
          fill={`url(#swift-${uniqueId})`}
        />

        <path
          d="M44 16c5 4 8 10 6 16 0 0 0 1 1 2 2 3 5 7 5 7s-6 1-11-1c0 0-6 5-15 4-10-1-16-9-16-9s3 2 8 2c0 0-6-4-8-11 0 0 2 1 5 2 0 0-6-5-7-13 0 0 8 8 16 11 0 0-2-3-1-8 0 0 5 8 17 10 0 0-1-4 0-12Z"
          fill="#fff"
        />
      </svg>
    ),

    // Kotlin
    kotlin: (
      <svg {...commonProps}>
        <defs>
          <linearGradient
            id={`kotlin-${uniqueId}`}
            x1="0"
            y1="0"
            x2="1"
            y2="1"
          >
            <stop offset="0" stopColor="#E44857" />
            <stop offset="0.5" stopColor="#C711E1" />
            <stop offset="1" stopColor="#7F52FF" />
          </linearGradient>
        </defs>

        <path
          d="M6 6h52L34 32l24 26H6l28-26L6 6Z"
          fill={`url(#kotlin-${uniqueId})`}
        />
      </svg>
    ),
  };

  // Render exactly ONE language icon.
  if (icons[key]) {
    return icons[key];
  }

  // Fallback icon for unknown languages.
  return (
    <svg {...commonProps}>
      <rect
        x="4"
        y="4"
        width="56"
        height="56"
        rx="12"
        fill="#6366F1"
      />

      <text
        x="32"
        y="41"
        textAnchor="middle"
        fontFamily="Arial, sans-serif"
        fontWeight="700"
        fontSize="24"
        fill="#fff"
      >
        {(name || slug || "?").charAt(0).toUpperCase()}
      </text>
    </svg>
  );
};

export default LanguageIcon;