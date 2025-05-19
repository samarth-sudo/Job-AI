import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    base_url="https://api.together.xyz/v1",
    api_key=os.getenv("TOGETHER_API_KEY"),
    temperature=0.5,
    max_tokens=1024
)

async def main():
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    task = (
    "Open https://www.linkedin.com/login and log in using the credentials below:\n"
    f"- Email: {email}\n- Password: {password}\n\n"
    "After login, go directly to this URL: https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst%20Remote"
    "&f_AL=true"                        # Easy Apply filter
    "&f_E=2"                            # Entry level
    "&f_TP=1"                           # Past 24 hours
    "&origin=JOB_SEARCH_PAGE_JOB_FILTER\n\n"
    "Once on the page, scroll down, extract the titles of the first 10 job cards, and return them."
)


    agent = Agent(
        task=task,
        llm=llm
    )

    await agent.run()

asyncio.run(main())
