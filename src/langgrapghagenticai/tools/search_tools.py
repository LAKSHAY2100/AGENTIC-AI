# from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain_tavily import TavilySearch

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    # import os
    # if tavily_api_key:
    #     # Set the environment variable as well
    #     os.environ["TAVILY_API_KEY"] = tavily_api_key
    #     tools=[TavilySearch(max_results=2)]
    #     if  
    # else:
    #     tools=[TavilySearch(max_results=2)]



    tools=[TavilySearch(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)