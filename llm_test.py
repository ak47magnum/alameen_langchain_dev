# from dotenv import load_dotenv
# from langchain.tools import tool
# from langchain_core.prompts import PromptTemplate
# from langchain_core.tools import render_text_description 
# from langchain_openai import ChatOpenAI
# import requests

# load_dotenv()






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


############################################## practise exercises for python #########################################

# import json
# r ={
#   "input": "find three listings for a 2 bedroom flat in the wuse area of abuja  ",
#   "output": "{\"answer\": \"1. A 2 bedroom flat in Wuse2 District Abuja listed on propertypro.ng for ₦ 7,000,000/year. [source](https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom) 2. A 2 bedroom flat in Wuse Zone 6 Wuse Abuja Phase 1 listed on privateproperty.ng for ₦1400000. [source](https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203) 3. A 2 bedroom flat in Wuse 2, Abuja listed on nigeriapropertycentre.com, price not mentioned. [source](https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype)\", \"sources\": [{\"source_url\": \"https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom\"}, {\"source_url\": \"https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203\"}, {\"source_url\": \"https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype\"}]}"
# }


# s = json.loads(r["output"]) 

# # print(len(s["sources"]))

# for i, j in enumerate(s["sources"]):
#     print(i, j["source_url"])


############################################## practise exercises for python #########################################

# from dotenv import load_dotenv
# load_dotenv()

# from openai import OpenAI
# from pydantic import BaseModel

# client = OpenAI()

# class Step(BaseModel):
#     explanation: str
#     output: str

# class MathReasoning(BaseModel):
#     steps: list[Step]
#     final_answer: str

# response = client.responses.parse(
#     model="gpt-4o-2024-08-06",
#     input=[
#         {
#             "role": "system",
#             "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
#         },
#         {"role": "user", "content": "how can I solve 8x + 7 = -23"},
#     ],
#     text_format=MathReasoning,
# )

# math_reasoning = response.output_parsed
# print(math_reasoning)






############################################## practise exercises for python #########################################

# # from typing import Optional


# def get_email(first_name: str, last_name: str, age: int|None = None):
#     mail = f"{first_name}.{last_name}@yahoo.com"
#     return f"Your email is {mail} and your age is {age}"



# mm = get_email(first_name="mom", last_name="manu", age=32)

# print(mm)


####################################################



# def fizx_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         return "fizzbuzz"
#     if  input % 3 == 0:
#         return "fizz"
#     if input % 5 == 0:
#         return "buzz"
  


# # my_input = input("Enter a number: ")
# print(fizx_buzz(15))


###############################################################

# import json

# x = {
#   "input": "find three listings for a 2 bedroom flat in the wuse area of abuja  ",
#   "output": "{\"answer\": \"1. A 2 bedroom flat in Wuse2 District Abuja listed on propertypro.ng for ₦ 7,000,000/year. [source](https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom) 2. A 2 bedroom flat in Wuse Zone 6 Wuse Abuja Phase 1 listed on privateproperty.ng for ₦1400000. [source](https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203) 3. A 2 bedroom flat in Wuse 2, Abuja listed on nigeriapropertycentre.com, price not mentioned. [source](https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype)\", \"sources\": [{\"source_url\": \"https://propertypro.ng/property-for-rent/flat-apartment/in/abuja/wuse-2/2-bedroom\"}, {\"source_url\": \"https://privateproperty.ng/listings/2-bedroom-flat-apartment-for-rent-wuse-zone-6-wuse-abuja-phase-1-MY18203\"}, {\"source_url\": \"https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/wuse-2/showtype\"}]}"
# }

# y = json.loads(x["output"])
# print(y["sources"])

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################


#### THIS SECTION IS FOR KACE API TO CREATE TICKETS ##############################################

# import requests
# import json
# import warnings  # Import warnings module to suppress InsecureRequestWarning
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Suppress only the InsecureRequestWarning from urllib3 needed for verify=False
# # Use the standard urllib3 import path
# from urllib3.exceptions import InsecureRequestWarning
# warnings.simplefilter('ignore', InsecureRequestWarning)


