# 🌦️ Dockerized Streamlit Weather Forecasting App

This guide helps you set up a **Weather Forecast** application inside a **Docker** container for an efficient and portable development experience. 🚀

## ✅ Prerequisites
Before setting up the environment, ensure you have the following installed on your machine:

- **🔹 Docker** 🐳 (Ensure the Docker daemon is running)
- **🔹 Python 3.9+** 🐍 (Check installation with `python --version`)
- **🔹 pip** 📦 (Ensure it's up to date with `pip --version`)
- **🔹 Basic knowledge of Streamlit** 📊

## 📂 Directory Structure
```
project_root/
│── src/
│   └── weat.py
│── Dockerfile
│── requirements.txt
│── README.md
```

## 📜 File Explanations

### 1️⃣ `.streamlit/config.toml`
This file configures **Streamlit settings** for local development.
```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

### 2️⃣ `src/weat.py`
This file contains the **core logic** of the Weather Prediction application, including:

- 🏠 **Home Page** → Introduction to the app.
- 🌡️ **Weather Forecast** → Allows users to enter a location and get weather predictions.
- 📈 **Visualization Page** → Generates interactive charts and graphs for weather trends.

### 3️⃣ `Dockerfile`
Defines the **containerized environment** for Streamlit.
```dockerfile
# Use a lightweight Python image

FROM python:3.8-slim

WORKDIR /app

# Install pip requirements
COPY requirements.txt /app
RUN python -m pip install -r requirements.txt

COPY app.py /app

EXPOSE 8501

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

```

### 4️⃣ `requirements.txt`
Contains **necessary dependencies**:
```
streamlit
pandas
numpy
matplotlib
plotly
requests  # For fetching weather data
```

## ⚡ Steps to Run the Project

### 1️⃣ **Navigate to the project directory**
```sh
cd path/to/project_root
```

### 2️⃣ **Build the Docker image**
```sh
docker build -t weather-app .
```

### 3️⃣ **Run the container**
```sh
docker run -p 8501:8501 weather-app
```

### 4️⃣ **Open in Browser**
🌐 Go to → [http://localhost:8501](http://localhost:8501)
![image](https://github.com/vansh1306/Docker_Work/blob/main/2.%20Dockerized%20Streamlit%20Development%20Environment/image.png?raw=true)

## 🎯 Conclusion
You now have a **fully functional Weather Forecast app** running inside Docker! 🚀

## 💡 Next Steps:
- 🔹 Improve the **weather prediction model**.
- 🔹 Deploy the **containerized app** on **AWS, GCP, or Azure**.
- 🔹 Experiment with **Docker Compose** for multi-container applications.

🚀 **Happy Coding!** 🐳💙

