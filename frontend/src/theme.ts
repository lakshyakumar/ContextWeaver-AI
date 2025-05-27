import { extendTheme, type ThemeConfig } from '@chakra-ui/react';

const config: ThemeConfig = {
  initialColorMode: 'dark',
  useSystemColorMode: false,
};

const theme = extendTheme({
  config,
  styles: {
    global: (props: { colorMode: 'light' | 'dark' }) => ({
      body: {
        bg: props.colorMode === 'dark' ? 'gray.900' : 'white',
        color: props.colorMode === 'dark' ? 'white' : 'gray.800',
      },
    }),
  },
  components: {
    Button: {
      defaultProps: {
        colorScheme: 'blue',
      },
    },
    Input: {
      variants: {
        outline: {
          field: {
            _focus: {
              borderColor: 'blue.500',
              boxShadow: '0 0 0 1px var(--chakra-colors-blue-500)',
            },
          },
        },
      },
    },
  },
  colors: {
    gray: {
      700: '#2D3748',
      800: '#1A202C',
      900: '#171923',
    },
  },
});

// Enable color mode persistence
if (typeof window !== 'undefined') {
  const colorModeManager = {
    type: 'localStorage',
    get: () => {
      return localStorage.getItem('chakra-ui-color-mode') || 'dark';
    },
    set: (value: string) => {
      localStorage.setItem('chakra-ui-color-mode', value);
    },
  };

  (window as any).__CHAKRA_COLOR_MODE__ = colorModeManager;
}

export default theme; 