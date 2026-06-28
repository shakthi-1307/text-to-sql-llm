import json 

from datasets import Dataset 

from transformers import AutoTokenizer 

from config import MODEL_NAME,MAX_LENGTH,TRAIN_DATA_PATH

from prompt_template import create_prompt 

def load_json(path):
    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)
        
    return data 

def build_prompts(data):
    prompts = []
    
    for row in data:
        prompt = create_prompt(
            question = row["input"],
            sql = row["output"]
        )
        prompts.append(prompt)
        
    return prompts

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize(example):
    return tokenizer(
        example["text"],
        truncation = True,
        padding = "max_length",
        max_length = MAX_LENGTH 
    )
    
def prepare_dataset():
    data = load_json(TRAIN_DATA_PATH)
    
    prompts = build_prompts(data)
    
    dataset = Dataset.from_dict(
        {
            "text" : prompts
        }
    )
    
    tokenized_dataset = dataset.map(
        tokenize,
        batched = True
    )
    
    return tokenized_dataset