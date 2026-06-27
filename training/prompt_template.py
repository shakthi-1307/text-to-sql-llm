def create_prompt(schema,question,sql=None):
    prompt = f"""
    You are an expert SQL Developer.
    
    Database Schema:{schema}
    
    Question:{question}
    
    SQL:
    """
    
    if sql:
        prompt += sql
        
    return prompt