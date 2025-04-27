from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Setup your Azure OpenAI connection
openai_api_key = st.secrets["openai_api_key"]
openai_endpoint_url = st.secrets["openai_endpoint_url"]

llm = AzureChatOpenAI(
    openai_api_key=openai_api_key,
    azure_endpoint=openai_endpoint_url,
    deployment_name="gpt-4o-mini",  # Replace with your Azure OpenAI deployment name
    api_version="2025-01-01-preview",
    streaming=True  # Enable streaming for auto-scroll
)

def generate_answer(prompt):
    prompt_template = PromptTemplate(input_variables=["prompt"], template="{prompt}")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    response = chain.run({"prompt": prompt})
    return response.strip()