import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=1024,
)

# Agent task prompt
task = (
    "Use the go_to_url tool to open https://www.linkedin.com/login. Do not use Google.\n"
    "Then:\n"
    "1. Type 'samarthssingh5@gmail.com' into the input field with name='session_key'\n"
    "2. Type 'Solitude@123' into the input field with name='session_password'\n"
    "3. Click the button labeled 'Sign in'\n"
    "4. Wait for 5 seconds\n"
    "5. Navigate to the following job search URL:\n"
    "   https://www.linkedin.com/jobs/search/?currentJobId=4239789255&distance=25&f_AL=true&f_E=2%2C3&f_JT=F&f_TPR=r86400&f_VJ=true&geoId=103644278&keywords=robotics%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R\n"
    "6. Scroll to load more jobs if necessary\n"
    "7. For each job listed with the 'Easy Apply' tag:\n"
    "   - Click on the job card\n"
    "   - Click the 'Easy Apply' button\n"
    "   - Click the 'Next' button (if visible)\n"
    "   - Click the 'Submit' button to complete the application\n"
    "   - Log the job title that was applied to\n"
    "Respond step by step and handle each job card sequentially."
)

async def main():
    agent = Agent(
        task=task,
        llm=llm
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
