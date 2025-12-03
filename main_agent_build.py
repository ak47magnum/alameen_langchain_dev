# from dotenv import load_dotenv
# from langchain.tools import tool
# from langchain_core.prompts import PromptTemplate
# from langchain_core.tools import render_text_description, Tool
# from langchain_openai import ChatOpenAI
# from langchain_classic.schema import AgentAction, AgentFinish
# from typing import Union
# from langchain_classic.agents.output_parsers import ReActSingleInputOutputParser
# from langchain_classic.agents.format_scratchpad.log import format_log_to_str
# import os
# load_dotenv()

# @tool
# def get_text_length(text):
#     """Returns the length of a text by counting the number of characters."""
#     print(f"get_text_length: {text}#####")
#     text= text.strip("'\n").strip('"')
#     return len(text)

# def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
#     for tool in tools:
#         if tool.name == tool_name:
#             return tool
#     raise ValueError(f"Tool {tool_name} not found")

# if __name__ == "__main__":
#     print("Hello Langchain! ###")

#     tools = [get_text_length]

#     template = """
#     Answer the following questions as best you can. You have access to the following tools:

#     {tools}

#     Use the following format:

#     Question: the input question you must answer
#     Thought: you should always think about what to do
#     Action: the action to take, should be one of [{tool_names}]
#     Action Input: the input to the action
#     Observation: the result of the action
#     ... (this Thought/Action/Action Input/Observation can repeat N times)
#     Thought: I now know the final answer
#     Final Answer: the final answer to the original input question

#     Begin!

#     Question: {input}
#     Thought: {agent_scratchpad}
#         """

#     prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools), \
#                                                                      tool_names=", ".join([t.name for t in tools]))

#     llm = ChatOpenAI(temperature=0).bind(stop=["\nObservation:","Observation"])
                                         
                                  
#     # llm = ChatOpenAI(temperature=0, model_kwargs={"stop": ["\nObservation","Observation"]}) # another way to stop the llm from generating more text with "stop".
    

#     intermediate_steps = []

#     agent = {"input": lambda x: x["input"], "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"])} | prompt | llm | ReActSingleInputOutputParser()

    
#     # res = agent.invoke({"input": "What is the length of  'Moriarty' in characters?"})
#     # print(res)
    
    
    
#     agent_step: Union[AgentAction, AgentFinish]  = agent.invoke({"input": "What is the length of the text 'Moriarty'", 
#                                                                  "agent_scratchpad": intermediate_steps})
#     # print(agent_step)
#     print(f"{agent_step}###########")
    
  
#     if isinstance(agent_step, AgentAction):
#         tool_name = agent_step.tool
#         # print(tool_name) ################# TESTING
#         tool_to_use = find_tool_by_name(tools, tool_name)
#         tool_input = agent_step.tool_input
#         observation = tool_to_use.func(str(tool_input))
#         # print(f"{observation=}")
#         intermediate_steps.append((agent_step, str(observation)))

#     agent_step: Union[AgentAction, AgentFinish]  = agent.invoke({"input": "What is the length of the text 'Moriarty'", 
#                                                                 "agent_scratchpad": intermediate_steps})
  
#     print(agent_step)
 






######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

#############  This version uses the "callback handlers" to see exactly what is happening. This is using the callbacks.py file to see what is happening.



from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description, Tool
from langchain_openai import ChatOpenAI
from langchain_classic.schema import AgentAction, AgentFinish
from typing import Union
from langchain_classic.agents.output_parsers import ReActSingleInputOutputParser
from langchain_classic.agents.format_scratchpad.log import format_log_to_str
from callbacks import AgentcallbackHandler
import os
from os.path import exists
load_dotenv()

@tool
def get_text_length(text):
    """Returns the length of a text by counting the number of characters."""
    print(f"get_text_length: {text}#####")
    text= text.strip("'\n").strip('"')
    return len(text)

def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool {tool_name} not found")

