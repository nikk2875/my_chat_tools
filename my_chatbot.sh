#!/bin/bash

# Define the directory where the code will be executed.
# It is assumed that you have already installed the code with install.sh.
# This script should exist on the parent folfer of the installation. 
SCRIPT_DIR="`pwd`/My_Chatbot"


# Run the Python script
PYTHON_SCRIPT="my_chatbot.py"
echo "Running $PYTHON_SCRIPT..."
cd $SCRIPT_DIR/
uv run python "$PYTHON_SCRIPT"