import os
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from research_helper.tools.custom_tool import DuckDuckGoSearchTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
duckducktool = DuckDuckGoSearchTool(result_as_answer=True)
huggingfavce_llm = LLM(
	model="huggingface/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF", 
	api_key=os.getenv("HUGGINGFACE_API_KEY")

)

google_llm=LLM(
	model="gemini/gemini-1.5-flash", 
	temperature=0.6, 
	api_key=os.getenv("GOOGLE_API_KEY"),
)    

perplexity_llm = LLM(
    model="llama-3.1-sonar-large-128k-online",
    base_url="https://api.perplexity.ai",
    api_key=os.getenv("PERPLEXITY_API_KEY")
)

@CrewBase
class ResearchHelper():
	"""ResearchHelper crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def web_surfer(self) -> Agent:
		return Agent(
			config=self.agents_config['web_surfer'],			
		)

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			llm=perplexity_llm,
			
		)
	
	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm=google_llm,
			
		)

	@task
	def web_search_task(self) -> Task:
		return Task(
			config=self.tasks_config['web_search_task'],
			tools=[duckducktool],	
			verbose=True,			
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],

			output_file=f'./output/report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ResearchHelper crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
