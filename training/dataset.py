import json 

from prompt_template import create_prompt 

def load_data(path):
    with open(path,"r",encoding="utf-8") as f:
        data =json.load(f)
        
    prompts = []
    
    for row in data:
        schema = row.get(
            "schema",
            "No schema avaiable"
        )
        
        prompt = create_prompt(
            schema,
            row["input"],
            row["output"]
        )
        
        prompts.append(prompt)
        
    return prompts