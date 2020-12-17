<h1>EnviroPlus</h1>
<p>
    This is based on code from the offical EnviroPlus-Python Repo found <a href="https://github.com/pimoroni/enviroplus-python">here</a><br><br>
    I had some issues with it with Rasbian Buster Lite so here's my guide, and a webserver for remote monitoring of the Pi.

<h1 align="center">
  Basic Setup
</h1>

1. Grab the Raspbian Install image, I'm using buster
2. Enable SSH and connect to wifi (I did this using a physical connection but there's a variety of other ways to do it)
3. ```sh sudo apt update ```
4. ```sh sudo apt upgrade ```
5. ```sh sudo apt-get install git ```
6. ```sh git clone https://github.com/WitheredHope/EnviroPlus```
7. ```sh cd scripts```
8. ```sh sudo ./install.sh```
9. ```sh pip3 install spidev RPi.GPIO```

<h1 align="center">
  Webserver Setup
</h1>

1. ```sh pip3 install Flask``` (this can be ignored if you're not using the webserver)
2. ```sh sudo apt-get install``` tmux (this is just a creature comfort)
3. ```sh cd webserver```
4. ```FLASK_APP=webserver.py /home/pi/.local/bin/flask run --host=0.0.0.0``` (or wherever flask installed to, I'll change this eventually)
</p> 
