from helper import get_response

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape. Birds were chirping happily, and a gentle breeze rustled the leaves of the trees. It was a perfect evening for a leisurely stroll in the park"

# Create the instructions
instructions = "infer the language and the number of sentences of the given delimited text in tripe backticks(```); then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title."

# Create the output format
output_format = """ use the follwoing format for the output: 
- Text: <Text we want to title>
- Language: <the language use in text>
- Title: the generated title for the text"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)