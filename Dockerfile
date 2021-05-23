# Use latest python3.8 Debian buster Slim
FROM python:3.8-slim

# Home directory
WORKDIR /app/

RUN chmod 777 /app/ && \
    apt-get update && \
    # This Will install missing Dependencies for Opencv to run
    apt-get install -y python3-opencv wget unzip wget xz-utils tar && \
    # Clean apt cache and Unused Packages
    apt-get -y autoremove && rm -rf /var/lib/apt/lists/* && apt-get clean  && \
    # Install Caddy
    wget -q https://github.com/caddyserver/caddy/releases/download/v2.4.1/caddy_2.4.1_linux_amd64.tar.gz -O cad.tar.gz && tar xzf cad.tar.gz && \
    rm -rf cad.tar.gz && chmod a+x caddy && mv caddy /usr/bin/caddy && \
    # Get Data From Releases
    wget -q https://github.com/viswanathbalusu/Agrothon/releases/latest/download/Agrothon-Data.tar.gz && \
    tar -xzf Agro*.tar.gz && rm -rf Agro*.tar.gz && \
    wget -q https://github.com/viswanathbalusu/Agrothon/raw/main/server.sh && chmod a+x server.sh && \
    wget -q https://github.com/viswanathbalusu/Agrothon/raw/main/Caddyfile -O /Caddyfile
# Installing all the requirements
RUN pip3 -q --no-cache-dir install Agrothon

# Running the Container
CMD ["bash", "server.sh"]