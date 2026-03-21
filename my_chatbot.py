# Import libraries and configuration
import yaml
import gradio as gr
from pathlib import Path
from openai import OpenAI
import config

# Load the models configuration from YAML file
def load_models_config():
    config_path = Path(__file__).parent / config.config_file
    with open(config_path, 'r') as f:
         yaml_config = yaml.safe_load(f)
    return yaml_config['providers']

# Get list of provider display names
def get_provider_names(providers):
    return [provider_data['name'] for _, provider_data in providers.items()]

# Get provider ID from display name
def get_provider_id_by_name(providers, provider_name):
    for provider_id, provider_data in providers.items():
        if provider_data['name'] == provider_name:
            return provider_id
    return None

# Get list of models for a specific provider
def get_models_for_provider(providers, provider_name):
    provider_id = get_provider_id_by_name(providers, provider_name)
    if provider_id and provider_id in providers:
        return providers[provider_id]['models']
    return []

# Get API key and base URL for a provider
def get_api_key_and_base_url(provider_id):
    api_keys = {
        'openai': config.openai_api_key,
        'anthropic': config.anthropic_api_key,
        'gemini': config.gemini_api_key,
        'grok': config.grok_api_key,
        'groq': config.groq_api_key,
        'ollama': 'ollama'
    }
    base_urls = {
        'openai': None,  # OpenAI uses default
        'anthropic': config.ANTHROPIC_BASE_URL,
        'gemini': config.GEMINI_BASE_URL,
        'grok': config.GROK_BASE_URL,
        'groq': config.GROQ_BASE_URL,
        'ollama': config.OLLAMA_BASE_URL
    }
    return api_keys.get(provider_id), base_urls.get(provider_id)

# Update the models dropdown based on selected provider
def update_models_dropdown(provider_name):
    providers = load_models_config()
    models = get_models_for_provider(providers, provider_name)
    return gr.Dropdown(choices=models, value=models[0], interactive=True)

# Call API to get a response
def chat(history, provider_name, model_name, system_message):
    providers = load_models_config()
    provider_id = get_provider_id_by_name(providers, provider_name)
    api_key, base_url = get_api_key_and_base_url(provider_id)

    try:
        # Build conversation
        messages = []
        if system_message.strip():
            messages.append({"role": "system", "content": system_message})
        else:
            messages.append({"role": "system", "content": config.system_message})
        messages = messages + history

        # Send conversation to the API
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Unexpected error in chat: {type(e).__name__}: {str(e)}"


### MAIN ###
def main():
    # Load configuration
    providers = load_models_config()
    provider_names = get_provider_names(providers)
    initial_models = get_models_for_provider(providers, provider_names[0])

    # Create Gradio interface
    with gr.Blocks(title="My Chatbot") as bot:
        gr.Markdown("# My Chatbot")

        with gr.Row():
            provider_dropdown = gr.Dropdown(
                choices=provider_names,
                label="Provider",
                value=provider_names[0],
                interactive=True
            ) 
            model_dropdown = gr.Dropdown(
                choices=initial_models,
                label="Model",
                value=initial_models[0],
                interactive=True
            )

        system_msg = gr.Textbox(
            label="System Message",
            placeholder="Enter system message (optional)...",
            lines=2
        )

        chatbot = gr.Chatbot(label="Chat", height=400)
        msg = gr.Textbox(label="Message", placeholder="Type your message here...")

        with gr.Row():
            submit = gr.Button("Send", variant="primary", scale=1)
            summarize = gr.Button("Summarize", variant="secondary", scale=1)  
            clear = gr.Button("New Chat", variant="secondary", scale=1)
            exitapp = gr.Button("Exit App", variant="stop", scale=1)

        # Add user message to history
        def user_message(message, history):
            if not message:
                return "", history
            return "", history + [{"role": "user", "content": message}]
        
        # Send request to summarize
        def create_summary(message, history):
            return "", history + [{"role": "user", "content": config.summarize_message}]  

        # Generate bot response
        def bot_response(history, provider_name, model_name, system_message):
            chat_history = [{"role":h["role"], "content":h["content"][0]["text"]} for h in history]
            bot_reply = chat(chat_history, provider_name, model_name, system_message)
            return history + [{"role": "assistant", "content": bot_reply}]

        # Clear the chat history
        def clear_chat():
            return [], ""
        
        # Exit the app with proper cleanup
        def exit_app():
            import threading
            import time
            def shutdown():
                time.sleep(0.5)
                bot.close()
            threading.Thread(target=shutdown, daemon=True).start()
            gr.Info("Shutting down the application...")
            return None

        # Update models when provider changes
        provider_dropdown.change(
            fn=update_models_dropdown,
            inputs=[provider_dropdown],
            outputs=[model_dropdown]
        )

        # Handle message submission
        submit.click(user_message, [msg, chatbot], [msg, chatbot]).then(
            bot_response, [chatbot, provider_dropdown, model_dropdown, system_msg], [chatbot]
        )

        # Handle summarization
        summarize.click(create_summary, [msg, chatbot], [msg, chatbot]).then(
            bot_response, [chatbot, provider_dropdown, model_dropdown, system_msg], [chatbot]
        )

        # Handle clear button
        clear.click(clear_chat, None, [chatbot, msg])

        # Handle exit button
        exitapp.click(exit_app, None, None)

    bot.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()