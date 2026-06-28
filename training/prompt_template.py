# training/prompt_template.py

def create_prompt(question: str, sql: str = "") -> str:
    """
    Creates a training prompt for Text-to-SQL.

    Parameters
    ----------
    question : str
        Natural language question.

    sql : str
        SQL query (only provided during training).

    Returns
    -------
    str
        Formatted prompt.
    """

    prompt = f"""You are an expert SQL developer.

### Instruction:
Convert the following natural language question into SQL.

### Question:
{question}

### SQL:
{sql}"""

    return prompt