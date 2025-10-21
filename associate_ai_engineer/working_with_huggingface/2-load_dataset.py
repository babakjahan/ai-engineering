from datasets import load_dataset

my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="validation")

print(my_dataset[0])

