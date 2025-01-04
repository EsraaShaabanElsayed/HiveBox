FROM python:3.10.12
WORKDIR /app

COPY requirements.txt ./

RUN pip install   --no-cache-dir -r requirements.txt
COPY main.py .
# Create a non-root user and switch to it
RUN adduser --disabled-password appuser
USER appuser

CMD [ "python3","main.py" ]

EXPOSE 5000
# Healthcheck to ensure the container is healthy
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl --fail http://localhost:5000/ || exit 1
