from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgrapghagenticai.state.state import State
from src.langgrapghagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class Graphbuilder:
    def __init__(self,model) -> None:
        self.llm = model
        self.graph_builder = StateGraph(State)

    def setup_graph(self,usecase:str):
        if(usecase=='Basic Chatbot'):
            self.basic_chatbot_build_graph()
            
    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)
