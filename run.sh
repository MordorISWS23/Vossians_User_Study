#!/bin/bash

cd /opt/vossians
source /opt/vossians/venv/bin/activate
streamlit run introduction.py --sever.port=8501 --server.address=127.0.0.1