# # Define your KACE SMA appliance URL
# HOST = "support.julius-berger.com"  # e.g., "k1000.yourcompany.com"
# # Define the API base URL for Service Desk
# BASE_URL = f"http://{HOST}/api/service_desk"
# # Define the AMS base URL for login
# AMS_BASE_URL = f"http://{HOST}/ams/shared/api/security"

# # Admin credentials
# USERNAME = os.getenv("KACE_USER_NAME")
# PASSWORD = os.getenv("KACE_PASSWORD")




# CUSTOM_7_CONSULTANTS = ["Unassigned", "Jayalakshmi Nagarajan - jayalakshmi.n@aakit.com  - AMS Manager", "Prachiti Kothare - prachiti.kothare@aakit.com - Dispatcher", 
#                         "Atul Arsekar - atul.arsekar@aakit.com - MM Consultant", "Rahul Khamkar	-  rahul.khamkar@aakit.com - MM Consultant", 
#                         "Wasimuddin Sayed - wasimuddin.sayed@aakit.com - MM/TM Consultant", "Divesh Mistry  - divesh.mistry@aakit.com - FI Consultant", 
#                         "Akshay Zirmirkar - akshay.zirmirkar@aakit.com - FI Consultant", "Amey Mule - amey.mule@aakit.com - FI Consultant", 
#                         "Suhas Patil - suhas.patil@aakit.com - EWM Consultant", "Pratap Jagadam - pratap.jagadam@aakit.com - EWM Consultant", 
#                         "Tarka Karwadkar - tarka.karwadkar@aakit.com - Technical Lead", "Ashish Patil - ashish.patil@aakit.com	- Technical Lead", 
#                         "Shardul Tendulkar - shardul.tendulkar@aakit.com	- Technical Lead", "Sitesh Sawant - sitesh.sawant@aakit.com	- Technical Consultant", 
#                         "Asmitha Pamuru - asmitha.pamuru@aakit.com - Technical Consultant", "Niket Patil - niket.patil@aakit.com - BASIS Consultant"
# ]


# CUSTOM_6_MODULES = ["Unassigned", "SAP-ABAP", "SAP-AUTHORIZATION", "SAP-BASIS", "SAP-EWM, SAP-FI", "SAP-GENERAL", "SAP-MM", "SAP-SD, JOE", "SAM", "TACA",""
#                     " Clubhouse Software", "Travel DB", "Palette CAD", "Lucanet", "Kuhnle", "Precast", "Iron Bending", "IDcard Asure", "Paula", "Julian", 
#                     "WMS", "Sharepoint"]

# CUSTOM_5_DEPARTMENT = ["Finance", "NSG", "PED", "PLS", "PMO", "TM", "ZAMS/HYPERCARE/IT/PMO"]

# # Ensure this is a list of dictionaries, mapping name to ID
# TICKET_OWNER = [{"Kabir, Amin": "11411"}, {"Eguwe, Ewomazino": "12265"}]


# def login(host, username, password):
#     """Authenticates with the KACE SMA and returns the session cookies."""

#     # Corrected URL construction: Append only '/login' to the base host URL
#     url = f"{host}/login"
#     headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'x-kace-api-version': '8'}
#     payload = {
#         "userName": username,
#         "password": password
#     }

#     # Added verify=False to bypass SSL certificate verification.
#     # WARNING: This disables security checks. Only use if you trust the server
#     # or understand the security implications.
#     response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
#     response.raise_for_status()


#     # # --- DEBUGGING: Print login response details to find CSRF token ---
#     # print("\n--- Login Response ---")
#     # print(f"Status Code: {response.status_code}")
#     # print("Headers:")
#     # # Use dict() to convert CaseInsensitiveDict for JSON serialization
#     # print(json.dumps(dict(response.headers), indent=2))
#     # print("Cookies:")
#     # # Use requests.utils helper function
#     # print(json.dumps(requests.utils.dict_from_cookiejar(response.cookies), indent=2))
#     # try:
#     #     print("Body (JSON):")
#     #     print(json.dumps(response.json(), indent=2))
#     # except json.JSONDecodeError:
#     #     print("Body (Text):")
#     #     print(response.text)
#     # print("--- End Login Response ---\n")
#     # # --- End Debugging ---

