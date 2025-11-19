# """
# Groq Model Switching Exercise - LangChain Integration

# Instructions:
# 1. This exercise simulates langchain-groq integration patterns
# 2. You'll implement functions to switch between Groq models
# 3. Complete the functions below to demonstrate proper model switching
# 4. Use valid model names from the Groq website (console.groq.com)

# Learning Objectives:
# - Learn LangChain-Groq integration patterns
# - Practice switching between different LLM models with full model names
# - Understand proper class instantiation and method calls
# - Master function composition and data structures

# Note: This uses mock objects to simulate the langchain-groq package behavior!
# Model names should match exactly what's available on console.groq.com
# """
# from dotenv import load_dotenv
# import os
# load_dotenv()

# # GROQ_KEY = os.getenv("GROQ_API_KEY")

# # Mock ChatGroq class to simulate the real langchain-groq behavior
# class ChatGroq():
#     """Mock ChatGroq class for educational purposes."""

#     def __init__(self, model, temperature=0, max_retries=2):
#         self.model = model
#         self.temperature = temperature
#         self.max_retries = max_retries
#         self.valid_models = [
#             "llama-4-8b-instant",
#             "llama-3.3-70b-versatile",
#             "llama-3.1-8b-instant"
#         ]

#         if model not in self.valid_models:
#             raise ValueError(f"Invalid model: {model}")

#     def invoke(self, messages):
#         """Mock invoke method that returns a simulated response."""
#         if not isinstance(messages, list) or len(messages) == 0:
#             raise ValueError("Messages must be a non-empty list")

#         # Simulate different responses based on model and temperature
#         if self.model == "llama-4-8b-instant":
#             content = f"[Llama 4 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
#         elif self.model == "llama-3.3-70b-versatile":
#             if self.temperature > 0.2:
#                 content = f"[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
#             else:
#                 content = f"[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
#         else:
#             content = f"[Mock Response] This is a simulated response from {self.model}"

#         return MockAIMessage(content)

# class MockAIMessage:
#     """Mock AI message response."""
#     def __init__(self, content):
#         self.content = content


# def implement_set_api_key(api_key):
#     """
#     IMPLEMENT: Set the GROQ_API_KEY environment variable.

#     Args:
#         api_key (str): Your Groq API key
#     """
#     # TODO: Your implementation here
#     os.environ["GROQ_API_KEY"] = api_key
#     print(f'{os.environ["GROQ_API_KEY"]}\n')
#     # pass


# def check_api_key():
#     """
#     Check if GROQ_API_KEY is set in environment variables.
#     Raise an exception if the API key is not set.
#     (This function is provided for you)
#     """
#     if "GROQ_API_KEY" not in os.environ:
#         raise Exception("GROQ_API_KEY environment variable is required")


# def implement_llama_4_model():
#     """
#     IMPLEMENT: Create and return a ChatGroq instance for Llama 4.
#     Use the exact model name from console.groq.com
#     Set temperature=0 for consistent responses
#     """
#     # TODO: Your implementation here
#     llm =  ChatGroq("llama-4-8b-instant", temperature=0)
#     return llm
#     # pass


# def implement_llama_3_3_model():
#     """
#     IMPLEMENT: Create and return a ChatGroq instance for Llama 3.3.
#     Use the exact model name from console.groq.com
#     Set for slightly more creative responses
#     """
#     # TODO: Your implementation here
#     llm =  ChatGroq("llama-3.3-70b-versatile", temperature=0.5)
#     return llm
#     # pass


# def implement_query_model(model, prompt):
#     """
#     IMPLEMENT: Send a query to the model and return the response content.

#     Args:
#         model: The ChatGroq model instance
#         prompt: The text prompt to send

#     Returns:
#         str: The response content
#     """
#     # TODO: Your implementation here
#     messages = [prompt]
#     response = model.invoke(messages)
#     return response.content

#     # pass


# def implement_compare_models(prompt):
#     """
#     IMPLEMENT: Query both models and return a dictionary with both responses.

#     Args:
#         prompt: The text prompt to send to both models

#     Returns:
#         dict: Dictionary with responses from both models
#     """
#     # TODO: Your implementation here
#     message1 = [prompt]
#     response1 = implement_llama_4_model().invoke(message1)
#     message2 = [prompt]
#     response2 = implement_llama_3_3_model().invoke(message2)
#     return {"llama-4-8b-instant": response1.content, "llama-3.3-70b-versatile": response2.content}

#     # pass


# def main():
#     """
#     Main function to test your implementations.
#     """
#     print("🚀 Groq Model Switching Exercise (LangChain Integration)")
#     print("=" * 55)
#     print("📝 This exercise simulates langchain-groq package behavior!")
#     print("🌐 Model names should match console.groq.com exactly")
#     print()

#     try:
#         # Test your set_api_key implementation
#         print("🔑 Setting API key...")
#         implement_set_api_key("izaHj6rwWGdyb3FYGydjWyUCqR57ec")

#         # Check if API key was set correctly
#         check_api_key()
#         print("✓ API key validation working!")

#         # Test prompt
#         test_prompt = "Explain the concept of machine learning in one sentence."

#         # Test your model implementations
#         print(f"\n🤖 Testing your Llama 4 implementation:")
#         llama4 = implement_llama_4_model()
#         response4 = implement_query_model(llama4, test_prompt)
#         print(f"Llama 4: {response4}\n")

