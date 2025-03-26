# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim
WORKDIR /app
# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["streamlit", "run", "weat.py", "--server.port=8501", "--server.address=0.0.0.0"]
