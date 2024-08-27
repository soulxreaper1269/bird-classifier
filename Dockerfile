FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH="/app/birdVIT2.pth"

CMD [ "python", "main.py" ]
