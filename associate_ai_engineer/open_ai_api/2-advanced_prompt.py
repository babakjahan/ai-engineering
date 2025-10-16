from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

prompt="""Replace car with plane and adjust phrase:
A plane is a vehicle that is typically powered by an internal combustion engine or an electric motor.
It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Planes have become a ubiquitous part of modern society,
and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods.
Planes are often associated with freedom, independence, and mobility."""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,

    messages=[{"role": "user", "content": prompt}]  

)

print(response.choices[0].message.content)