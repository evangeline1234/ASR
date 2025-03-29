FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements.txt into working directory
COPY requirements.txt /app/


# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy asr directory
COPY asr/ /app/asr/


# Expose the port that FastAPI will run on
EXPOSE 8001

# Command to run FastAPI app
CMD ["uvicorn", "asr.asr_api:app", "--host", "0.0.0.0", "--port", "8001"]
