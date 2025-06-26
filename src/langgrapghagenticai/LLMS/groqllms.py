from langchain_groq import ChatGroq
import streamlit as st

class Groqllm:
    def __init__(self , user_control_input):
        self.user_control_input = user_control_input

    def get_llm_models(self):
        try:
            groq_api_key = self.user_control_input['GROQ_API_KEY']
            selected_groq_model = self.user_control_input['selected_groq_model']
            if groq_api_key==' ':
                st.error("Please enter a valid api key")
            else:
                llm = ChatGroq(model=selected_groq_model , api_key=groq_api_key)
        except Exception as e :
            raise ValueError(f"Error occured with exception {e}")
        return llm
