from helper import get_response


self_consistency_instruction = """Imagine three completely independent experts who reason differently are answering this question.
the final answer is obtained by majority vote.The question is:"""


problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"


prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)

print(response)
