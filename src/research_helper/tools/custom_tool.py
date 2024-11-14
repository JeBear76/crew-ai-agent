import requests
from langchain.tools import tool
import json
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool
from langchain_community.tools import DuckDuckGoSearchResults

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = (
        "Searches for a given query on DuckDuckGo."
    )
    
    def _run(self, argument: str) -> str:
        result = DuckDuckGoSearchResults(num_results=5, output_format='json').invoke(argument)        
        siteScraperTool = SiteScraperTool(json.loads(result))
        result = siteScraperTool.getRawSiteData()
        return json.dumps(result)

class SiteScraperTool:
    def __init__(self, sites):
        self.sites = sites
        self.tool = ScrapeWebsiteTool()

    def getRawSiteData(self):
        for site in self.sites:
            text = self.tool.run(website_url=site['link'])
            site['snippet'] = text
        return self.sites