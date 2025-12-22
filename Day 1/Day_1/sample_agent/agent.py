from google.adk.agents import Agent #base Agent class.
from google.adk.models.google_llm import Gemini #engine or the "brain" of your agent.
from google.adk.runners import InMemoryRunner #environment where the agent actually "lives" and executes its loop.
from google.adk.tools import google_search #allow it to look up real-time information on the internet
from google.genai import types #define specific configurations.

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

root_agent = Agent(
    name="helpful_assistant",  #internal identifier for the agent
    model=Gemini(
        model="gemini-2.5-flash-lite",  #specifies the version of the Gemini model to use
        retry_options=retry_config  #plugs in the retry logic
    ),
    description="A simple agent that can answer general questions.", #high-level summary of what the agent is for
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.", #tells the agent how to behave
    tools=[google_search], #gives the agent its "external capabilities.
)

runner = InMemoryRunner(agent=root_agent) #initializes the execution engine for your agent.