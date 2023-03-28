import openai
import os.path
from datetime import date

today = date.today()
file_name = today.strftime("%b-%d-%Y") + ".txt"
path = "/home/rowan/gpt_cli/logs/" + file_name
class OpenAIAPI:
    def __init__(self, api_key, model_engine):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.response = ""
        self.prompt = ""
        
    def generate_response(self, prompt):
        """
        Generates a response for the given prompt
        """
        self.prompt = prompt
        completion = openai.ChatCompletion.create(model=self.model_engine, messages=[{"role": "user", "content": prompt}])
        self.response = completion.choices[0].message.content
        return self.response

    def save_response(self, file_name):
        """
        Saves the current response to a file
        """
        if(os.path.isfile(file_name)):
            with open(file_name, "a") as f:
                f.write("\n\n")
                f.write("###############\n\n")
                f.write(f"Model: {self.model_engine}\n\n")
                f.write(f"Prompt: {prompt}\n\n")
                f.write(f"Response:\n {self.response}")
                f.close()
            print(f"Response saved to {file_name}")
        else:
            with open(file_name, "x") as f:
                f.write(f"Model: {self.model_engine}\n\n")
                f.write(f"prompt: {prompt}\n\n")
                f.write(f"response: {self.response}")
                f.close()
            print(f"Response saved to {file_name}")
            
    def handle_exception(self, e):
        """
        Handles any exceptions that occur
        """
        if isinstance(e, openai.exceptions.OpenAiError):
            print(f"Error: {e}")
        elif isinstance(e, IndexError):
            print("Error: No response generated")
        else:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    model_name = input("Model: ")
    if(model_name == "3.5"):
        model_name = "gpt-3.5-turbo"
    elif(model_name == "4"):
        model_name = "gpt-4"
    save_option = input("Do you want to save your work? ")
    api = OpenAIAPI("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", model_name)
    while True:
        prompt = input("Search: ")
        if prompt.strip().lower() == "exit":
            break
        try:
            response = api.generate_response(prompt)
            print("\n")
            print(response)
            print("\n\n")
            if(save_option.strip().lower() == "yes"):    
                api.save_response(path)
        except Exception as e:
            api.handle_exception(e)

