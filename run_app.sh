#!/bin/bash
uvicorn app.main:app --reload --port 8000 &
sleep 2
streamlit run app/frontend/streamlit_app.py --server.port 8501
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT 