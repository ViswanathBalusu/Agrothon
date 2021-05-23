<div align="center">
<h1>Agrothon</h1>
<h3>A Farm Monitoring Bot</h3>
<a href="https://pypi.org/project/Agrothon"><img alt="PyPI" src="https://img.shields.io/pypi/v/Agrothon?style=for-the-badge"></a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Agrothon?style=for-the-badge">
<img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/Agrothon?style=for-the-badge">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/Agrothon?style=for-the-badge">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Agrothon?style=for-the-badge">
<a href="https://github.com/viswanathbalusu/Agrothon/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ViswanathBalusu/agrothon?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/agrothon/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ViswanathBalusu/agrothon?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/agrothon/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ViswanathBalusu/agrothon?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/agrothon/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ViswanathBalusu/agrothon?style=for-the-badge"></a>

</div>

## Introduction
- This project has three parts
   - The [Agrothon-Client](https://github.com/viswanathbalusu/Agrothon-Client) Module which will be running in Raspberry Pi
   - API Server
   - Telegram Bot
  
- API Server handles Everything, All the routes are shown below
  ![API Docs](.github/Apiserver.png?raw=true)
- Telegram bot is just a frontend for the whole Project
  ![Telegram Bot](.github/telegrambot.png)
- [Agrothon-Client](https://github.com/viswanathbalusu/Agrothon-Client) Sends Sensor data, Intruder images to the API Server which will be analysed there and Stored in the Database

## Installation
- Via **pip** 
  - First fill the variables in `agrothon-sample.env` and rename it to `agrothon.env`
  - you can extend all tha variables that are in the [Base Config](agrothon/BaseConfig.py)
  - Get the latest [Release](https://github.com/viswanathbalusu/Agrothon/releases/latest/download/Agrothon-Data.tar.gz) of data directory and untar in it the same directory where you placed `agrothon.env`
      ```
      tar -xzf Agrothon-Data.tar.gz
      ```
  - Then Create a Virtual Environment(Optional but Recommended)
      ```
      pip install Agrothon
      ```
  - There are two commands in Agrothon
    - `agroserver` - Which actually starts the Uvicorn Server on a Unix Domain Socket, So you should use a Reverse proxy (Preferably Caddy)
    - `agrothon` - Which starts the telegram bot

- Via **Docker**
   - Download [Docker compose](./docker-compose.yml) and Map the ports according to your use
      - ```wget -q https://viswanathbalusu.github.io/Agrothon/docker-compose.yml```
   - Download [agrothon.env](./agrothon-sample.env) and Fill the Variables (can be extended from [Base Config](agrothon/BaseConfig.py))
      - ```wget -q https://viswanathbalusu.github.io/Agrothon/agrothon-sample.env -O agrothon.env```
   - Finally do `docker-compose up` it will pull the image from container registry and run the services 