# How to setup in your localhost
```
install Python 3.8.10 
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn --reload -w 4 --timeout 120 -k uvicorn.workers.UvicornWorker main:app       
```

# How to install python 3 in Ubuntu 20
sudo apt update
sudo apt upgrade
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8 -y

# Setup server to deploy first time

## update ubuntu 
```
    sudo apt update
```
    
## make dir
```
    mkdir coini
```

## clone repo
```
    git clone https://github.com/stacks-training/clari-ai-backend.git
```

## install pip
```
    sudo apt-get install python3-pip
```

## install python3-dev/setuptools
```
    sudo apt-get install python3-dev
    sudo apt-get install python3-setuptools
```

## install virtualenv
```
    sudo apt-get install python3-venv
```

## create virtualenv
```
    python3 -m venv coini-env
    source coini-env/bin/activate
```

## install dependences
```
    pip install -r requirements.txt
```
    
## only for deploy
```
    pip install gunicorn
```

# install nginx
```
    sudo apt-get install nginx
```

# make config
```
    nano /etc/nginx/sites-available/coini
    ln -s /etc/nginx/sites-available/coini /etc/nginx/sites-enabled
```

# config coini file:
```
server {
    server_name scraper.coini.tech;
    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

# restart nginx 
```
    service nginx restart
```


# run with gunicorn and test nginx config 
It's important to set up a higher timeout because llms take more time to return a response
```
    gunicorn --reload -w 4 --timeout 120 -k uvicorn.workers.UvicornWorker main:app       
```


# create service 
```
    sudo nano /etc/systemd/system/coini.service
```

``` 
    [Unit]
    Description=Coini Scraper

    [Service]
    WorkingDirectory=/root/coini/coini-scraper
    Enviroment="PATH=/root/coini/coini-env/bin"
    ExecStart=/root/coini/coini-env/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

    [Install]
    WantedBy=multi.user.target
```

    
# start service 
```
    service coini start
    service coini restart
    service coini status
```

# start dev service
```
    service coini-dev start
    service coini-dev restart
    service coini-dev status
```

# run local (python 3.8)
```
    pip3 install virtualenv
    virtualenv coini-env
    source coini-env/bin/activate
    copy paste requeriments.in into the terminal
    uvicorn main:app --reload
```
    

# end 

# test

[Unit]
Description=Coini Scraper

[Service]
WorkingDirectory=/root/coini/coini-scraper
Enviroment="PATH=/root/coini/coini-env/bin"
ExecStart=/root/coini/coini-env/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker --timeout 600 main:app

[Install]
WantedBy=multi.user.target


# How to setup location files for log in Gunicorn
```
vim /root/coini/gunicorn.conf.py
```

Use the following content:
```
accesslog = "/var/log/fastapi.log"
errorlog = "/var/log/fastapi.error.log"
```

Finally, update the service config file:
```
[Unit]
Description=Coini Scraper

[Service]
WorkingDirectory=/root/coini/coini-scraper
Enviroment="PATH=/root/coini/coini-env/bin"
ExecStart=/root/coini/coini-env/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker --timeout 600 --config /root/coini/gunicorn.conf.py main:app

[Install]
WantedBy=multi.user.target
```
