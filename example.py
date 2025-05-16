import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain.chat_models import ChatOpenAI

# Load GROQ_API_KEY from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLaMA 3 from Groq using OpenAI-compatible endpoint
llm = ChatOpenAI(
    model="llama3-8b-8192",  # You can also try "llama3-70b-8192"
    temperature=0.7,
    max_tokens=1024,
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",  # Required override
)

# Async run with browser-use agent
async def main():
    agent = Agent(
        task="Search LinkedIn for data science jobs and summarize the top 3 with application links.",
        llm=llm
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