#     # We will extract the actual token later based on the debug output
#     # For now, just return the cookies
#     return response.cookies


# def get_tickets_in_queue(base_url, cookies, queue_id):
#     """Retrieves a list of tickets in a specific queue."""

#     # Base endpoint URL
#     url = f"{base_url}/tickets"
#     # Parameters dictionary - requests will handle URL encoding
#     params = {
#         'filtering': f'hd_queue_id eq {queue_id}'
#     }

#     print(f"Attempting to fetch tickets from URL: {url} with params: {params}")  # Updated print

#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'x-kace-api-version': '5'   # Check if this header is still required/correct for your KACE version
#         # We will add the CSRF token header here later
#     }

#     # Added verify=False to bypass SSL certificate verification.
#     # WARNING: This disables security checks. Only use if you trust the server
#     # or understand the security implications.
#     # Pass params dictionary to requests.get
#     try:
#         response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
#         response.raise_for_status()
#         print(response.url)
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#         print(f"Status Code: {e.response.status_code if e.response else 'N/A'}")
#         print("Response Headers:")
#         print(json.dumps(dict(e.response.headers) if e.response else {}, indent=2))
#         try:
#             print("Response Body:")
#             print(e.response.text if e.response else 'N/A')
#         except:
#             print("Could not decode response body.")
#         raise  # Re-raise the exception to propagate it
#     except requests.exceptions.RequestException as e:
#         print(f"Request Error: {e}")
#         raise
   

# def get_ticket_template(base_url, cookies, queue_id):
#     """Fetch the ticket template for a specific Service Desk queue."""
#     url = f"{base_url}/queues/{queue_id}/ticket_template"

#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'x-kace-api-version': '5'
#     }

#     try:
#         print(f"Fetching ticket template from: {url}")
#         response = requests.get(url, headers=headers, cookies=cookies, verify=False)
#         response.raise_for_status()
#         print("Ticket template fetched successfully.")
#         return response.json()

#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#         if e.response:
#             print("Status code:", e.response.status_code)
#             print("Response:", e.response.text)
#         raise
#     except requests.exceptions.RequestException as e:
#         print(f"Request Error: {e}")
#         raise



# def get_queue_fields(base_url, cookies, queue_id):
#     url = f"{base_url}/tickets"
#     # Parameters dictionary - requests will handle URL encoding

#     print(f"Attempting to fetch tickets from URL: {url} with queue_ID: {queue_id}")  # Updated print

#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'x-kace-api-version': '5' # Check if this header is still required/correct for your KACE version
#         # We will add the CSRF token header here later
#     }

#     response = requests.get(url=url, headers=headers, cookies=cookies)
#     response.raise_for_status()
#     return response


# def create_incident(base_url, cookies, queue_id):
#     url = f"{base_url}/tickets"
#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'x-kace-api-version': '5'  # Check if this header is still required/correct for your KACE version
#         # We will add the CSRF token header here later
#     }


#     ticket_data = {
#         "Tickets": [
#             {
#                 "hd_queue_id": queue_id,
#                 "summary": "Trouble shooting level 1",
#                 "title": "Trouble shooting level 2",
#                 "submitter": { "id": 10 },
#                 "priority": { "id": 117 },
#                 "owner" : {"id": 11411 },
#                 "status": { "id": 242 }
#             }
#         ]
#     }

#     # payload = json.dumps(ticket_data)
#     # print(type(payload))
#     # response = requests.post(url=url, headers=headers, data=payload, cookies=cookies)
#     # response.raise_for_status()

#     payload = json.dumps(ticket_data)
#     print("Submitting:", payload)

#     # print("Ticket creation response:")
#     # print(json.dumps(response.json(), indent=2))

#     try:
#         response = requests.post(url=url, headers=headers, data=payload, cookies=cookies, verify=False)
#         response.raise_for_status()
#         print("Ticket created successfully.")
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         print("HTTP Error:", e)
#         print("Status Code:", e.response.status_code)
#         print("Response Text:", e.response.text)
#         raise

# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# ## >👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# def main():
#     """Main function to log in and get tickets in a queue."""

#     try:
#         session_cookies = login(AMS_BASE_URL, USERNAME, PASSWORD)  ####################### FUNCTION WORKS !!!!!
#         print("Logged in successfully.\n")

