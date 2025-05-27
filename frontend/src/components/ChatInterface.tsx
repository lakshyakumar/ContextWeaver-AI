import { useState, useRef, useEffect } from 'react';
import {
  Box,
  VStack,
  Button,
  Container,
  Text,
  Flex,
  Input,
  Icon,
  useColorMode,
} from '@chakra-ui/react';
import { chatService } from '../services/chatService';
import type { Message } from '../types/chat';

export const ChatInterface = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const { colorMode } = useColorMode();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async () => {
    if (!input.trim()) return;

    try {
      setLoading(true);
      const userMessage: Message = {
        type: 'user',
        content: input,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, userMessage]);
      setInput('');

      const result = await chatService.sendMessage(input);
      console.log('Response from backend:', result);

      const assistantMessage: Message = {
        type: 'assistant',
        content: result.response,
        timestamp: new Date(),
        summary: result.summary,
        sentiment: result.sentiment,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Flex direction="column" h="100vh" w="80vw" bg={colorMode === 'dark' ? 'gray.900' : 'gray.50'}>
      <Box flex="1" overflowY="auto" px={4} py={6}>
        {messages.length === 0 ? (
          <Flex
            direction="column"
            align="center"
            justify="center"
            h="100%"
            color={colorMode === 'dark' ? 'gray.400' : 'gray.600'}
            textAlign="center"
          >
            <Icon viewBox="0 0 24 24" boxSize={16} mb={4}>
              <circle cx="12" cy="12" r="10" fill="currentColor" opacity={0.2} />
              <path
                d="M12 6v12M6 12h12"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
              />
            </Icon>
            <Text fontSize="xl" mb={2}>
              Ask me anything about any topic
            </Text>
            <Text fontSize="sm">
              I'm here to help!
            </Text>
          </Flex>
        ) : (
          messages.map((message, index) => (
            <Flex
              key={index}
              justify={message.type === 'user' ? 'flex-end' : 'flex-start'}
              mb={6}
            >
              <Box
                maxW="70%"
                bg={
                  message.type === 'user'
                    ? 'blue.500'
                    : colorMode === 'dark'
                    ? 'gray.700'
                    : 'white'
                }
                color={message.type === 'user' || colorMode === 'dark' ? 'white' : 'gray.800'}
                p={4}
                borderRadius="lg"
                boxShadow="lg"
              >
                <Text>{message.content}</Text>
                {message.type === 'assistant' && message.summary && (
                  <Text fontSize="xs" color={colorMode === 'dark' ? 'gray.300' : 'gray.600'} mt={2}>
                    Summary: {message.summary}
                  </Text>
                )}
                {message.type === 'assistant' && message.sentiment && (
                  <Text fontSize="xs" color={colorMode === 'dark' ? 'gray.300' : 'gray.600'}>
                    Sentiment: {message.sentiment}
                  </Text>
                )}
                <Text fontSize="xs" color={colorMode === 'dark' ? 'gray.400' : 'gray.500'} mt={2}>
                  {message.timestamp.toLocaleTimeString()}
                </Text>
              </Box>
            </Flex>
          ))
        )}
        <div ref={messagesEndRef} />
      </Box>

      <Box p={4} borderTop="1px solid" borderColor={colorMode === 'dark' ? 'gray.700' : 'gray.200'}>
        <Container maxW="container.lg">
          <Flex>
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Message ContextWeaver..."
              size="lg"
              bg={colorMode === 'dark' ? 'gray.800' : 'white'}
              border="none"
              color={colorMode === 'dark' ? 'white' : 'gray.800'}
              _placeholder={{ color: colorMode === 'dark' ? 'gray.400' : 'gray.500' }}
              _focus={{
                boxShadow: 'none',
                bg: colorMode === 'dark' ? 'gray.700' : 'gray.50',
              }}
              onKeyPress={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  handleSubmit();
                }
              }}
              mr={4}
            />
            <Button
              colorScheme="blue"
              size="lg"
              px={8}
              isLoading={loading}
              onClick={handleSubmit}
              bg="blue.500"
              _hover={{ bg: 'blue.600' }}
            >
              Send
            </Button>
          </Flex>
          <Text fontSize="xs" color={colorMode === 'dark' ? 'gray.500' : 'gray.600'} mt={2} textAlign="center">
            ContextWeaver can make mistakes, so double-check its responses.
          </Text>
        </Container>
      </Box>
    </Flex>
  );
}; 