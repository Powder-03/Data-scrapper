import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from with_structured_output import Insight
from langchain_core.messages import HumanMessage


load_dotenv()


st.set_page_config(page_title="Company Insights", layout="wide")

st.title("🔍 Company Insight Generator")
st.write("Enter a company name to fetch insights using Google Gemini Pro.")


company_name = st.text_input("Enter Company Name", placeholder="e.g., Maruti Suzuki")


if st.button("Get Insights"):
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.1)
            
            
    template = load_prompt('template.json')
    formatted_prompt = template.format(company_name=company_name)

            
    structured_model = model.with_structured_output(Insight)

            
    result = structured_model.invoke([HumanMessage(content=formatted_prompt)])


    st.subheader(f"Insights for {company_name}")
    st.json(result.dict())  



