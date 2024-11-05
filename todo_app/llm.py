import os
import anthropic
import openai
from transformers import pipeline
from dotenv import load_dotenv
import cohere
load_dotenv() 

co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def get_cohere_response(todo_title):
    try:
        response = co.chat(
            model="command-r-plus", 
            messages=[
                {
                    "role": "user",
                    
                    "content": f"Generate a list of concise and actionable tips for '{todo_title}'. Each tip should be one sentence long and focus on practicality. The suggestions should help someone successfully complete the task with minimal preparation."
                }
            ]
        )

        
        generated_message = response.message.content[0] 
        return generated_message.text 

    except Exception as e:
        print(f"An error occurred while getting response: {e}")
        return "Error generating response."



