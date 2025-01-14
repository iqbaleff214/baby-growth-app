#!/bin/bash

source ./backend/.venv/bin/activate

npm run dev --prefix ./frontend &
uvicorn main:app --reload --app-dir ./backend

wait # Menunggu kedua proses selesai (opsional)