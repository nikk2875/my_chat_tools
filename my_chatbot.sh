#!/bin/bash

# Check if virtual environment exists
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_PATH="$SCRIPT_DIR/venv"

if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found. Please run install.sh first."
    exit 1
fi

# Check which Python script to run
PYTHON_SCRIPT="${1:-chatbot.py}"
if [ ! -f "$SCRIPT_DIR/$PYTHON_SCRIPT" ]; then
    echo "Error: Python script $PYTHON_SCRIPT not found in $SCRIPT_DIR"
    exit 1
fi

# Activate the virtual environment
echo "Starting chatbot using virtual environment from $VENV_PATH"
source "$VENV_PATH/bin/activate"

# Run the Python script
echo "Running $PYTHON_SCRIPT..."
python "$PYTHON_SCRIPT"

# Deactivate the virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment was not activated properly."
else
    deactivate
    echo "Virtual environment deactivated."
fi