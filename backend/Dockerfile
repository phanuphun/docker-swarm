FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir bottle paste
EXPOSE 8081
CMD ["python", "app.py"]