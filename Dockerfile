FROM python:3.8-buster
WORKDIR /app/
COPY . .

RUN chmod 777 /app/ && \
    pip3 install -r requirements.txt && \
    wget -q https://github.com/viswanathbalusu/Agrothon/releases/latest/download/yolov3.weights -O /app/data/models/yolo/yolo.weights

EXPOSE 10808

CMD ["bash", "start.sh"]