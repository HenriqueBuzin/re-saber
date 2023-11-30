# develop stage
FROM python:3.11-slim as develop-stage
WORKDIR /resaber
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "run.py" ]

# production stage
FROM python:3.11-slim as production-stage
WORKDIR /resaber
COPY requirements.txt ./
RUN apt-get update && apt-get install -y openssl && \
    pip install --no-cache-dir -r requirements.txt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .
CMD ["/bin/sh", "-c", "export SECRET_KEY=$(openssl rand -hex 32) && gunicorn run:app -w 4 -b 0.0.0.0:5000"]
