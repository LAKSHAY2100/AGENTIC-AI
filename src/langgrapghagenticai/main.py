import streamlit as st
import json
from src.langgrapghagenticai.ui.straeamlit.loadui import loadstreamlitUI
from src.langgrapghagenticai.LLMS.groqllms import Groqllm
from src.langgrapghagenticai.graphs.graph_builder import GraphBuilder

# from src.langgrapghagenticai.ui.straeamlit.display_result import DisplayResultStreamlit
# MAIN Function START
def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
   
    # Load UI
    ui = loadstreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = Groqllm(user_control_input=user_input)
            model = obj_llm_config.get_llm_models()
            
            if not model:
                st.error('Error : LLM could not be initialized')
                return
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("No usecase selected")
                return
            
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error: Graph Setup Failes {e}")
                return

        except Exception as e:
            raise ValueError(f"Error {e}")
                

            

        

   

    