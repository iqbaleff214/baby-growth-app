#!/bin/bash

if [[ ! -d "frontend/node_modules" || ! -d "backend/.venv" ]]; then
    echo "Make sure you run setup script first!"
    exit 0
fi

if [[ "$OS" == "Windows_NT" ]]; then
    backend\.venv\Scripts\activate
else
    source ./backend/.venv/bin/activate
fi

npm run dev --prefix ./frontend &
uvicorn main:app --reload --app-dir ./backend

wait # Menunggu kedua proses selesai (opsional)