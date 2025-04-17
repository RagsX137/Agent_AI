
from crewai import Agent, LLM 
from crewai import Task
from crewai_tools import SerperDevTool
import os
## Tools
search = SerperDevTool()

# Create First Agent
researcher = Agent(
    # llm=llm,
    llm= LLM(model="ollama/deepseek-r1:1.5b", base_url="http://localhost:11434"),
    function_calling_llm=LLM(model="ollama/gemma3:4b", base_url="http://localhost:11434"),
    role="Senior AI Researcher",
    goal="Find promising research in the field of Quantum Computing.",
    backstory="You are a veteran quantum computing researcher with background in modern physics",
    allow_delegation=False,
    tools=[search],
    verbose = 1,
    # endpoint = "http://localhost:11434"
    )


# Create Second Agent
writer = Agent(
    # llm=llm,
    llm= LLM(model="ollama/llama3.2:3b", base_url="http://localhost:11434"),
    role="Senior Speech Writer.",
    goal="Write engaging and witty keynote speeched from the provided research",
    backstory="You are a veteran quantum computing writer with background in modern physics",
    allow_delegation=False,
    verbose = 1,
    # endpoint = "http://localhost:11434"
    )

# Create a task
task1 = Task(
    description="Search the internet and find 5 examples of promising AI research.",
    expected_output="A detailed bullet point summary on each of the topics. Each bullet point should cover the topic, background and why the innovation is useful.",
    output_file="task1output.txt",
    agent=researcher,
)

# Create a task
task2 = Task(
    description="Write an engaging keynote speech on quantum computing.",
    expected_output="Detailed keynote speech with an intro, body and a conclusion",
    output_file="task2output.txt",
    agent=writer,
)