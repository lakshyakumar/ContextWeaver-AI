import streamlit as st
import requests
import json
from typing import Dict, List
import os

st.set_page_config(
    page_title="ContextWeaver AI",
    page_icon="🧠",
    layout="wide"
)

API_BASE_URL = "http://localhost:8000"

def initialize_session_state():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat_id' not in st.session_state:
        st.session_state.chat_id = None

def get_project_info() -> Dict:
    """Fetch project information from the backend."""
    try:
        response = requests.get(f"{API_BASE_URL}/")
        return response.json()
    except Exception as e:
        st.error(f"Error fetching project info: {str(e)}")
        return {}

def send_message(message: str) -> Dict:
    """Send a message to the backend API and get the response."""
    try:
        # Only include chat_id in params if it exists
        params = {"query": message}
        if st.session_state.chat_id:
            params["chat_id"] = st.session_state.chat_id
            
        response = requests.get(f"{API_BASE_URL}/query/", params=params)
        response_data = response.json()
        
        if response_data.get("success", False):
            # Update chat_id from the response if we don't have one yet
            if not st.session_state.chat_id and response_data.get("chat_id"):
                st.session_state.chat_id = response_data["chat_id"]
            
            # Update the response with the result
            return response_data
        return {}
    except Exception as e:
        st.error(f"Error communicating with backend: {str(e)}")
        return {}

def main():
    initialize_session_state()
    
    # Sidebar with project info
    with st.sidebar:
        st.title("🧠 ContextWeaver AI")
        project_info = get_project_info()
        if project_info:
            st.write(f"Version: {project_info.get('version', 'N/A')}")
            st.write(f"Description: {project_info.get('description', 'N/A')}")
            
            if st.session_state.chat_id:
                st.write(f"Current Chat ID: {st.session_state.chat_id}")
        
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.session_state.chat_id = None
            st.rerun()

    st.header("Chat with ContextWeaver AI")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = send_message(prompt)
                if response and response.get("success", False):
                    # Display the response
                    bot_response = response.get("result", {}).get("response", "Sorry, I couldn't process that.")
                    st.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
                else:
                    st.error("Failed to get response from the backend.")

if __name__ == "__main__":
    main() 