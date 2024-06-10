import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load the GROQ and OpenAI API keys
# groq_api_key = os.getenv('GROQ_API_KEY')

groq_api_key=st.secrets["groq_api_key"]
# Initialize the language model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Set the header of the Streamlit app
st.header("Generate Captions 🤖")
st.write("Please enter three words that best describe your social media post.")

def generate_caption(word1, word2, word3):
    template = "Picture yourself as a clever and creative chat assistant that crafts perfect social media captions using three descriptive words: {word1}, {word2}, and {word3}."
    prompt = PromptTemplate(input_variables=["word1", "word2", "word3"], template=template)
    formatted_prompt = prompt.format(word1=word1, word2=word2, word3=word3)
    response = llm.invoke(formatted_prompt)
    return response.content

# Layout for the input fields
col1, col2, col3 = st.columns(3)

with col1:
    word1 = st.text_input("word1")

with col2:
    word2 = st.text_input("word2")

with col3:
    word3 = st.text_input("word3")

# Button to generate the caption
submit = st.button("Generate")

if submit:
    if word1 and word2 and word3:  # Ensure all three words are provided
        caption = generate_caption(word1, word2, word3)
        st.markdown(caption)
    else:
        st.error("Please enter all three words to generate a caption.")

if __name__ == "__main__":
    pass