if __name__ == "__main__":
    print("Hello Langchain! ###")
    if exists("agent_output.txt"):
        os.remove("agent_output.txt")

    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought: {agent_scratchpad}
        """

    prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools), \
                                                                     tool_names=", ".join([t.name for t in tools]))

    llm = ChatOpenAI(temperature=0, callbacks=[AgentcallbackHandler()]).bind(stop=["\nObservation:","Observation"])
                                         
                                  
    # llm = ChatOpenAI(temperature=0, model_kwargs={"stop": ["\nObservation","Observation"]}) # another way to stop the llm from generating more text with "stop".
    

    intermediate_steps = []

    agent = {"input": lambda x: x["input"], "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"])} | prompt | llm | ReActSingleInputOutputParser()

    
    agent_step = ""
    
    
while not isinstance(agent_step, AgentFinish):    
        agent_step: Union[AgentAction, AgentFinish]  = agent.invoke({"input": "What is the length of the text 'Moriarty'", 
                                                                    "agent_scratchpad": intermediate_steps})
        # print(agent_step)
        # print(f"{agent_step}###########")
        
    
        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            # print(tool_name) ################# TESTING
            tool_to_use = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input
            observation = tool_to_use.func(str(tool_input))
            # print(f"{observation=}")
            intermediate_steps.append((agent_step, str(observation)))

        print(agent_step)

        if isinstance(agent_step, AgentFinish):
            print(agent_step.return_values)














######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################




#### Below is an example of the above task without above agent methods. This is just the llm guessing the answer using token prediction #####
#### Now we can see the power of the agent. The agent is able to use the tool to get the answer. The llm is just guessing.



# from dotenv import load_dotenv
# from langchain.tools import tool
# from langchain_core.prompts import PromptTemplate
# from langchain_core.tools import render_text_description, Tool
# from langchain_openai import ChatOpenAI
# from langchain_classic.schema import AgentAction, AgentFinish
# from typing import Union
# from langchain_classic.agents.output_parsers import ReActSingleInputOutputParser
# from langchain_classic.agents.format_scratchpad.log import format_log_to_str
# import os
# load_dotenv()

# @tool
# def get_text_length(text):
#     """Returns the length of a text by counting the number of characters."""
#     print(f"get_text_length: {text}")
#     text= text.strip("'\n").strip('"')
#     return len(text)

# def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
#     for tool in tools:
#         if tool.name == tool_name:
#             return tool
#     raise ValueError(f"Tool {tool_name} not found")

# if __name__ == "__main__":
#     print("Hello Langchain!")

#     tools = [get_text_length]

#     template = """
#     Answer the following questions as best you can. You have access to the following tools:

#     {tools}

#     Use the following format:

#     Question: the input question you must answer
#     Thought: you should always think about what to do
#     Action: the action to take, should be one of [{tool_names}]
#     Action Input: the input to the action
#     Observation: the result of the action
#     ... (this Thought/Action/Action Input/Observation can repeat N times)
#     Thought: I now know the final answer
#     Final Answer: the final answer to the original input question

#     Begin!

#     Question: {input}
#     Thought: {agent_scratchpad}
#         """

#     prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools), \
#                                                                      tool_names=", ".join([t.name for t in tools]))

#     llm = ChatOpenAI(temperature=0)
                                         
                                  
#     # llm = ChatOpenAI(temperature=0, model_kwargs={"stop": ["\nObservation","Observation"]}) # another way to stop the llm from generating more text with "stop".
    

#     intermediate_steps = []

#     agent = {"input": lambda x: x["input"], "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"])} | prompt | llm 

    
#     # res = agent.invoke({"input": "What is the length of  'Moriarty' in characters?"})
#     # print(res)
    
    
    
#     agent_step: Union[AgentAction, AgentFinish]  = agent.invoke({"input": "What is the length of the text 'Moriarty'", 
#                                                                  "agent_scratchpad": intermediate_steps})
#     print(agent_step)
    
  



    # if isinstance(agent_step, AgentAction):
    #     tool_name = agent_step.tool
    #     # print(tool_name) ################# TESTING
    #     tool_to_use = find_tool_by_name(tools, tool_name)
    #     tool_input = agent_step.tool_input
    #     observation = tool_to_use.func(str(tool_input))
    #     # print(f"{observation=}")
    #     intermediate_steps.append((agent_step, str(observation)))

    # agent_step: Union[AgentAction, AgentFinish]  = agent.invoke({"input": "What is the length of the text 'Moriarty'", 
    #                                                             "agent_scratchpad": intermediate_steps})
  
    # print(agent_step)
 