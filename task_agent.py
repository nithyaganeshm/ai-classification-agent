import os
from dotenv import load_dotenv
from openai import OpenAI

# load env
load_dotenv()

# get env file from .env
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the OpenAI client instance
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# read tasks method
def read_tasks(filepath):
     with open(filepath, 'r') as file:
         return file.read()

# Summarize tasks
def summarize_tasks(tasks):
    formatted_prompt = f"""
    You are a smart task planning agent.
    Given a list of tasks, categorize them into 3 priority
    buckets:
    - High Priority
    - Medium Priority
    - Low Priority

    Tasks:
    {tasks}

    Return the response in this format:
    High Priority:
    - task 1
    - task 2

    Medium Priority:
    - task 1
    - task 2
    - task 3

    Low Priority:
    ...
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": formatted_prompt}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("Task Summary")
    print("*" * 30)
    print(f"\n{summary}")