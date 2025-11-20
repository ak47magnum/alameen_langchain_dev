from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import json

from prompt import REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS
from schemas import AgentResponse

load_dotenv()
import os

open_ai_key = os.environ.get("OPENAI_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")

llm = ChatOpenAI(model="gpt-4", temperature=0.0)  ## As a note... ChatOllama() does not work with create_react_agent...Yet!!!
structured_llm = llm.with_structured_output(AgentResponse)

tools = [TavilySearch(tavily_api_key=tavily_api_key)]

# react_prompt = hub.pull("hwchase17/react")  ### we have switched to a custom prompt.."REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS" below. So not using this.

react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS, input_variables=["input", "agent_scratchpad", "tool_names", "tools"] ## "tools" was missing on e.marco's version
).partial(format_instructions="")

agent = create_react_agent(llm, tools, prompt=react_prompt_with_format_instructions)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

extract_output = RunnableLambda(lambda x: x["output"]) ## A langchain runnable that extracts the output from the agent executor
chain = agent_executor | extract_output | structured_llm


def main():
    print("Hello Langchain!")
    # result = chain.invoke(input={"input": "who is elon musk in three sentences?"})
    result = chain.invoke(
        input={"input": input("Enter your query: ")}  ## I used this for interesting results..."find three listings for a 2 bedroom flat in the wuse area of abuja"
    )  ## Using the "input()" function to allow for dynamic user input



    print(result)  
    # print(result.output)  
    # print(result.sources)  


    # #### testing a parsed output using langchain's parsers... WORKS!!
    # parsed_result = output_parser.parse(result["output"])
    # print(parsed_result)




    ## Testing a    little json conversion and 
    ### A little working example of how to parse the output into a json object and then print the sources
    # final_result = json.loads(result["output"])
    # for i, j  in enumerate(final_result["sources"]):
    #     print(i, j["source_url"])


   

if __name__ == "__main__":
    main()







