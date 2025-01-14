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
    source .venv/bin/activate
else
    echo "Creating new virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Virtual environment created."
    echo "Installing requirements"
    pip install -r requirements.txt
fi

echo "Backend completed."