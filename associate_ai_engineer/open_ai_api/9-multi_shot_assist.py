from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries.just talk about borders country and capital city."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Give me a quick summary of USA."},
       {"role": "assistant", "content": "USA is a country in North America that borders Canada & Mexico. The capital city is Washington, D.C."},
       {"role": "user", "content": "Give me a quick summary of Netherlands."},
       {"role": "assistant", "content": "Netherlands is a country in Europe that borders Germany and Belgium. The capital city is Amsterdam"},
       {"role": "user", "content": "Give me a quick summary of Romania."},
       {"role": "assistant", "content": "Romania is a country in Europe that borders Bulgaria, Serbia, Hungary, Slovakia, Ukraine and Moldavia. The capital city is Bucharest"},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)