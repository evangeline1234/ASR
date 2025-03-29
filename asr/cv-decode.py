import os
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


asr_api_url = "http://localhost:8001/asr"
proj_dir = r"C:\Users\evann\Documents\GitHub\ASR"
csv_file = os.path.join(proj_dir, "datasets", "cv-valid-dev.csv")


def transcribe_file(file_path):
    """Send an audio file to the ASR API and return the transcription."""
    with open(file_path, "rb") as f:
        response = requests.post(asr_api_url, files={"file": f})

    if response.status_code == 200:
        return response.json().get("transcription", "")
    else:
        return "Error"
   
def process_csv():
    """Read cv-valid-dev.csv, transcribe each MP3 file, and save results."""
    if not os.path.exists(csv_file):
        print(f"CSV file not found: {csv_file}")
        return
    
    df = pd.read_csv(csv_file)
    df_test = df.head(10)
    file_paths = [
        os.path.join(proj_dir, "datasets", row["filename"]) for _, row in df_test.iterrows()
    ]
    transcriptions = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_file = {executor.submit(transcribe_file, file_path): file_path for file_path in file_paths}

        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                transcription = future.result()
                transcriptions.append(transcription)
                print(f"Processed: {file_path}")
            except Exception as exc:
                print(f"Error processing {file_path}: {exc}")
                transcriptions.append("Error")

    # Add generated text to DataFrame
    df_test["generated_text"] = transcriptions
    df_test.to_csv("df_test", index=False)
    print("Transcription completed. CSV updated.")



if __name__ == "__main__":
    process_csv()