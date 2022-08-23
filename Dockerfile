FROM python:3.9-slim

EXPOSE 8501

RUN apt-get update -y && apt-get install -y

COPY ./requirements.txt /requirements.txt

# Upgrade pip to latest version
RUN pip install --no-cache-dir --upgrade pip

# Install all the requirements from the requirements.txt file
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

#Copy all the files from the current folder to the /app folder
COPY . /app

WORKDIR /app

#CMD streamlit run summarize.py
CMD streamlit run --server.port $PORT app.py