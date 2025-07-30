import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
import json
from pprint import pprint
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

chat_store = {}

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message,model, session_id=None) -> None:
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.session_id = session_id
        self.llm = model

    def diplay_result_on_ui(self):
        usecase=self.usecase
        graph = self.graph
        user_message = self.user_message
        session=self.session_id
        model = self.llm
        
        # FUNCTION TO STORE AND UPDATE BaseChatMessageHistory
        def get_session_history(session_id:str)->BaseChatMessageHistory:
            if session_id not in chat_store:
                # messages are stored in-memory means ram ,,, we can also store in database but not doing right now
                chat_store[session_id]=ChatMessageHistory()
            return chat_store[session_id]
        
        with_message_history=RunnableWithMessageHistory(model,get_session_history)
        
        if usecase == "Basic Chatbot":
            # Create messages for the model
            messages = [{"role": "user", "content": user_message}]
            
            # Invoke the model with message history
            response = with_message_history.invoke(
                messages,
                config={"configurable": {"session_id": session}}
            )
            
            
            # Display chat history
            history = get_session_history(session)
            if history.messages:
                st.subheader("📝 Chat History")
                for msg in history.messages:
                    if hasattr(msg, 'type') and msg.type == 'human':
                        with st.chat_message("user"):
                            st.write(msg.content)
                    elif hasattr(msg, 'type') and msg.type == 'ai':
                        with st.chat_message("assistant"):
                            st.write(msg.content)

        elif usecase=="Chatbot with Tool":
             # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()
                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    
                
                with open(AI_NEWS_PATH, 'r') as f:
                    st.download_button(
                        "💾 Download Summary",
                        f.read(),
                        file_name=AI_NEWS_PATH,
                        mime="text/markdown"
                    )
                st.success(f"✅ Summary saved to {AI_NEWS_PATH}")
