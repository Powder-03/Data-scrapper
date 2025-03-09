from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """You work is to do web scrapping and find all the information in the structured format about the company {company_name}
    """,
input_variables= ['company_name'],
validate_template = True
)
template.save('template.json')