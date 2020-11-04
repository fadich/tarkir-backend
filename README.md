# My Project

## Pre-requirements

First of all, make sure that you have already installed:
* [Docker](https://docs.docker.com/engine/install/ubuntu/);
* [Docker Compose](https://docs.docker.com/compose/install/);
* [Python 3.9](#python-39-installation);


Install pip-requirements
```shell script
pip install -r ./requirements.txt
```

### Python 3.9 Installation

Install OS tools (optional)
```shell script
sudo apt update 
sudo apt install wget software-properties-common
```

Install Python3.9
```shell script
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update 
sudo apt install python3.9 
```

Install Python tools (optional)
```shell script
sudo apt install \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3.9-distutils \
    python3.9-dev \ 
    python3-pip \
    virtualenv
```

Create virtualenv (optional)
```shell script
virtualenv -p python3.9 venv
source venv/bin/activate
```

## Local Deployment

Once, your project is setup, up the database via docker-compose
```shell script
docker-compose up -d db
```

Install your project locally with:
```shell script
pip install -e .
```

### Running the Admin

Setup environment variables
```shell script
export SANIC_ADMIN_USER='admin'
export SANIC_ADMIN_PASSWORD='123456'
```


## Built With

* [Aiohttp]();
* [Docker](https://docs.docker.com/engine/install/ubuntu/);
* [Docker Compose](https://docs.docker.com/compose/install/);
* [Gino ORM]();
* [Python]();
