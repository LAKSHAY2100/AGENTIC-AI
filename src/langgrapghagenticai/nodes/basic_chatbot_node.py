from src.langgrapghagenticai.state.state import State

class BasicChatbotNode:
    def __init__(self,model) -> None:
        self.llm = model
    
    def process(self , state:State):
        return {'messages':[self.llm.invoke(state['messages'])]}