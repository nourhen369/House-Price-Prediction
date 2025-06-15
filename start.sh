#!/bin/bash

# FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Streamlit
streamlit run front.py --server.port=8501