#         target_queue_id = "36"  # Replace with the actual queue ID you want to query  eg, (27: it_requisition) or (36: it_requisition_test)

#         tickets = get_tickets_in_queue(BASE_URL, session_cookies, target_queue_id)    ###################### FUNCTION WORKS !!!!!
#         # print(tickets["Tickets"])
#         # print(f"Number of tickets in QUEUE: =  {len(tickets)} \n\n")
#         print(f"Number of tickets in QUEUE: =  {len(tickets['Tickets'])}\n")
#         for ticket in tickets["Tickets"]:
#             print(ticket, "\n") #adjust keys as needed

#         # print(f"Tickets in Queue {target_queue_id}:")
#         # for ticket in tickets:
#         #     print(f"  - Ticket ID: {ticket['ID']}, Title: {ticket['Title']}") #adjust keys as needed
#         #     # print(ticket) #adjust keys as needed

#         fields = get_queue_fields(BASE_URL, cookies=session_cookies, queue_id=target_queue_id)  ################ FUNCTION WORKS !!!!!
#         field_data = json.dumps(fields.text)
#         # print(fields.text)
#         # print(field_data["Fields"])
#         # for item in field_data:
#         #     print(item["jsonKey"])
#         # print(type(field_data))

#         create_ticket = create_incident(BASE_URL, cookies=session_cookies, queue_id=target_queue_id) ### FUNCTION NOT WORKING ********** !!!!!
#         print("Ticket  created!!!!!")




#         # template =  get_ticket_template(BASE_URL, cookies=session_cookies, queue_id=target_queue_id)
#         # print(template)

#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#         print(f"Response content: {e.response.text if e.response else 'No response'}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         import traceback
#         traceback.print_exc()  # Print the full traceback for other exceptions


# if __name__ == "__main__":
#     main()



###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

# from dotenv import load_dotenv
# from langchain.tools import tool
# from langchain_core.prompts import PromptTemplate
# from langchain_core.tools import render_text_description 
# from langchain_openai import ChatOpenAI
# # from langchain_anthropic import ChatAnthropic


# load_dotenv()


# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import ConfigurableField
# from langchain_core.tools import tool
# from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
# from langchain_tavily import TavilySearch  ## This is the latest langchain search tool for using tavily





# @tool
# def multiply(x: float, y: float) -> float:
#     """Multiply 'x' times 'y'."""
#     return x * y

# @tool
# def exponentiate(x: float, y: float) -> float:
#     """Raise 'x' to the 'y'."""
#     return x**y

# @tool
# def add(x: float, y: float) -> float:
#     """Add 'x' and 'y'."""
#     return x + y

# @tool
# def subtract(x: float, y: float) -> float:
#     """Subtract 'y' from 'x'."""
#     return x - y




# prompt = ChatPromptTemplate.from_messages([
#     ("system", "you're a helpful assistant"), 
#     ("human", "{input}"), 
#     ("placeholder", "{agent_scratchpad}"),
# ])

# tools = [multiply, exponentiate, add, subtract, TavilySearch(tavily_api_key="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")]


# # llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)  ############ I need credits to use anthropic API *****************

# # llm = ChatOpenAI(model="gpt-5", temperature=0) ## real slow and expensive  - (support tool calling)
# # llm = ChatOpenAI(model="gpt-4-turbo", temperature=0) ## Quicker but still expensive - (support tool calling)
# # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) ## Quicker and cheaper - (support tool calling)
# # llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0) ## Also Quicker and cheaper - (support tool calling)
# llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0) ## Also Quicker and cheaper - (support tool calling). I like this one!!


# agent = create_tool_calling_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# # agent_executor.invoke({"input": "what's 3 plus 5 raised to the 2.743. also what's 17.24 - 918.1241", }) ## uses calculation tools
# # agent_executor.invoke({"input": "get me a list of three 2 bedroom apartments for sale on queensway in london", }) ## Uses TavilySearch() tool
# res = agent_executor.invoke({"input": "What is the weather like in london uk and in minsk \
#                        belarus today? And what is the difference between the two in celsius?", }) ## Uses TavilySearch() tool

# # print(res)



#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################



