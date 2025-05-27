import { Box, Flex, ChakraProvider } from '@chakra-ui/react';
import { ChatInterface } from './components/ChatInterface';
import { Sidebar } from './components/Sidebar';
import theme from './theme';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Flex h="100vh" bg="gray.900">
        <Sidebar />
        <Box flex="1">
          <ChatInterface />
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
