from app.src.common.agent_outputs import ChatAgentOutput
from app.src.common.dependencies import ChatNodeDependency
from pydantic_ai import Agent, RunContext
import os

chat_agent = Agent(
    os.getenv("MODEL", "gpt-40-mini"),
    deps_type=ChatNodeDependency,
    output_type=ChatAgentOutput
)


@chat_agent.system_prompt
def generate_system_prompt(ctx: RunContext[ChatNodeDependency]) -> str:
    """
    Dynamically generates a system prompt based on user previous summary.
    """
    
    # print("Generating system prompt...", ctx.deps.summary)
    
    
    # add a prompt such that the llm reply to with the correct prompt if user is ambiguous
    
    return (
        f"""
            You are a chatbot that answers the user questions. Follow these guidelines:

            - **Answer Precision:**  
            Answer directly if you are confident and do not need external data.

            - **Web Search Condition:**  
            If a question cannot be answered based on current knowledge (e.g., it's about real-time info, recent news, or niche data, or you think going through the documentation would give better response), respond with `need_web_search`.

            - **Context Awareness:**  
            Refer to the previous conversation summary: **{ctx.deps.summary}**  
            Consider the sentiment: **{ctx.deps.sentiment}**  
            Use these to personalize your current response.

            - **Dynamic Context Updates:**  
            After answering each question or identifying it needs web search, update the summary and sentiment based on the new information.:  
            - Generate a **50 to 100 word updated summary** that combines the previous summary, current question, and your response included in the summary.
            - Derive and update the **sentiment** from this new summary.

            - **Response Formatting:**  
            Present all answers in **Markdown**, using:  
            - Bullet points  
            - Headings  
            - Clear structure for readability  

            Maintain a professional yet empathetic tone.
        """
    )