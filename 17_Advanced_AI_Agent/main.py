import os 
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@function_tool("get_weather")
def get_weather(location:str, unit:str ="C")->str:
    """
    Fetch the weather for a given location, return the weather
    """
    return f"The weather in {location} is 22 degrees {unit}"


# Create an greeting agent with instructions, and model
agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent designed to provide friendly interactions and information about Asharib Ali.

        Your responsibilities:
        1. Greet users warmly when they say hello (respond with 'Salam from Shanzay Fatima')
        2. Say goodbye appropriately when users leave (respond with 'Allah Hafiz from Shanzay Fatima')
        3. When users request information about Shanzay Fatima, use the get_asharib_data tool to retrieve and share his profile information
        4. For any questions not related to greetings or Shanzay Fatima, politely explain: 'I'm only able to provide greetings and information about Shanzay Fatima. I can't answer other questions at this time.'

        Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
    model=model,
    tools=[get_weather]
)


@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])

    await cl.Message(content= "Hello! How can I help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")

    history.append({"role" : "user" , "content" : message.content})

    formatted_history = []

    for msg in history:
        role = "user" if msg["role"] == "user" else "model"

        formatted_history.append({"role" : role, "parts": [{"text": msg["content"]}]})
    
    response = model.generate_content(formatted_history)

    response_text = response.text if hasattr(response, "text") else ""

    history.append({"role": "assistant", "content": response_text})
    
    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output

    await cl.Message(content=response_text).send()

    history.append({"role":"assistant", "content": response_text})
    cl.user_session.set("history", history)