import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
# Load the GROQ and OpenAI API keys from Streamlit secrets
# groq_api_key = st.secrets["groq_api_key"]

# Initialize the language model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Set the header of the Streamlit app
st.title("Captions Crafter Bot 🤖")
st.markdown("<h4 style='color:gray;'>Please enter three words that best describe your social media post.</h4>", unsafe_allow_html=True)
st.write("---")

def generate_caption(word1, word2, word3):
    template = "Picture yourself as a clever and creative chat assistant that crafts perfect social media captions using three descriptive words: {word1}, {word2}, and {word3}."
    prompt = PromptTemplate(input_variables=["word1", "word2", "word3"], template=template)
    formatted_prompt = prompt.format(word1=word1, word2=word2, word3=word3)
    response = llm.invoke(formatted_prompt)
    return response.content

# Layout for the input fields
st.markdown("<h5 style='color:blue;'>Enter your words:</h5>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    word1 = st.text_input("First word", placeholder="e.g., sunny")

with col2:
    word2 = st.text_input("Second word", placeholder="e.g., beach")

with col3:
    word3 = st.text_input("Third word", placeholder="e.g., vacation")

# Button to generate the caption
st.write("---")
submit = st.button("Generate Caption")

if submit:
    if word1 and word2 and word3:  # Ensure all three words are provided
        st.markdown("<h5 style='color:green;'>Your Generated Caption:</h5>", unsafe_allow_html=True)
        caption = generate_caption(word1, word2, word3)
        st.markdown(caption, unsafe_allow_html=True)
    else:
        st.error("Please enter all three words to generate a caption.")

# Footer
st.write("---")
st.markdown("<small style='color:gray;'>© 2024 Color Crafter Bot. All rights reserved.</small>", unsafe_allow_html=True)

if __name__ == "__main__":
    pass
