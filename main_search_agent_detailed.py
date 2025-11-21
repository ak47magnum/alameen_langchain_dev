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

#### User:


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




### Model:


# This is a great question. Understanding how to control the "shape" of the data coming out of an LLM is the most critical step in moving from a fun demo to a real production application.

# Here is a breakdown of how this specific code works, followed by the answers to your specific questions about fields and formats, and finally, a "Standard Formula" you can use for future projects.

# 1. The High-Level Concept: Two Steps

# In this specific script, the pipeline is actually performing two distinct operations to get your data:

# The Researcher (Agent): It uses the "Raw" LLM + Tools (Tavily) to find information. It produces a block of text (a string).

# The Formatter (Structured LLM): It takes that block of text and passes it through the LLM again, forcing it to organize that text into your specific JSON format (Pydantic).

# 2. Explaining the Code Block by Block
# A. Defining the "Shape" (The Contract)
# code
# Python
# download
# content_copy
# expand_less
# class Source(BaseModel):
#     source_url: str = Field(description="The url of the source")

# class AgentResponse(BaseModel):
#     answer: str = Field(description="The answer to the query")
#     sources: List[Source] = Field(...)

# What is this? This is Pydantic. It is a data validation library.
# Why do we need it? LLMs speak English (or text). Apps speak Objects/JSON. Pydantic bridges this gap. You are defining a "contract" that says: "I don't care how the LLM thinks, but the final result MUST have a field called answer which is a string, and sources which is a list."

# B. The Structured LLM
# code
# Python
# download
# content_copy
# expand_less
# structured_llm = llm.with_structured_output(AgentResponse)

# The Magic: This is where the parser connects to the LLM.
# In the "Old Days" (6 months ago), we had to write prompts like "Please output your answer in JSON format." and then use a parser to fix the messy text the LLM returned.
# The New Way (This Code): .with_structured_output() uses a feature called Tool Calling (or Function Calling). It sends your Pydantic schema to OpenAI alongside the prompt. OpenAI is trained to return a perfect JSON object matching that schema, bypassing the need for messy string parsing.

# C. The Chain (The Pipeline)
# code
# Python
# download
# content_copy
# expand_less
# extract_output = RunnableLambda(lambda x: x["output"])
# chain = agent_executor | extract_output | structured_llm

# This pipe (|) operator is the LangChain Expression Language (LCEL). It flows left to right:

# agent_executor:

# Input: {"input": "who is elon musk?"}

# Action: It searches Tavily, thinks, acts, and generates a final text response.

# Result: It outputs a dictionary standard to LangChain agents:

# code
# JSON
# download
# content_copy
# expand_less
# {
#     "input": "who is elon musk?",
#     "output": "Elon Musk is a tech billionaire..."
# }

# extract_output:

# This simple function grabs only the value of "output" from the dictionary above.

# Result: "Elon Musk is a tech billionaire..." (Just a string).

# structured_llm:

# It takes that string.

# It looks at your AgentResponse schema.

# It "rewrites" or "maps" the string into that JSON structure.

# Final Result: An AgentResponse object (which looks like JSON).

# 3. Addressing Your Questions
# "How does the structuring of the output work? Is it text, JSON, or what?"

# Raw LLM Output: Always Text (String).

# Structured Output: The .with_structured_output() method instructs the LLM to generate a JSON string internally, which LangChain immediately converts into a Python Object (specifically, an instance of your Pydantic class).

# For your App: You can convert that Pydantic object to standard JSON easily using .dict() or .json().

# "I have seen fields like 'answer', 'output', 'tools'. Are these standard?"

# There are two types of fields happening here, and it's important not to confuse them:

# LangChain Standard Fields (Internal):

# input: What goes into a chain.

# output: The default key for the result of an Agent or Chain.

# intermediate_steps: Used by agents to show their work.

# You generally cannot change these names when using pre-built agents like AgentExecutor.

# User-Defined Fields (Your Data):

# answer: Not standard. This exists only because you wrote answer: str in your AgentResponse class.

# sources: Not standard. Exists because you defined it.

# You can name these whatever you want. If you changed your class to class Pizza(BaseModel): topping: str, your output field would be topping.

# "How are parsers connected to the LLM?"

# In modern LangChain (as seen in your code), the connection happens via .with_structured_output().

# LangChain converts your Pydantic class into a JSON Schema.

# It sends that Schema to the API (e.g., OpenAI) as a "Tool".

# It forces the LLM to "call the tool" with the answer, ensuring the format is correct.

# 4. The "Standard Formula" for Parsing LLM Output

# If you want to build a real-world app where you need specific data formats to pass down a pipeline (e.g., to a frontend or database), use this formula.

# Step 1: Define the Goal (Pydantic)
# Always start by defining what you want the data to look like.

# code
# Python
# download
# content_copy
# expand_less
# from pydantic import BaseModel, Field
# from typing import List

# # The exact structure you want your API/Frontend to receive
# class FinalReport(BaseModel):
#     summary: str = Field(description="A 2-sentence summary")
#     sentiment: str = Field(description="The sentiment: POSITIVE, NEGATIVE, or NEUTRAL")
#     key_points: List[str] = Field(description="List of 3 bullet points")

# Step 2: Setup the Structured LLM
# Bind the model to the LLM.

# code
# Python
# download
# content_copy
# expand_less
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4o", temperature=0)
# # This forces the LLM to ONLY speak in "FinalReport" format
# structured_llm = llm.with_structured_output(FinalReport)

# Step 3: Create the Prompt
# Tell the LLM what to do to generate the content.

# code
# Python
# download
# content_copy
# expand_less
# from langchain_core.prompts import ChatPromptTemplate

# system_msg = "You are a helpful data analyzer. Analyze the user text and extract the required fields."
# prompt = ChatPromptTemplate.from_messages([
#     ("system", system_msg),
#     ("human", "{user_text}"),
# ])

# Step 4: The Chain
# Connect them.

# code
# Python
# download
# content_copy
# expand_less
# chain = prompt | structured_llm

# Step 5: Execution
# Run it. The result response will be a Python object, not a string.

# code
# Python
# download
# content_copy
# expand_less
# raw_text = "I absolutely loved the new phone! The camera is great, but the battery sucks. Overall good."

# response = chain.invoke({"user_text": raw_text})

# # Access data cleanly using dot notation
# print(response.sentiment)   # Output: POSITIVE (or MIXED depending on LLM)
# print(response.key_points)  # Output: ['Camera is great', 'Battery sucks', ...]

# # Need JSON for your API?
# print(response.json())
# Summary of your specific code snippet

# Your code is unique because it combines an Agent (which is chaotic and searches the web) with a Structured Output (which cleans up the mess).

# User types query.

# AgentExecutor runs around the internet (Tavily) and writes a text paragraph.

# extract_output isolates that paragraph.

# structured_llm reads the paragraph and fits it into AgentResponse(answer=..., sources=...).

# A Warning on your specific code:
# Because the structured_llm is only looking at the final text output of the agent (and not the raw search results), it might struggle to populate the sources list accurately unless the Agent explicitly wrote the URLs in its final text answer.

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