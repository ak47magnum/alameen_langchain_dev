from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS
from schemas import AgentResponse

load_dotenv()
import os

open_ai_key = os.environ.get("OPENAI_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")


llm = ChatOpenAI(
    model="gpt-4", temperature=0.0, openai_api_key=open_ai_key
)  ## As a note... ChatOllama() does not work with create_react_agent...Yet!!!

tools = [TavilySearch(tavily_api_key=tavily_api_key)]
# react_prompt = hub.pull("hwchase17/react")  ### we have switched to a custom prompt.."REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS". So not using this.

output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS, input_variables=["input", "agent_scratchpad", "tool_names"]
).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(llm, tools, prompt=react_prompt_with_format_instructions)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    print("Hello Langchain!")
    # result = chain.invoke(input={"input": "who is elon musk in three sentences?"})
    result = chain.invoke(
        input={"input": input("Enter your query: ")}
    )  ## Using the "input()" function to allow for dynamic user input
    print(result)


if __name__ == "__main__":
    main()







