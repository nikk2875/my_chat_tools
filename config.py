# Load keys from .env
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# Define providers URL
ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Set API keys
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
gemini_api_key = os.getenv('GOOGLE_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')


# Define models file name - must be in the same folder as the mail Python script
config_file = 'models.yml'

# Define default system message
system_message = "Please assist me on my request."

# Define summarization message
summarize_message='Please summarize the above conversation.'