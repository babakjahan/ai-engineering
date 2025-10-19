from helper import get_response

# Create a prompt detailing steps to plan the trip
prompt = """make a plan for a beach vacation, which should include:
step 1 : four potential locations.
step 2 : each with some accommodation options,activities.
step 3 : pros & cons for each location."""

response = get_response(prompt)
print(response)