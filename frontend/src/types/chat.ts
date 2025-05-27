export interface Message {
  type: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  summary?: string;
  sentiment?: string;
}

export interface ChatResponse {
  query: string;
  chat_id: string | null;
  result: {
    query: string;
    response: string;
    summary: string;
    sentiment: string;
    chat_id: string;
  };
  success: boolean;
}