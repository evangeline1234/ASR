import os
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

asr_api_url = "http://localhost:8001/asr"
csv_file = './datasets/cv-valid-dev.csv'
audio_dir = './datasets/'

def transcribe_file(file_path):
    """Send an audio file to the ASR API and return the transcription."""
    with open(file_path, "rb") as f:
        response = requests.post(asr_api_url, files={"file": f})

    if response.status_code == 200:
        return response.json().get("transcription", "")
    else:
        return "Error"
   
def process_csv():
    if not os.path.exists(csv_file):
        print(f"CSV file not found: {csv_file}")
        return
    
    df = pd.read_csv(csv_file)
    df = df.head(10).copy()

    # Submit jobs with row index
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_index = {
            executor.submit(transcribe_file, os.path.join(audio_dir, row["filename"])): idx
            for idx, row in df.iterrows()
        }

        # Prepare empty column first
        df["generated_text"] = ""

        for future in as_completed(future_to_index):
            idx = future_to_index[future]
            try:
                transcription = future.result()
                df.at[idx, "generated_text"] = transcription
                print(f"Processed row {idx}: {df.at[idx, 'filename']}")
            except Exception as exc:
                df.at[idx, "generated_text"] = "Error"

    df["generated_text"] = df["generated_text"].str.lower()
    df.to_csv('./datasets/cv-valid-devtest123.csv', index=False)
    print("Transcription completed. CSV updated.")


if __name__ == "__main__":
    process_csv()