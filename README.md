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

  ![API Docs](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/Apiserver.png)
- Telegram bot is just a frontend for the whole Project

- [Agrothon-Client](https://github.com/viswanathbalusu/Agrothon-Client) Sends Sensor data, Intruder images to the API Server which will be analysed there and Stored in the Database

## Installation
- Via **pip** 
  - Install Dependencies
    
    ```
    mkdir agrothon && cd agrothon
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install python3.8 wget
    wget -q https://github.com/caddyserver/caddy/releases/download/v2.4.1/caddy_2.4.1_linux_amd64.tar.gz
    tar xzf caddy_2.4.1_linux_amd64.tar.gz
    rm -rf caddy_2.4.1_linux_amd64.tar.gz
    chmod a+x caddy
    mv caddy /usr/local/bin/caddy
    wget -q https://github.com/viswanathbalusu/Agrothon/raw/main/Caddyfile -O Caddyfile
    ```
  - First fill the variables in `agrothon-sample.env` and rename it to `agrothon.env`
    
    ```
    wget -q https://github.com/viswanathbalusu/Agrothon/raw/main/agrothon-sample.env -O agrothon.env
    ```
  - you can extend all tha variables from [Base Config](agrothon/BaseConfig.py)
  - Get the latest [Release](https://github.com/viswanathbalusu/Agrothon/releases/latest/download/Agrothon-Data.tar.gz) of data directory and untar in it the same directory where you placed `agrothon.env`
      
      ```
      wget -q https://github.com/viswanathbalusu/Agrothon/releases/latest/download/Agrothon-Data.tar.gz
      tar -xzf Agrothon-Data.tar.gz && rm -rf Agrothon-Data.tar.gz
      ```
  - Edit the `$API_PORT` in `Caddyfile` or Just Set `$API_PORT` in your Shell Environment.
  - Then Create a Virtual Environment (Optional but Recommended) and then install Agrothon with
      
      ```
      python3.8 -m virtualenv venv
      source venv/bin/activate
      pip install Agrothon
      ```
  - There are two commands in Agrothon
    - `agroserver` - Which actually starts the Uvicorn Server on a Unix Domain Socket at `/usr/agrothon.sock`, So you should use a Reverse proxy (Preferably Caddy)
    - `agrobot` - Which starts the telegram bot
    - `agrothon` - Starts Both `agroserver` and `agrobot` with caddy reverse proxy

- Via **Docker**
   - Download [Docker compose](./docker-compose.yml) and Map the ports according to your use
      - ```wget -q https://viswanathbalusu.github.io/Agrothon/docker-compose.yml```
   - Download [agrothon.env](./agrothon-sample.env) and Fill the Variables (can be extended from [Base Config](agrothon/BaseConfig.py))
      - ```wget -q https://viswanathbalusu.github.io/Agrothon/agrothon-sample.env -O agrothon.env```
   - Finally do `docker-compose up` it will pull the image from container registry and run the services 

## Variables in `agrothon.env`

| Variable | Value | Example | Required | Description |
| :---: | :---: | :---: | :---: | :---: |
| - | - | Bot Configuration | - | - |
| TELEGRAM_APP_ID | Telegram API APP ID | 1234567 | True | Can be obtained from [Telegram](https://my.telegram.org/auth) |
| TELEGRAM_API_HASH | Telegram API Hash | 022d29afxxxxxxxxf825980a7974ec42 | True | Can be obtained from [Telegram](https://my.telegram.org/auth) |
| BOT_TOKEN | Telegram Bot Token | 123456:abcdefghij | True | Can be obtained from [Bot Father](https://t.me/botfather)
| API_BASE_URL | Api base Host URL | https://mysite.com/ | True | Must be host Without port (i.e Port 80/443* only) |
| ALERT_CHANNEL_ID | Alert channel ID | -100123456789 | True | Intruder Alerts will be posted to this channel |
| STATE | name of the state | Andhra Pradesh | True | Must be a state in India 🤔|
| DISTRICT | name of the district | East Godavari | True | name of your district |
| DEF_LANG | Default Language | english | False | Can be choosen from `english`, `telugu`, `tamil`, `hindi` (Default is `english`)|
| DEF_CITY | Default City | Vijayawada | True | City from which weather should be fetched |
| - | - | Server Configuration | - | - |
| OPEN_WEATHER_API | Open weather API Key| d6778a1acdd67c4xxxxxxe500e81987d | True | API to get the weather data of a particular region, Get this from [OpenWeather](https://openweathermap.org/api)|
| API_KEY | An API Key for your Server | Agrothon | True | This is like a Password for your API Server, So choose Wisely (Alphanumeric only) |
| DB_URL | MongoDB URL | mongodb+srv://xxx:xxx@hmmm.mongodb.net | True | Database to Store All the data, get this from [MongoDB](https://mongodb.com) |
| SENSOR_PRIORITY_INDEX | Moisture sensor priority | 2 | True | Which moisture sensor to use for predicting on/off the pump |
| AUTH_ID | Telegram user ID | 12345678 | False | If this is not provided, Bot access can is given to all the telegram users |
  
 `* if there are Other ports too the Bot will Work but it may not be able to post images`

## Note
- We are using heavy modules like tensorflow and Yolov3, so make sure you have atleast 2.5GB RAM free to get this running
- Only Works in UNIX environments
- `caddy`,`xz-utils`, all OpenCV Dependencies must be installed if you are choosing non Docker method.
- `Python3.8` is compulsory

<div align="center">
<h1>Agrothon Telegram bot</h1>
<h1>Screenshots</h1>
</div>

- Telegram Bot Start
  
  ![Start](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/telegrambot.png)

- Bot Commands
  
  ```
    start - start command
    field - get field status
    weather - get weather status
    rainfall - get predictions of rainfall for your region
    settings - change settings of the bot
    restart - restart the bot
    log - get the log files
    stats - get the server stats
    ping - check ping of server
    help - to get help message
  ```

  ![Commands](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/botcommands.png)

- Object Detection
  
  ![Bear](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/beardetect.jpg)

  ![Cow](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/cowdetect.jpg)

  ![Elephant](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/elephantdetect.jpg)

  ![Farm](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/farmdetect.jpg)

  ![Sheep](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/sheepdetect.jpg)

  ![Peacock](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/pcdetect.jpg)

- Bot Commands Usage
  
  - Pump Prediction
  
    ![Pump Prediction](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/botpredhindi.png)
  - Language Change
  
    ![Language Change](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/changelangtelugu.png)
  - Complete info
  
    ![Complete info](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/completeinfotamil.png)
  - Field Command
  
    ![Field Command](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/fieldtamil.png)
  - Help Command
  
    ![Help Command](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/helptamil.png)
  - Object Detection by sending an Image to Bot
  
    ![Object Detection Bot](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/intrudertel.png)
  - Language Menu
  
    ![Language Menu](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/langtelugu.png)
  - Pump Keyboard
    
    ![PumpKeyboard](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/pumphindi.png)

  - Pump on/off
  
    ![pump on/off](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/pumponoffhindi.png)
  - Rainfall Prediction

    ![Rainfall](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/rainfall.png)
  - Settings Keyboard

    ![Settings](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/settings.png)
  - Server Stats

    ![Stats](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/statstelugu.png)
  - Weather Data

    ![Weather](https://raw.githubusercontent.com/viswanathbalusu/Agrothon/main/images/weathertelugu.png)