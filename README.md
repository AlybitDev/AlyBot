# AlyBot
A Discord Bot "Powered by AI" with which you can talk.


## Installation🚀
You have 2 methods to choose from to install AlyBot

### Method 1: Using the python3 command.
1. Clone this repository.<br>
```gh repo clone AlybitDev/AlyBot```
2. Go into the repository.<br>
```cd AlyBot```
3. In main.py change the Discord bot token, the openrouter API key and the ai model to the one you want to use.
4. Run the python3 command.<br>
```python3 main.py```

### Method 2: In a Docker Container.
1. Clone this repository.<br>
```gh repo clone AlybitDev/AlyBot```
2. Go into the repository.<br>
```cd AlyBot```
3. In main.py change the Discord bot token, the openrouter API key and the ai model to the one you want to use.
4. Build the Docker Image.<br>
```docker build -t alybot .```
5. Run the Docker Container.<br>
```docker run -d alybot```
