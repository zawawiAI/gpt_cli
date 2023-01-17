# chatgpt_cli
This scripts allows you to use OpenAI in your Linux terminal 

This is a command line tool that allows you to search using the OpenAI API your CLIs such as Linux terminal or Windows Command Prompt (I have not personally tested). It uses the openai library to interact with the API and the text-davinci-003 model to generate responses to your queries.

Getting Started

Install the openai library by running pip install openai in your command line.

Set up an API key for the OpenAI API by signing up for an account on the OpenAI website and obtaining a key.

Replace "Your OpenAI API Key" in the code with your own API key.

Run the code with python chatgpt_linuxterminal.py and start searching.

Usage

The tool will prompt you to enter a search query. Once you enter your query, it will generate a response using the text-davinci-003 model. You can search for any topic you want, and the model will generate a relevant response.

You can change the model_engine to any other OpenAI's models. Also, you can play with the max_tokens, n, stop, and temperature parameters to customize the output of the model.

Tips

Keep your queries concise and specific for more accurate results.
If you are not satisfied with the response, try rephrasing your query or adjusting the temperature parameter.
Feel free to experiment with different models to see which one works best for your use case.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
