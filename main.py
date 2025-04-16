from agents import *
from crewai import Crew, Task, Agent, LLM
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()
config = dotenv_values(".env")
os.environ["SERPER_API_KEY"] = config['SERPER_API_KEY']
## Tools
search = SerperDevTool()

# Put it all together with the crew
crew = Crew(agents =[researcher,writer], tasks=[task1,task2], verbose = 1)
print(crew.kickoff())