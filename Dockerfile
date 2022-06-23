FROM python:3.10

WORKDIR /app/

COPY ./server.py /app/server.py
COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt && chmod +x server.py

# EXPOSE 8001

CMD ["python3", "-u", "./server.py"]