import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv 
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#Function to load OpenAI model and get response 

def get_open_ai_response(question):
  llm = OpenAI(temperature=0.5,model_name="gpt-3.5-turbo-instruct")
  response = llm(question)
  return response

  #Initialize streamlit app 
st.set_page_config(page_title='QA demo')
st.header("LangChain Application")

input = st.text_input("Please type your Question:", key="input")
response = get_open_ai_response(input)
submit = st.button("Ask the Question", use_container_width=False)


#If "Ask the Question" button is clicked
if submit:
  st.subheader("The Response is")
  st.write(response)
