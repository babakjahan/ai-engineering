from helper import get_response

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape. Birds were chirping happily, and a gentle breeze rustled the leaves of the trees. It was a perfect evening for a leisurely stroll in the park"
# Create the instructions
instructions =  "determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters."

# Create the output format
output_format = """ use the follwoing format for the output: 
- Text: <Text we want to title>
- Language: <the language use in text>
- Title: the generated title for the text"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)