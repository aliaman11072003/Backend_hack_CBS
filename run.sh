#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Export environment variables
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 