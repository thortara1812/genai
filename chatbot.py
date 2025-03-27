from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Set OpenRouter API Key and Base URL
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the Chat Model with API Key
chat_model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
)

def chat_with_ai():
    print("Chatbot is ready! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_model.invoke([HumanMessage(content=user_input)])
        print("AI:", response.content)

# Run the chatbot
chat_with_ai()
