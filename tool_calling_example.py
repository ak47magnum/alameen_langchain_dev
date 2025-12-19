from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description 
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from ollama import chat, ChatResponse
# from langchain_anthropic import ChatAnthropic


load_dotenv()


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_tavily import TavilySearch  ## This is the latest langchain search tool for using tavily





@tool
def multiply(x: float, y: float) -> float:
    """Multiply 'x' times 'y'."""
    return x * y

@tool
def exponentiate(x: float, y: float) -> float:
    """Raise 'x' to the 'y'."""
    return x**y

@tool
def add(x: float, y: float) -> float:
    """Add 'x' and 'y'."""
    return x + y

@tool
def subtract(x: float, y: float) -> float:
    """Subtract 'y' from 'x'."""
    return x - y




prompt = ChatPromptTemplate.from_messages([
    ("system", "you're a helpful assistant"), 
    ("human", "{input}"), 
    ("placeholder", "{agent_scratchpad}"),
])

tools = [multiply, exponentiate, add, subtract, TavilySearch()]




# llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)  ############ ******** I need credits to use anthropic API *****************
#
# llm = ChatOllama(model="gpt-oss:20b", temperature=0.0) ## Not very accurate
# llm = ChatOllama(model="llama3.1:8b", temperature=0.0)  ## Can have errors... but overall pretty good. I like this one for a local model!!!!!!!



# llm = ChatOpenAI(model="gpt-5", temperature=0) ## real slow and expensive  - (support tool calling)
# llm = ChatOpenAI(model="gpt-4-turbo", temperature=0) ## Quicker but still expensive - (support tool calling)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) ## Quicker and cheaper - (support tool calling)
# llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0) ## Also Quicker and cheaper - (support tool calling)
llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0) ## Also Quicker and cheaper - (support tool calling). I like this one for a paid model!!!!!!



agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# agent_executor.invoke({"input": "what's 3 plus 5 raised to the 2.743. also what's 17.24 - 918.1241", }) ## uses calculation tools
# agent_executor.invoke({"input": "get me a list of three 2 bedroom apartments for sale on queensway in london", }) ## Uses TavilySearch() tool
res = agent_executor.invoke({"input": "What is the weather like in london uk and in minsk \
                       belarus today? And what is the difference between the two in celsius?", }) ## Uses TavilySearch() tool

print(res)