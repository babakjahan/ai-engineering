from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

text = "I love programming with Python! It's such a versatile language."

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Download the model and tokenizer
my_model = AutoModelForSequenceClassification.from_pretrained(model_name)
my_tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the pipeline
my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# Predict the sentiment
output = my_pipeline("This course is pretty good, I guess.")

tokens = my_tokenizer.tokenize(text)
print(f"Tokenized output: {tokens}")
print(f"Sentiment using AutoClasses: {output[0]['label']}")

