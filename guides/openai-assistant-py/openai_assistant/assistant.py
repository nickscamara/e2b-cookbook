from typing import List

from dotenv import load_dotenv
import openai
from openai.types.beta.assistant_create_params import Tool

load_dotenv()


def create_assistant():
    client = openai.Client()

    functions: List[Tool] = [
        {
            "type": "function",
            "function": {
                "name": "save_content_to_file",
                "description": "Save content (code or text) to file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The content to save",
                        },
                        "filename": {
                            "type": "string",
                            "description": "The filename including the path and extension",
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "write_to_file",
                "description": "Write text or other content to a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The content to save",
                        },
                        "filename": {
                            "type": "string",
                            "description": "The filename including the path and extension",
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_files",
                "description": "List files in a directory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to the directory",
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to the file",
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "commit_and_push",
                "description": "Commit and push changes to the repository",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "commit_message": {
                            "type": "string",
                            "description": "The commit message",
                        },
                    },
                },
            },
        },
    ]

    ai_developer = client.beta.assistants.create(
        instructions="""You are an AI developer.
    The provided codebase is in the /home/user/repo.
    When given a coding task, you will work on it until it is completed. You will summarize your steps.
    If you encounter some problem, just communicate it please. 
    You can save code to file (or create a new file), list files in a given directory, read files, and commit and push changes.
    Please every time you are asked to do a task, do the task the best you can, and then commit and push it without asking.
    You are professional, don't argue, and just complete the task.
    Here are few model examples for you to understand how to communicate with the person assigning you the task (we will call them "User" and you "AI developer"):
    Example 1:
    User: Create a file called "hello.py" in the /home/user/repo directory.
    AI developer: I created the file called "hello.py" in the /home/user/repo directory.
    Example 2:
    User: Create a file called "hello.py" in the /home/user/repo directory.
    AI developer: I created the file called "hello.py" in the /home/user/repo directory.
    Example 3:
    User: List all non-empty files in the given repository.
    AI developer: I listed all non-empty files in the given repository.
    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()
