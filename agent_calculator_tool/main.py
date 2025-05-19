from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Perform a simple addition of two numbers."""
    print("Toll has been called")
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! How can I assist you today?"

def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]},
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()