# my_chat_tools
A collection of tools that I built for personal training:
- **get_models.py** => This is a standalone utility to retrieve all available API models per provider. Providers are OpenAI, Anthropic, Google, xAI, Groq and Ollama. I used it to update the `models.yml` file properly (which is used by the chatbots to choose for a working model).
- **my_chatbot.py** => This is a chatting interface, that I made for personal use and provides some features that I could not find in other tools:
    - Be able to use models of any provider without the limitations of free tiers, but do not be tied to a specific subscription and allow flexibility.
    - Add features like the summarization to improve personal efficiency.
    - Use multiple models in the same conversation. For example, start with Sonnet, when you need something more advanced ask Opus, and for simple tasks like summarization go to Haiku (or even better to Ollama!).
I plan to extend with more features in the future.

### Other files:
- **.sample_env** => This is a sample for the `.env` file, that is required for storing the API keys.
- **config.py** => This code is used to set up the API keys, provider URLs and other important parameters.

## Executing the code - FOR LINUX
Once you have cloned the repository, you need to install the dependencies and run the script:
1. **Installation** => Go to the folder where you cloned the repo and find `install.sh`. Edit the file and define a target folder, run `chmod +x install.sh` and then `./install.sh`. *It is assumed that you have `uv` installed in your system!*
2. **Execution** => You will find the Python code on the target folder that you defined in the previous step. But, I wanted to have the caller on its parent folder, so you need to find `my_chatbot.sh` there. Find it and make it executable with `chmod +x my_chatbot.sh`, then run the app with `./my_chatbot.sh`. To initiate the App open the URL (http://127.0.0.1:7860/) in any browser.