from helper import get_response


function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
modify the given function according to the specified requirements: 
step 1: test if the inputs to the functions are positive.
step 2: if not the inputs are positive display appropriate error messages
step 3: otherwise return the area and perimeter of the rectangle

function :
```{function}```

"""

response = get_response(prompt)
print(response)