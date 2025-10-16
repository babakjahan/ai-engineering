
from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": assistant,
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].____.____)