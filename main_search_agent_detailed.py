from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent


from dotenv import load_dotenv
load_dotenv()
import os
open_ai_key = os.environ.get("OPENAI_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain.tools import tool






llm = ChatOpenAI(model="gpt-4", temperature=0.0, openai_api_key=open_ai_key)
tools = [TavilySearch(tavily_api_key=tavily_api_key)]
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=react_prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    print("Hello Langchain!")
    result = chain.invoke(input={"input": "who is elon musk in three sentences?"})  
    print(result)
if __name__ == "__main__":  
    main()



















# #############  dont need the below part because we are going to use the langchain_tavily library...."TavilySearch()", instead of our custom tool #### TEST BLOCK
# # from tavily import TavilyClient
# # tavily = TavilyClient()


# # @tool
# # def search(query: str) -> str:
# #     """Tool that searches the internet.
# #     Args:
# #         query: The query to search for.
# #     Returns:
# #         The results of the search.
# #     """
# #     print(f"Searching for {query}")
# #     return tavily.search(query=query)

# #############  dont need the above part because we are going to use the langchai_tavily library instead of our custom tool ####




 
# class Source(BaseModel):
#     """Schema for a source used by the agent."""
#     url: str = Field(description="The url of the source")
 

# class AgentResponse(BaseModel):
#     """Schema for the agent response with answer and sources"""
#     answer: str = Field(description="The agent's answer to the query")
#     sources: list[Source] = Field(default_factory=list, description="The list of sources used by the agent to generate the answer")

# llm = ChatOpenAI(model="gpt-5", temperature=0.0)
# # llm = ChatOllama(model="gpt-oss:20b", temperature=0.0)
# tools = [TavilySearch()]
# agent = create_agent(llm, tools, response_format=AgentResponse)






# def main():
#     # print("Hello World!")
#     result = agent.invoke({"messages": [HumanMessage(content="search for 3 linkedin job postings in the bay area for an ai engineer with experience using \
#                                                       langchain,  and list their details",)]})  
#     # result = agent.invoke({"messages": [HumanMessage(content=input("Enter your query: "))]})  ## AN example using the additional dynamic functionality of "input()"
#     print(result)





# if __name__ == "__main__":
#     main()






