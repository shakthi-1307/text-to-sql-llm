from datasets import load_dataset

spider = load_dataset("spider")

sample = spider["train"][0]

for key in sample:
    print(f"key : {key}\nvalue: {sample[key]}")
    
print("\nQuestion")
print(sample["question"])

print("\nSQL")
print(sample["query"])