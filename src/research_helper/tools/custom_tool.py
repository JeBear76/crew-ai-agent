import requests
from langchain.tools import tool
import json
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchResults

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = (
        "Searches for a given query on DuckDuckGo."
    )
    
    def _run(self, argument: str) -> str:
        result = DuckDuckGoSearchResults(num_results=10, output_format='json').invoke(argument)
        return result
