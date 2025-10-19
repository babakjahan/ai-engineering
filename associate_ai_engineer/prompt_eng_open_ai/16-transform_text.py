from helper import get_response
text = """
Hey guys, wanna know a cool trick? Here's how u can up your productivity game! First, download this awesome app, it's like the best thing ever! Then, just start using it and u'll see the difference. Its super easy and fun, trust me! So, what are u waiting for? Try it out now!
"""

# Craft a prompt to transform the text
prompt = f"""
improve the text quality by applying below steps :
step 1 : proofreads the text without changing its structure.
step 2 : adjusts its tone to be formal and friendly.
step 3:  just write the text and not extra info from youself

here is the text : ```{text}```

"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)