import axios from 'axios';
import type { ChatResponse } from '../types/chat';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';


class ChatService {
  private sessionId: string | null = null;

  constructor() {
    // Try to get existing session ID from localStorage
    this.sessionId = localStorage.getItem('chat_session_id');
  }

  private setSessionId(sessionId: string) {
    this.sessionId = sessionId;
    localStorage.setItem('chat_session_id', sessionId);
  }

  async sendMessage(message: string): Promise<ChatResponse['result']> {
    try {
      const response = await axios.get<ChatResponse>(`${API_BASE_URL}/query`, {
        params: {
          query: message,
          chat_id: this.sessionId,
        }
      });

      // If we get a new session ID, store it
      if (response.data.result.chat_id) {
        this.setSessionId(response.data.result.chat_id);
      }

      return response.data.result;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  }

  clearSession() {
    this.sessionId = null;
    localStorage.removeItem('chat_session_id');
  }
}

export const chatService = new ChatService();
