#from datasets import load_dataset
from datasets import Dataset


# Use the small demo version (only a few hundred examples)
#wikipedia = load_dataset("wikimedia/wikipedia", "20231101.en", split="validation[:0.1%]")


# Your Wikipedia-style text
text = """Luis Miguel Aparecido Alves (born May 25, 1985), known as Gugu, 
is a Brazilian football player currently playing for Iraklis Psachna F.C.

External links

1985 births
Living people
Brazilian men's footballers
Thrasyvoulos F.C. players
Ionikos F.C. players
Super League Greece players
Expatriate men's footballers in Greece
Brazilian expatriate men's footballers
Men's association football midfielders
"""

# Create a dataset with the same structure as real Wikipedia dataset
data = {
    "id": ["1"],
    "url": ["https://en.wikipedia.org/wiki/Luis_Miguel_Aparecido_Alves"],
    "title": ["Luis Miguel Aparecido Alves"],
    "text": [text],
}

# Convert to a Hugging Face Dataset
wikipedia = Dataset.from_dict(data)

# Filter the documents
filtered = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = filtered.select(range(1))


print(example[0]["text"])