from dotenv import load_dotenv
load_dotenv()

from google.adk.agents import LlmAgent
from typing import Dict
from google.adk.tools import AgentTool
from Investment_Plan_Agent.agent import investment_plan_agent


# CUSTOM TOOLS

def get_user_personal_finance_details() -> Dict:
    """
    Gets users personal finance details like salary, expense and savings capacity.
    """
    return {
        "salary": 43000,
        "expense": {
            "rent": 1500,
            "groceries": 500,
            "utilities": 300,
            "entertainment": 200
        },
        "savings": 7000
    }

# BUILT IN TOOLS + CUSTOM TOOLS AGENT
finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A friendly finance assistant that helps users with finance questions and planning.",
    instruction="""
You are a friendly finance assistant.

You help answer generic finance questions and assist users in planning
their financial goals. Be friendly, clear, and positive.

You have two tools available:

1. get_user_personal_finance_details  
   - Use this to understand the user's salary, expenses, and savings.

2. investment_plan_agent  
   - Use this agent whenever latest or real-time information is required.
   - This agent can search the web and ask follow-up questions to help plan savings and investments.

ALWAYS use the investment_plan_agent when asked about:
- Stock prices (e.g., "Tesla stock price", "TSLA latest price")
- Market data, financial news, or company information
- Any question containing words like "current", "today", "now", or "recent"
""",
    tools=[
        AgentTool(investment_plan_agent),
        get_user_personal_finance_details
    ]
)

    # tool = if the data persists in knowledge base, it can be retrieved using retrieval tools or else google search can be used.



# BASE AGENT

root_agent = finance_assistance_agent
