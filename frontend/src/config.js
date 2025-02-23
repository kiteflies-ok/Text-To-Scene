export const CONFIG = {
    API_BASE_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
    MAX_FILE_SIZE: 5 * 1024 * 1024, // 5MB
    SUPPORTED_FORMATS: ['application/pdf', 'text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
    DEFAULT_ANIMATION_SETTINGS: {
      resolution: '1080p',
      voiceSpeed: 1.0,
      stylePreset: 'infographic'
    },
    THEME_COLORS: {
      primary: '#2563eb',
      secondary: '#1e40af',
      accent: '#7c3aed'
    }
  };