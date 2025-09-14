FROM python:3.8

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY auth.py .
COPY backup_router.py .
#COPY restore_cfg.py .

RUN mkdir -p /app/router_backups

ENTRYPOINT ["python", "backup_router.py"]
CMD ["arg1", "arg2", "arg3"]