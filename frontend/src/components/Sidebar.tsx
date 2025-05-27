import { Box, Button, VStack, Text, Icon, useColorMode } from '@chakra-ui/react';
import { AddIcon, SunIcon, MoonIcon } from '@chakra-ui/icons';
import { chatService } from '../services/chatService';

export const Sidebar = () => {
  const { colorMode, toggleColorMode } = useColorMode();

  const handleNewChat = () => {
    chatService.clearSession();
    window.location.reload();
  };

  return (
    <Box
      w="300px"
      h="100%"
      bg="gray.800"
      p={4}
      color="white"
      borderRight="1px solid"
      borderColor="gray.700"
    >
      <VStack spacing={4} align="stretch" h="100%">
        <Button
          leftIcon={<AddIcon />}
          colorScheme="blue"
          size="lg"
          borderRadius="full"
          bg="blue.500"
          _hover={{ bg: 'blue.600' }}
          onClick={handleNewChat}
        >
          New chat
        </Button>

        <Box flex="1">
          <Text mb={2} color="gray.400" fontWeight="medium">
            Chat history
          </Text>
          <VStack align="stretch" spacing={2}>
            <Button
              variant="ghost"
              justifyContent="flex-start"
              color="gray.300"
              _hover={{ bg: 'gray.700' }}
              leftIcon={<Icon viewBox="0 0 24 24" boxSize={5}>
                <circle cx="12" cy="12" r="8" fill="currentColor" opacity={0.4} />
              </Icon>}
              onClick={handleNewChat}
            >
              New Chat
            </Button>
          </VStack>
        </Box>

        <Button
          variant="ghost"
          leftIcon={colorMode === 'light' ? <MoonIcon /> : <SunIcon />}
          justifyContent="flex-start"
          color="gray.300"
          _hover={{ bg: 'gray.700' }}
          onClick={toggleColorMode}
        >
          {colorMode === 'light' ? 'Dark mode' : 'Light mode'}
        </Button>
      </VStack>
    </Box>
  );
}; 