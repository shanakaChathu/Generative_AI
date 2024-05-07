import os 
import openai 
from dotenv import load_dotenv, find_dotenv


class OpenAIChat(): 

    def init(): 
        pass 

    def get_completion(prompt, model="gpt-3.5-turbo"):
        """
        given prompt this will generate response
        input: promopt, model 
        output: response for the prompt
        """
        messages = [{"role": "user", "content": prompt}]
        response=openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0, 
        )
        return response.choices[0].message.content
    

    def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
    #     print(str(response.choices[0].message))
        return response.choices[0].message.content
        
    
    

