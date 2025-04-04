# ASR

## Task 1️⃣ Clone the Repository
```sh
git clone https://github.com/evangeline1234/ASR.git
cd ASR

python -m venv asr
source asr/bin/activate  # On macOS/Linux
asr\Scripts\activate  # On Windows

# Install requirements file after activating venv
pip install -r requirements.txt
```

## Task 2️⃣ 
### 2.b)
**📌 Question:**  Write a ping API (i.e. http://localhost:8001/ping via GET) to return a response of “pong” to check if your service is working.

**✅ How to Run:**
```sh
python asr/ping_api.py
```
Then, paste "http://localhost:8001/ping" in the browser and it should show {"message": "pong"}. \n

### 2.c) 
**📌 Question:**  Write an API with the following specifications as a hosted inference API for the model in Task 2a. Name your file asr_api.py.

**✅ How to Run:**
```sh
python asr/asr_api.py
```
To test the command using CURL:
```sh
curl -F "file=@/home/username/Path/To/Your/File/sample-000000.mp3" http://localhost:8001/asr
```

### 2.d) 
**📌 Question:**  Write a python file called cv-decode.py to call your API in Task 2b to transcribe the 4,076 common-voice mp3 files under cv-valid-dev folder.

**✅ How to Run:**
```sh
python asr/cv-decode.py
```

### 2.e) 
**📌 Question:**  Containerise asr_api.py using Docker. This will be in Dockerfile with the service name asr-api.

**✅ How to Run:**
```sh
docker build -t asr-api .
```

## Task 3️⃣
### 3.a)
**📌 Question:**  From Task 2d, you are to use the common-voice mp3 files under cv-valid-train and cv-valid-train.csv for finetuning train dataset.

Open Jupyter Notebook and run cv-train-2a.ipynb. \n

