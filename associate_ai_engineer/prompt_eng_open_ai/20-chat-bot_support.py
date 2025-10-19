from helper import get_response

# Define the purpose of the chatbot
chatbot_purpose = "you are a chat bot for an e-commerce company specializing in electronics your role is handles customer support, specializes in electronics, and is there to assist with inquiries, order tracking, and troubleshooting"

# Define audience guidelines
audience_guidelines = "your target audience are tech-savvy individuals interested in purchasing electronic gadgets"

# Define tone guidelines
tone_guidelines = "use a professional and user-friendly tone while interacting with customers"

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)