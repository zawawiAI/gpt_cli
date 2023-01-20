import openai

# Set up the OpenAI API client
openai.api_key = "Your OpenAI API Key"

# Set up the model and prompt
model_engine = "text-davinci-003"

# Initialize a variable to store the previous response
response = ""

while True:
    prompt = input("Search: ")
    if prompt.strip().lower() == "exit":
        break
    try:
        if prompt.strip().lower() != "save":
            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0.52,
                presence_penalty=0.5,
                stop=["11."]
            )

            # Extract the response text
            response = completion.choices[0].text
            print(response)
        else:
            # Check if there is a previous response to save
            if response == "":
                print("No previous response to save.")
            else:
                # Prompt the user to enter a file name
                file_name = input("Enter a file name: ")

                # Write the response to the file
                with open(file_name, "w") as f:
                    f.write(response)
                    f.close()

                # Confirm that the file was saved
                print(f"Response saved to {file_name}")
    except openai.exceptions.OpenAiError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: No response generated")
    except Exception as e:
        print(f"Error: {e}")
