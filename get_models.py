# Import configuration parameters
import config

# Function to return models
def get_models(provider, api_key, base_url):
    from openai import OpenAI
    client = OpenAI(api_key=api_key, base_url=base_url)
    models = client.models.list().data
    print(80 * '-')
    print(f'{provider}:')
    print(20 * '-')
    for model in models:
        print(model.id)

# Function to return Anthropic models
def get_anthropic_models():
    from anthropic import Anthropic
    client = Anthropic(api_key=config.anthropic_api_key)
    models = client.models.list().data
    print(80 * '-')
    print('Anthropic:')
    print(20 * '-')
    for model in models:
        print(model.id)

# Function to return Ollama local models
def get_ollama_models():
    import ollama
    models = ollama.list().models
    print(80 * '-')
    print('Ollama:')
    print(20 * '-')
    for model in models:
        print(model.model)


### Get and print list of models ###

# OpenAI
get_models('OpenAI', config.openai_api_key, None)
# Gemini
get_models('Google Gemini', config.gemini_api_key, config.GEMINI_BASE_URL)
# Grok
get_models('Grok', config.grok_api_key, config.GROK_BASE_URL)
# Groq
get_models('Groq', config.groq_api_key, config.GROQ_BASE_URL)
# OpenRouter
get_models('OpenRouter', config.openrouter_api_key, config.OPENROUTER_BASE_URL)
# Anthropic
get_anthropic_models()
# Ollamacle
get_ollama_models()