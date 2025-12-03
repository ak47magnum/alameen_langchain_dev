
from typing import Any
from uuid import UUID
from langchain_core.outputs import LLMResult
from langchain_classic.callbacks.base import BaseCallbackHandler
# from langchain_core.callbacks.base import BaseCallbackHandler


### Override the BaseCallbackHandler class to see what is happening in the agent.
class AgentcallbackHandler(BaseCallbackHandler):
    def on_llm_start(self,
        serialized: dict[str, Any],
        prompts: list[str],
        **kwargs: Any,
    ) -> Any:
        """Run when LLL starts running."""
        print(f"***Prompt to LLM was :***\n{prompts[0]}")
        print("*********")

        ## My little addition to print to a txt file
        with open("agent_output.txt", "a") as f:
            f.write(f"***Prompt to LLM was :***\n{prompts[0]}\n")
        
    def on_llm_end(self,
        response: LLMResult,
        **kwargs: Any,
    ) -> Any:
        """Run when LLM ends running."""
        print(f"***Response fromLLM was :***\n{response.generations[0]}")
        print("*********")

        ## My little addition to print to a txt file
        with open("agent_output.txt", "a") as f:
            f.write(f"***Response fromLLM was :***\n{response.generations[0]}\n")

    
    