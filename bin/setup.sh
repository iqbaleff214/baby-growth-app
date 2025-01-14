#!/bin/bash

# FE
echo "Setting up Frontend modules..."
cd frontend

if [ ! -d "node_modules" ]; then
    echo "Installing node modules..."
    npm install
    echo "Node modules installed."
fi

echo "Frontend completed."


# BE
echo "Setting up Backend modules..."
cd ../backend

if [ -d ".venv" ]; then
    echo "Virtual environment found."
    if [[ "$OS" == "Windows_NT" ]]; then
        .venv\Scripts\activate
    else
        source .venv/bin/activate
    fi
else
    echo "Creating new virtual environment..."
    if [[ "$OS" == "Windows_NT" ]]; then
        python -m venv .venv
        .venv\Scripts\activate
    else
        python3 -m venv .venv
        source .venv/bin/activate
    fi
    echo "Virtual environment created."
    
    echo "Installing requirements"
    pip install -r requirements.txt
fi

echo "Backend completed."