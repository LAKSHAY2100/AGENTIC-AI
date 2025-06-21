from configparser import ConfigParser

class Config:
    def __init__(self,config_file="src\langgrapghagenticai\ui\uniconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)
    
    def get__llm__option(self):
        return self.config['DEFAULT'].get('LLM_OPTIONS').split(',')
    
    def get__usecase__option(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS').split(',')
    
    def get__groq_model__option(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS').split(',')
    
    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')
    