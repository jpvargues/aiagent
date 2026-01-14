import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable not found. Please ensure it's set in your environment or .env file.")
client = genai.Client(api_key=api_key)

def main():
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",)
    print(response.text)


if __name__ == "__main__":
    main()
