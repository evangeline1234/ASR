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
### 2.b) - Ping API
**📌 Question:**  
Write a ping API (i.e. http://localhost:8001/ping via GET) to return a response of “pong” to check if your service is working.

**✅ How to Run:**
```bash
python asr/ping_api.py
```
The message "Server running on http://localhost:8001" should appear. \n
Then, paste "http://localhost:8001/ping" in browser and it should show {"message": "pong"}. \n

### 2.c) - 
**📌 Question:**  
Write an API with the following specifications as a hosted inference API for the model in Task 2a. Name your file asr_api.py.
