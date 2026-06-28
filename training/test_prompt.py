from prompt_template import create_prompt 

question = "Show all employees"

sql = "SELECT * FROM employees;"

prompt = create_prompt(question,sql)

print(prompt)