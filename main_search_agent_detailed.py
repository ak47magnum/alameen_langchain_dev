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

react_prompt = hub.pull("hwchase17/react")  ### we have switched to a custom prompt.."REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS" below. So not using this.

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





####################### QUESTION 1: PROMPT FOR EXPLAINING THE CODE ABOVE 👇###########################################################################

# could you pleaseexplain the code below to me in a way that i might understand the way langcahin works with these 
# various llm's and parsers. How the parsers are connected to he llm. Also how does the structuring of the output of the llm work? 
# The result that is  produced by the llm... is it text, json, or what. 
# I have seen  fields like, "answer", "output", "tools" , are these standard fields or are the field names different for different models . 
# i am really trying to understand the parsing of outputs from llm's and i know this is important for real world apps cos you might need 
# to forward the data down an app pipeline in a spcific format. Anyway see the code and try to give me an explainer with a standard template 
# or formukaI might follow to parse an llp output however I want.




# See code below

# from dotenv import load_dotenv
# from langchain_classic import hub
# from langchain_classic.agents import AgentExecutor
# from langchain_classic.agents.react.agent import create_react_agent
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableLambda
# from langchain_ollama import ChatOllama
# from langchain_openai import ChatOpenAI
# from langchain_tavily import TavilySearch
# import json

# load_dotenv()
# import os

# from typing import List

# from pydantic import BaseModel, Field

# class Source(BaseModel):
# """
# Schema for the source used by the agent.
# """

# code
# Code
# download
# content_copy
# expand_less
# source_url: str = Field(description="The url of the source")

# class AgentResponse(BaseModel):
# """
# Schema for the agent's response with answer and sources.
# """

# code
# Code
# download
# content_copy
# expand_less
# answer: str = Field(description="The answer to the query")
# sources: List[Source] = Field(
#     default_factory=list, description="The sources used to answer the query"
# )  ## The Source class in List[Source], is defined above..

# REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS = """
# Answer the following questions as best you can. You have access to the following tools:

# {tools}
# Use the following format:

# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question
# formatted according to format_instructions: {format_instructions}.

# Begin!

# Question: {input}
# Thought: {agent_scratchpad}
# """

# open_ai_key = os.environ.get("OPENAI_API_KEY")
# tavily_api_key = os.environ.get("TAVILY_API_KEY")

# llm = ChatOpenAI(model="gpt-4", temperature=0.0)  ## As a note... ChatOllama() does not work with create_react_agent...Yet!!!
# structured_llm = llm.with_structured_output(AgentResponse)

# tools = [TavilySearch(tavily_api_key=tavily_api_key)]

# react_prompt = hub.pull("hwchase17/react")  ### we have switched to a custom prompt.."REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS" below. So not using this.

# react_prompt_with_format_instructions = PromptTemplate(
# template=REACT_PROMPT_WITH_FORMAT_ISTRUCTIONS, input_variables=["input", "agent_scratchpad", "tool_names", "tools"] ## "tools" was missing on e.marco's version
# ).partial(format_instructions="")

# agent = create_react_agent(llm, tools, prompt=react_prompt_with_format_instructions)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# extract_output = RunnableLambda(lambda x: x["output"]) ## A langchain runnable that extracts the output from the agent executor
# chain = agent_executor | extract_output | structured_llm

# def main():
# print("Hello Langchain!")
# # result = chain.invoke(input={"input": "who is elon musk in three sentences?"})
# result = chain.invoke(
# input={"input": input("Enter your query: ")}  ## I used this for interesting results..."find three listings for a 2 bedroom flat in the wuse area of abuja"
# )  ## Using the "input()" function to allow for dynamic user input

# code
# Code
# download
# content_copy
# expand_less
# print(result)

# if name == "main":
# main()






############################################### QUESTION 2: PROMPT 2 FOR ADDITIONAL EXPLANATION #########################################################################################



