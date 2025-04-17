# Agent_AI

An experimental agentic AI system designed to autonomously solve complex tasks through reasoning, planning, and execution.

Note this only works on Python 3.11 at the moment.

## Overview

Agent_AI is a prototype framework that enables AI models to operate as autonomous agents capable of:
- Breaking down complex problems into manageable steps
- Planning and executing multi-stage tasks
- Learning from feedback and adapting strategies
- Interacting with external tools and environments

This project explores the frontier of agentic AI systems, aiming to create more capable and reliable autonomous agents.

## Features

- **Modular Architecture**: Separate components for reasoning, planning, memory, and execution
- **Tool Integration**: Built-in support for various external tools and APIs
- **Adaptive Planning**: Dynamic adjustment of plans based on execution results
- **Local LLMs**: Ability to run the LLMs and Agents locally using OLLAMA. NO MONTHLY FEES!!

## Installation

```bash
# Clone the repository
git clone https://github.com/RagsX137/Agent_AI.git
cd Agent_AI

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Getting Started

1. Go to serper.dev and create an account. Get an API key and put that API key inside your  `.env` file
2. Run the agent with:
   ```bash
   python main.py 
   ```

## Limitations

This is an experimental prototype with known limitations:
Current limitations
- Hardcoded prompts, model names and tasks.
- Performance degrades with extremely complex tasks
- Limited self-correction capabilities in novel domains
- Tool integration requires careful configuration
- Resource intensive for long-running tasks

## Improvements on the way
- Modularization of prompts, model names and tasks.
- Expansion of capabilities. Currently only 2 agents and 2 tasks

## Citation

If you use Agent_AI in your research, please cite:
```
@software{agent_ai_2025,
  author = {RagsX137},
  title = {Agent_AI: An Experimental Agentic AI System},
  year = {2025},
  url = {https://github.com/RagsX137/Agent_AI}
}
```

## Acknowledgements

Special thanks to the open-source community and research collaborators who have contributed ideas and feedback to this project.
