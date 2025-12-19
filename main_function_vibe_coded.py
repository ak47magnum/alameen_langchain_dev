from dotenv import load_dotenv
# from langchain.tools import tool # deprecated
from langchain_core.tools import tool
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from callbacks import AgentcallbackHandler
from langchain_core.messages import HumanMessage
from langchain_core.messages import ToolMessage
import os
from os.path import exists

load_dotenv()

@tool
def get_text_length(text):
    """Returns the length of a text by counting the number of characters."""
    print(f"get_text_length: {text}#####")
    text = text.strip("'\n").strip('"')
    return len(text)

def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool {tool_name} not found")

if __name__ == "__main__":
    print("Hello Langchain! ###")


    tools = [get_text_length]


    # llm = ChatOllama(model="gpt-oss:20b", temperature=0.0) ## Not very accurate
    llm = ChatOllama(model="llama3.1:8b", temperature=0.0)  ## Can have errors... but overall pretty good. I like this one for a local model!!!!!!!



    # llm = ChatOpenAI(model="gpt-5", temperature=0, callbacks=[AgentcallbackHandler()]) ## real slow and expensive  - (support tool calling)
    # llm = ChatOpenAI(model="gpt-4-turbo", temperature=0, callbacks=[AgentcallbackHandler()] ## Quicker but still expensive - (support tool calling)
    # llm = ChatOpenAI(model="gpt-4", temperature=0, callbacks=[AgentcallbackHandler()]) ## real slow and expensive  - (support tool calling)
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, callbacks=[AgentcallbackHandler()]) ## Quicker and cheaper - (support tool calling)
    # llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, callbacks=[AgentcallbackHandler()]) ## Also Quicker and cheaper - (support tool calling)
    # llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0, callbacks=[AgentcallbackHandler()]) ## Also Quicker and cheaper - (support tool calling). I like this one!!


    # Bind the tools to the LLM to enable automatic tool invocation
    llm_with_tools = llm.bind_tools(tools)

    messages = [HumanMessage(content="What is the length of the text 'Moriarty'")]

    # ai_message = llm_with_tools.invoke(messages) ## Delete this part. Its just a test
    # print(ai_message)  ## Delete this part. Its just a test
  

    while True:
        ai_message = llm_with_tools.invoke(messages)
        tool_calls =  getattr(ai_message, "tool_calls", None) or []
        if len(tool_calls) > 0 :
            messages.append(ai_message)
            for tool_call in tool_calls:
                tool_name = tool_call.get("name")
                tool_args = tool_call.get("args", {})
                tool_calls_id = tool_call.get("id")
                tool_to_use = find_tool_by_name(tools, tool_name)
                # print(type(tool_to_use)) ## TEST
                observation = tool_to_use.invoke(tool_args)
                print(f"{observation=}")
                messages.append(ToolMessage(content=str(observation), tool_call_id=tool_calls_id))
            continue
        print(ai_message.content)
        break

    # print(messages)  ### TEST


