from dotenv import load_dotenv
import os
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv()
api = os.getenv('GEMINI_API_KEY')

# Initialize the LLM
llm = GoogleGenerativeAI(api_key=api, model='gemini-pro')

def generate_restaurant_headline_menu(cuisine, diet):
    prompt_headline = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant that serves {cuisine} food. Give me a headline of the restaurant without restaurant name.",
    )
    headline_chain = LLMChain(llm=llm, prompt=prompt_headline, output_key='headline')

    prompt_menu = PromptTemplate(
        input_variables=['headline', 'diet'],
        template="The headline of the restaurant is '{headline}'. Generate a menu that focuses on {diet} options within {headline} theme.",
    )
    menu_chain = LLMChain(llm=llm, prompt=prompt_menu, output_key='menu')

    chain = SequentialChain(
        chains=[headline_chain, menu_chain],
        input_variables=['cuisine', 'diet'],
        output_variables=['headline', 'menu'],
    )

    response = chain({'cuisine':cuisine, 'diet':diet})
    return response

st.title('Personalized Restaurant Menu Recommendation System')
cuisine = st.sidebar.text_input("Enter the cuisine name")
diet = st.sidebar.text_input("Enter the diet preference")

if cuisine and diet:
    response = generate_restaurant_headline_menu(cuisine, diet)
    st.header(response['headline'])
    menu_items = response['menu'].split(',')
    st.write("Personalized Menu:")
    for item in menu_items:
        st.write("-", item)