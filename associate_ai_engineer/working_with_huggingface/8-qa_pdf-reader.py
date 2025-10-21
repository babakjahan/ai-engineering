from pypdf import PdfReader
from transformers import pipeline

reader = PdfReader("Sample_Employee_Policy.pdf")

document_text = ""
for page in reader.pages:
    document_text += page.extract_text()
    

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

question = "What is the main topic of the document?"
result = qa_pipeline(question=question, context=document_text)
print(f"Question: {question}")
print(f"Answer: {result['answer']}")