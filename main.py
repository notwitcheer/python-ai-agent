import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise Exception("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)


parser = argparse.ArgumentParser(description="Python AI Agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


response = client.models.generate_content(
    model='gemini-2.5-flash-image',
    contents=messages,
)

if response.usage_metadata is None:
    raise RuntimeError("API request failed: usage_metadata is None")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
