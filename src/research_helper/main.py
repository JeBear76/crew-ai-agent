#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
load_dotenv()
from langtrace_python_sdk import langtrace
langtrace.init(api_key=os.getenv("LANGTRACE_API_KEY"))
               
from research_helper.crew import ResearchHelper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Robotic Process Automation, Organizational Network Analysis and AI LLMs'
    }
    ResearchHelper().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'Robotic Process Automation, Organizational Network Analysis and AI LLMs'
    }
    try:
        ResearchHelper().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResearchHelper().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'Robotic Process Automation, Organizational Network Analysis and AI LLMs'
    }
    try:
        ResearchHelper().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
