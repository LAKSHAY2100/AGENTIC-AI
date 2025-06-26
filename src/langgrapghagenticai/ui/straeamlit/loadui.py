import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from src.langgrapghagenticai.ui.uiconfigfile import Config
class loadstreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control ={}
    
    def initialize_session(self):
        return{
            "current_step":"requirements",
            "requirements":"",
            "user_stories":"",
            "po_feedback":"",
            "generated_code":"",
            "review_feedback":"",
            "decision":None
        }

    def render_requirements(self):
        st.markdown("Requirements Submission")
        st.session_state.state['requirements']=st.text_area(
            "Enter your requirements",
            height=200,
            key='red'
        )
        if st.button("submit requirements",key="submit_req"):
            st.session_state.state['current_step'] = "generate_user_stories"
            st.session_state.IsSDLC =True

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖"+self.config.get_page_title(),layout="wide")    
        st.header("🤖"+self.config.get_page_title())
        st.session_state.timeframe=""
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            llm_options = self.config.get__llm__option()
            usecase_options = self.config.get__usecase__option()

            self.user_control["selected_llm"] = st.selectbox("selected llm",llm_options)

            if(self.user_control['selected_llm'] == "Groq"):
                model_options = self.config.get__groq_model__option()
                self.user_control["selected_groq_model"] = st.selectbox("selected model" , model_options)

                self.user_control["GROQ_API_KEY"] = st.session_state['GROQ_API_KEY'] =st.text_area("API key" , key="password")

                if not self.user_control['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API key to proceed ,. Dont have ? refer:https://console.groq.com/keys")
            
            self.user_control["selected_usecase"] = st.selectbox("select usecase" , usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            self.render_requirements()

        return self.user_control