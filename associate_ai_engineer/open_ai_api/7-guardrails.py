from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# One of the most popular uses of system messages is to add guardrails, which places restrictions on model outputs.
# In this exercise, you'll place a restriction on model outputs preventing 
# learning plans not related to languages, as your system is beginning to find its niche in that space.
# You'll design a custom message for users requesting these type of learning plans so they understand this change.


# Define the system message with guardrails
sys_msg = """You are a study planning assistant that creates plans for learning new languages.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to rollerskating."}
  ]
)

print(response.choices[0].message.content)