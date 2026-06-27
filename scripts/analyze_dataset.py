import json 

with open("data/processed/train.json","r",encoding="utf-8") as f:
    data = json.load(f)
    
print("samples:",len(data))