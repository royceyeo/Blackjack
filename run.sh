#!/bin/bash

set -e

VENV_DIR=".venv"
PYTHON_FILE="main.py"

# Detect if we are on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    PYTHON_EXEC="python"  # Windows often uses `python` instead of `python3`
    ACTIVATE_SCRIPT="$VENV_DIR/Scripts/activate"  # Path for Git Bash on Windows
else
    PYTHON_EXEC="python3"  # For Linux/macOS
    ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"
fi

# Check if Python is installed
if ! command -v "$PYTHON_EXEC" &> /dev/null; then
    echo "Python3 (or python) is not installed. Attempting to install..."
    
    # Attempt to use `apt` or other package managers if on Linux
    if command -v apt &> /dev/null; then
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-venv python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3 python3-venv python3-pip
    else
        echo "Python installation not found. Please install it manually."
        exit 1
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    $PYTHON_EXEC -m venv "$VENV_DIR"
fi

# Activate virtual environment
if [ -f "$ACTIVATE_SCRIPT" ]; then
    echo "Activating virtual environment..."
    source "$ACTIVATE_SCRIPT"
else
    echo "Activation script not found: $ACTIVATE_SCRIPT"
    exit 1
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    $PYTHON_EXEC -m pip install --upgrade pip
    pip install -r requirements.txt || { echo "Failed to install dependencies"; deactivate; exit 1; }
else
    echo "requirements.txt not found!"
    deactivate
    exit 1
fi

# Run Python script
if [ -f "$PYTHON_FILE" ]; then
    echo "Running $PYTHON_FILE..."
    $PYTHON_EXEC "$PYTHON_FILE"
else
    echo "$PYTHON_FILE not found!"
    deactivate
    exit 1
fi

# Deactivate virtual environment
deactivate
