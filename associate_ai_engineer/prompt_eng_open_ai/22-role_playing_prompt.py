from helper import get_response

# Craft the system_prompt using the role-playing approach
system_prompt = "act as a learning advisor and the instruction to recommend beginner and advanced textbooks based on their background"

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)

