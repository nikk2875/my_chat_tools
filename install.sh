#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 could not be found. Please install Python3 first."
    exit 1
fi

# Check if virtualenv is installed
if ! python3 -m pip show virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing virtualenv..."
    python3 -m pip install virtualenv
fi

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Create virtual environment
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Creating virtual environment in $SCRIPT_DIR/venv"
    python3 -m virtualenv "$SCRIPT_DIR/venv"
 else
    echo "Virtual environment already exists in $SCRIPT_DIR/venv"
fi

# Activate the virtual environment and install dependencies
echo "Installing dependencies from requirements.txt"
source "$SCRIPT_DIR/venv/bin/activate"
pip install -r "$SCRIPT_DIR/requirements.txt"

echo "Installation complete. To activate the virtual environment, run:"
echo "source $SCRIPT_DIR/venv/bin/activate"