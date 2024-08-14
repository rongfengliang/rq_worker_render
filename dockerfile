FROM python:3.11-slim
WORKDIR /app
COPY task.py  /app/task.py
COPY callback.py /app/callback.py
COPY app.py /app/app.py
ENV REDIS_URL redis://redis:6379/0
ENV region  beijing
COPY entrypoint.sh /app/entrypoint.sh
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt && chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]