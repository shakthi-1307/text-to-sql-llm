from datasets import load_dataset 
import json 

spider = load_dataset("spider")

processed = []

for row in spider["train"]:
    processed.append(
        {
            "instruction": "Convert natural language to SQL",
            "input":row["question"],
            "output":row["query"]
        }
    )
    
with open("data/processed/train.json","w",encoding="utf-8") as f:
    json.dump(processed,f,indent=4)