# User
# ok...so.... from propt templates...is there a standard for names of variables like {tools}, or {tool_names} or {input} or {agent_scratchpad} that need to be adhered to in the code for models to recognise? aAlso keyword like Question:, Thought: , Action:, Action Input:, Thought:, and Final Answer:.... are these standards? how do i consistently reference these diffrerent pieces of data in my code. my question might be all over the place, but again I am trying to understand the rules of working with models, how to prompt them . how to pares output to a certain format that I need and how the workflow chain works when creating meaningful and useful AI projects using llm's.
# So far I seem to be all over the place. I feel like there is no set rules or standards to working with LLM's.
# For example, learning about python functions or classes or loops, have a defined set of rules to follow. These never change. They are set in stone. I want the same type of understanding when it comes to working with models. At the moment I feel like its all about how clever you are with prompts. Which is ok, but I want to understand the technivcal fundamentals and be told what the set rules are no matter the type of prompt used. Also, Is the  langchain expression language the standard here?



# Model:

# This is the specific "Aha!" moment every developer needs to have when moving from standard coding (Python/Java) to AI Engineering.

# You are absolutely right: Python has syntax errors; LLMs have "drift." In Python, if you miss a parenthesis, the code crashes immediately. In LLMs, if you name a variable wrong or mess up a keyword, the model just talks nonsense, and you don't know why.

# Here are the Set Rules and Standards you are looking for.

# 1. Variable Names ({tools}, {input}, {agent_scratchpad})

# Are these universal standards? No. The LLM (GPT-4) does not care what these are called.
# Are they Framework standards? Yes.

# This is where the "Rules" come in.

# The Rule: If you use a pre-built function like create_react_agent(), you MUST use the variable names that the function creators hard-coded into their internal code.

# LangChain's create_react_agent code internally looks for a variable called agent_scratchpad to inject the conversation history. If you rename it to {history} in your prompt, the Python code will crash (KeyError) because it can't find the variable it expects to fill.

# The Exception: If you build a chain from scratch (using just PromptTemplate | LLM), you can name variables whatever you want.

# You could use {user_stuff} instead of {input}.

# You could use {magic_box} instead of {tools}.

# Constraint: Your Python dictionary keys passed into .invoke() MUST match the {} names in the prompt string.

# 2. The Keywords (Question:, Action:, Observation:)

# Are these standards? They are Patterns, not syntax.

# These specific keywords come from a research paper called ReAct (Reasoning + Acting).

# How it works technically:

# The Prompt: You tell the LLM: "When you want to run a tool, type the word 'Action:' followed by the tool name."

# The Parser (Python Code): LangChain has a Regex parser running in the background. It is literally doing something like: text.split("Action:").

# The "Set Rule" (The Contract):
# This is the Prompt-Parser Handshake.

# If you change the Prompt to say Please execute: [Tool Name], but your Python Parser is still looking for the word Action:, your app breaks.

# Rule: You can change the keywords to anything (e.g., THOUGHT, COMMAND, RESULT), but you must update both the Prompt text AND the Parsing logic simultaneously.

# 3. How to consistently reference pieces of data (The Pipeline Formula)

# If you want a "formula" like a Python loop, here is the Data Flow Architecture for almost every LLM app:

# State A: The Input Dictionary
# This is your entry point.

# code
# Python
# download
# content_copy
# expand_less
# # The keys here MUST match the {variables} in your Prompt Template
# data = {
#     "input": "Who is Elon?",
#     "context": "Use this data...",
# }

# State B: The Prompt Rendering
# LangChain replaces the {} with the values from State A.

# Result: A giant string of text.

# State C: The LLM Generation
# The LLM receives the string. It predicts the next tokens.

# Result: A giant string of text (The Output).

# State D: The Parsing (The Critical Step)
# This is where you turn "Text" back into "Data".

# Result: JSON, Pydantic Object, or a Dict.

# 4. Is LangChain Expression Language (LCEL) the standard?

# Is it an Industry Standard? No. It is a LangChain Standard.
# If you use other libraries (like LlamaIndex, Haystack, or raw OpenAI SDK), you won't see the pipe | syntax.

# Should you learn it?
# If you are using LangChain, yes. It handles the "invisible glue" code for you.

# Without LCEL: You have to manually write prompt.format(), then llm.predict(), then parser.parse().

# With LCEL (prompt | llm | parser): It passes the output of one to the input of the other automatically.

# The "Set Rules" Checklist for LLM Engineers

# Since you want strict rules like Python has, here is your checklist to ensure your code works every time:

