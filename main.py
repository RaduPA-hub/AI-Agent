import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import json
import sys
from config import MAX_ITERATIONS

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("The API Key was not found")

client = OpenAI(
    base_url ="https://openrouter.ai/api/v1",
    api_key = api_key,
)
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

messages = [
    {"role": "system", "content":system_prompt},
    {"role": "user", "content": args.user_prompt},
]
final_message = ""
for _ in range(MAX_ITERATIONS):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature = 0,
        tools = available_functions,
    )
    message = response.choices[0].message
    messages.append(message)
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        final_message = message.content
        break
if final_message:
    print("Final response:")
    print(final_message)
else:
    print(f"Maximum iterations reached")
    sys.exit(1)
if response.usage is None:
    raise RuntimeError("failed API request, try again")
if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens} \n Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)