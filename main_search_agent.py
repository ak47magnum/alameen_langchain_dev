from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

from dotenv import load_dotenv
load_dotenv()
import os
open_ai_key = os.environ.get("OPENAI_API_KEY")

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain.tools import tool



#############  dont need the below part because we are going to use the langchai_tavily library instead of our custom tool ####
# from tavily import TavilyClient
# tavily = TavilyClient()


# @tool
# def search(query: str) -> str:
#     """Tool that searches the internet.
#     Args:
#         query: The query to search for.
#     Returns:
#         The results of the search.
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

#############  dont need the above part because we are going to use the langchai_tavily library instead of our custom tool ####



llm = ChatOpenAI(model="gpt-5", temperature=0.0)
# llm = ChatOllama(model="gpt-oss:20b", temperature=0.0)
tools = [TavilySearch()]
agent = create_agent(llm, tools)






def main():
    # print("Hello World!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 linkedin job postings in the bay area for an ai engineer with experience using \
                                                      langchain,  and list their details",)]})  
    # result = agent.invoke({"messages": [HumanMessage(content=input("Enter your query: "))]})  ## AN example using the additional dynamic functionality of "input()"
    print(result)





if __name__ == "__main__":
    main()






