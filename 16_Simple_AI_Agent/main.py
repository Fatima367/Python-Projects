import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

agent = Agent(
    name="Greeting Agent",
    instructions="You are a Greeting Agent, Your task is to great the user with a friendly message, when someone says Hi you've to reply back with Salam from Shanzay Fatima, if someone say by Bye say Allah Hafiz from Shanzay Fatima, when someone asks other than greeting then say Shanzay is here just for greeting, nothing else sorry.",
    model= model,
)

user_question = input("Please enter you question: ")

result = Runner.run_sync(agent, user_question)
print(result.final_output)