# The Variable Match Rule:
# Look at your PromptTemplate. Every word inside curly braces {variable} MUST exist as a key in the dictionary you pass to .invoke(). If it's missing, it crashes.

# The Stop Sequence Rule:
# If you are building an Agent (loop), the LLM needs to know when to stop talking and let the Python code run.

# Standard: The LLM types Action Input: "search term".

# Rule: You must tell the LLM (via prompt) "Stop generating after you type 'Action Input'". (LangChain usually handles this, but knowing it helps debugging).

# The Type Contract Rule:

# LLMs always output Strings.

# If you want JSON, you must Force it (using .with_structured_output or strict prompt engineering).

# Never assume the LLM will output clean data unless you have a distinct parsing step (like your structured_llm code).

# Summary of your specific code

# In the code you posted:

# {tools}, {tool_names}, {agent_scratchpad} are Mandatory because you used create_react_agent. That function is hard-coded to look for them.

# Question:, Thought: are Mandatory because the internal LangChain parser is writing Regex expressions looking for those exact words to figure out what the Agent is doing.

# If you want total freedom, you stop using create_react_agent and build a simple chain (prompt | llm), where you define every single word and rule yourself!




############################################### QUESTION 3 : ANOTHER QUESTION ABOUT PARCING ############################################################


# User:
# So what part of my code is doing the parcing. I dont see the word "parse" in this version of the project?


# Model:

# You don't see the word "parse" because modern LangChain (v0.1+) has hidden it inside the LLM call itself.

# In the "old days" (2023), you would see lines like parser.parse(text).
# In your code, the parsing is happening in two specific places, but it looks different.

# Here is exactly where the parsing logic lives in your script:

# 1. The "Data Structure" Parser (The Main One)

# This is the line that converts the text into your JSON/Pydantic object:

# code
# Python
# download
# content_copy
# expand_less
# structured_llm = llm.with_structured_output(AgentResponse)

# How this is "Parsing":

# Old Way: You would get a string back from the LLM, then pass it to a separate parser object to clean it up.

# This Way (Function Calling):

# When you run .with_structured_output(AgentResponse), LangChain takes your Pydantic class (AgentResponse).

# It translates that class into a JSON Schema.

# It sends that schema to OpenAI and says: "Don't give me text. Give me arguments that match this schema."

# OpenAI sends back a JSON string.

# The Hidden Parser: Inside the .with_structured_output function, there is code that automatically takes that JSON and converts it into your python AgentResponse object.

# So, the "parser" is effectively baked into this single line of code.

# 2. The "ReAct" Parser (The Hidden One)

# You asked earlier about Action:, Observation:, and Thought:. You don't see the code checking for these words, but it is running here:

# code
# Python
# download
# content_copy
# expand_less
# agent = create_react_agent(llm, tools, prompt=react_prompt_with_format_instructions)

# How this is "Parsing":

# Inside the create_react_agent function, LangChain loads a specific class called ReActSingleInputOutputParser.

# What it does: It uses Regular Expressions (Regex).

# It looks at the text coming from the LLM.

# It scans for the specific pattern Action: [Tool Name].

# If it finds it, it "parses" that into a command to run the tool.

# If it finds Final Answer:, it "parses" that as the signal to stop the loop.

# You cannot see this parser because create_react_agent sets it up automatically in the background.

# 3. The "Glue" Parser (The Manual One)

# There is one tiny piece of parsing you did write explicitly:

# code
# Python
# download
# content_copy
# expand_less
# extract_output = RunnableLambda(lambda x: x["output"])

# How this is "Parsing":

# The Agent produces a dictionary: {'input': '...', 'output': 'Elon is rich', ...}.

# The structured_llm expects a String, not a Dictionary.

# This line "parses" the dictionary by stripping away everything except the value inside "output".

# Summary: Where is the logic?

# If you want to visualize the flow of data transformation (parsing):

# Hidden ReAct Parser: Reads Action: keywords inside the agent to control the search loop.

# Manual Lambda: Extracts the text string from the agent's final result.

# Hidden Structured Parser: The .with_structured_output function forces the text into your AgentResponse Pydantic model.

# You have successfully automated the parsing without writing a parser class yourself! This is the modern "Best Practice."