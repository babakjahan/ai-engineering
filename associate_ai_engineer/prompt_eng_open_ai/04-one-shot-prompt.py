from helper import get_response
# number of examples in the prompt
# no examples > zero shot
# one example > one shot
# multiple examples > few shot


# Create a one-shot prompt
one_shot_prompt = """ extract the odd numbers from the set {1, 3, 7, 12, 19} answer is : {1,3,7,19} . what is odd numbers in {3,5,11,12,16}"""

response = get_response(one_shot_prompt)
print(response)