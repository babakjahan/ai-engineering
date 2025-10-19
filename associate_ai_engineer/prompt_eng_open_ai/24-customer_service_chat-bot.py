from helper import get_response


# the prompt includes context information about the service
system_prompt = """
a customer service chatbot for a delivery service that responds in a gentle way and point to a service description,
some information about our company are delimited by triple backticks
```{service_description}```
"""



user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt,user_prompt)

print(response)