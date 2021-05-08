# Use latest python3.8 Debian buster
FROM python:3.8-buster

# Home directory
WORKDIR /app/

# Copy all the files in host Workdir to Container Workdir
COPY . .

RUN chmod 777 /app/ && \
    apt-get update && \
    # This Will install missing Dependencies for Opencv to run
    apt-get install -y python3-opencv && \
    # Clean apt cache
    apt-get clean && \
    # Get the weights from the latest release
    wget -q https://github.com/viswanathbalusu/Agrothon/releases/latest/download/yolov3.weights -O /app/data/models/yolo/yolov3.weights

# Installing all the requirements
RUN pip3 -q install --no-cache-dir -r requirements.txt

# Port that was used to run the API Server
EXPOSE 10808

# Running the Container
CMD ["bash", "start.sh"]