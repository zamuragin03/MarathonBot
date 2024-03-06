FROM python:3.11
WORKDIR /app
ENV TZ="Africa/Lusaka"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
