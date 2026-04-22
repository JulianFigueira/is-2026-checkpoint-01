FROM python:3.12-slim

RUN useradd -m appuser
USER appuser

WORKDIR /home/appuser/app

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

EXPOSE 5000

CMD ["python", "app.py"]