#         print(f"🤖 Testing your Llama 3.3 implementation:")
#         llama33 = implement_llama_3_3_model()
#         response33 = implement_query_model(llama33, test_prompt)
#         print(f"Llama 3.3: {response33}\n")

#         # Test your comparison implementation
#         print("🔄 Testing your model comparison:")
#         comparison = implement_compare_models(test_prompt)
#         print("Comparison results:")
#         for model, response in comparison.items():
#             print(f"  {model}: {response}")

#         print("\n🎉 All implementations working!")
#         print("✅ Great job implementing the LangChain-Groq patterns!")

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         if "GROQ_API_KEY" in str(e):
#             print("\n💡 Check your implement_set_api_key() function!")
#         else:
#             print("📝 Check your function implementations!")
#             print("🌐 Verify model names match console.groq.com exactly")


# if __name__ == "__main__":
#     main()


############################################## practise exercises for python #########################################


# from dotenv import load_dotenv
# import os
# load_dotenv()


# keys = os.environ["GROQ_API_KEY"] = "izaHj6rwWGdyb3FYGydjWyUCqR57ec"
# print(keys)

# cpu = os.cpu_count()
# print(cpu)
# print(os.curdir)
# print(os.listdir())
# print(os.getlogin())


############################################## practise exercises for python #########################################


# words: list[str] = ["hello", "world", "this", "is", "a", "list", "of", "words"]

# for index, word in enumerate(words):
#     print(f"Word {index} is {word}")

# for word in enumerate(words):
#     print(word)


# for word in enumerate(words):
#     print(word)


# for word in words:
#     if len(word)> 2:
#         print(word)

# for word in words:
#     print(words.index(word), word)

# new_dict = {word: len(word) for word in words if len(word)}
# print(new_dict)

############################################## practise exercises for python #########################################


# from pathlib import Path

# p = Path("D:\PODCAST")
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
# print(p.name)
# print(p.parent)
# print(p.stem)
# print(p.suffix)
# print(p.resolve())

# for x in p.iterdir():
#     print(x.name)

# for y in p.glob("*.jpg"):
#     print(y.name)
#     # print(y.with_suffix(".jpg"))
#     y.rename(y.with_suffix(".jpeg"))


############################################## practise exercises for python #########################################


# def list_words(words: list[str]) -> None:
#     for i, word in enumerate(words):
#         print(i, word)

# words: list[str] = ["hello", "world", "this", "is", "a", "list", "of", "words"]
# # list_words(words)


# copy_list_words = list_words  ## a function can be assigned to a variable for refferal jus like any other object in python
# # copy_list_words(words)

############################################## practise exercises for python #########################################

# words: list[str] = ["hello", "world", "this", "is", "a", "list", "of", "words"]
# class ListWords:
#     def __call__(self, words: list[str]) -> None:  ### This is a dunder function in python where the object can be called like a function
#         for i, word in enumerate(words):
#             print(i, word)

# list_words = ListWords()   ### This is a dunder function being called
# list_words(words)


############################################## practise exercises for python #########################################

# words: list[str] = ["hello", "world", "this", "is", "a", "list", "of", "words"]


# class ListWords:
#     def transform(self, words: list[str]) -> None:

#         return {i: word for i, word in enumerate(words)}

# class DoubleWords:
#     def transform(self, words: list[str]) -> list[str]:
#         for i, word in enumerate(words):
#             # print(i, word)
#             return [word * 2 for word in words]


# def transform(transform: ListWords, words: list[str]) -> None:
#     new_words = transform.transform(words)
#     print(new_words)


# word_changer = ListWords()
# transform(word_changer, words)

# word_doubler = DoubleWords()
# transform(word_doubler, words)


####### Summary for above code.#######
# """Yes — the parameter:

# def transform(transform: ListWords, words: list[str]) -> None:


# does NOT need to be a ListWords object.

# It can be any class, as long as it has a method called:

# transform(self, words)


# That’s the only requirement.

# So this works:

# ListWords class ✔️ (has transform)

# DoubleWords class ✔️ (has transform)

# Any new class you create ✔️ (as long as it defines transform)

# This pattern is a classic design approach.

# """


############################################## practise exercises for python #########################################


# from datetime import datetime, timedelta

# # current_date = datetime.now()
# # print(current_date)
# # print(current_date.year)
# # print(current_date.month)
# # print(current_date.day)
# # print(current_date.hour)
# # print(current_date.minute)
# # print(current_date.second)
# # print(current_date.microsecond)
# #
# print(timedelta(seconds=600))
# print(datetime.now().year)


#####################################

import json
r ={
  "input": "find three listings for a 2 bedroom flat in the wuse area of abuja  ",
  "output": "{\"answer\": \"1. A 2 bedroom flat in Wuse2 District Abuja listed on propertypro.ng for ₦ 7,000,000/year. [source](https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom) 2. A 2 bedroom flat in Wuse Zone 6 Wuse Abuja Phase 1 listed on privateproperty.ng for ₦1400000. [source](https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203) 3. A 2 bedroom flat in Wuse 2, Abuja listed on nigeriapropertycentre.com, price not mentioned. [source](https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype)\", \"sources\": [{\"source_url\": \"https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom\"}, {\"source_url\": \"https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203\"}, {\"source_url\": \"https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype\"}]}"
}


s = json.loads(r["output"]) 

# print(len(s["sources"]))

for i, j in enumerate(s["sources"]):
    print(i, j["source_url"])