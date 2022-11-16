FROM python:3.11.0

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "src/main.py"]