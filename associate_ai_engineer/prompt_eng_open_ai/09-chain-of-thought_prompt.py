from helper import get_response

# Create the chain-of-thought prompt
prompt = "determine your friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20. think step by step"

response = get_response(prompt)
print(response)