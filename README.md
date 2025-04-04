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

*To Note: Download the dataset from https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&dl=0 and upload into "datasets" folder for use.

## Task 2️⃣ 
### 2.b)
**📌 Question:**  Write a ping API (i.e. http://localhost:8001/ping via GET) to return a response of “pong” to check if your service is working.

**✅ How to Run:**
```sh
python asr/ping_api.py
```
Then, paste "http://localhost:8001/ping" in the browser and it should show {"message": "pong"}.

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
## Note: For the fine-tuning task, due to limited computational resources (GPU) and time, I only used 10,000 training audio samples for fine-tuning.

### 3.a)
**📌 Question:**  From Task 2d, you are to use the common-voice mp3 files under cv-valid-train and cv-valid-train.csv for finetuning train dataset.

**Open Jupyter Notebook and run cv-train-2a.ipynb.**

## Task 5️⃣
### 5.a)
**📌 Question:**  Using the transcribed results from cv-valid-dev mp3 dataset using your finetuned model in task 4, the hot words to be detected are: “be careful”, “destroy” and “stranger”. Save the list of mp3 filenames with the hot words detected into detected.txt.

**Open Jupyter Notebook and run cv-hotword-5a.ipynb.**

### 5.b)
**📌 Question:**  Using the text embedding model, write a python jupyter notebook called cv-hotword-similarity-5b.ipynb to find similar phrases to the 3 hot words in task 5a.

**Open Jupyter Notebook and run cv-hotword-similarity-5b.ipynb**
