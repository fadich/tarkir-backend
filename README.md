# My Project

- [About the Project](#about-the-project)
    - [Rest endpoints](#rest-endpoints)
- [Local Deployment](#local-deployment)
    - [Using Docker](#using-docker)
    - [Manually](#manually)
        - [Pre-requirements](#pre-requirements)
        - [Running the Admin](#running-the-admin)
        - [Running the API](#running-the-api)
    - [Finalizing](#finalizing)
- [Production deployment](#production-deployment)
- [Built With](#built-with)

## About the Project

Some information about the project goal...

### Rest endpoints

Describe how to interact the app...

## Local Deployment

### Using Docker

You only need to have [Docker](https://docs.docker.com/engine/install/ubuntu/)
  and [Docker Compose](https://docs.docker.com/compose/install/) installed on
  your machine.

Once it's being installed, you may use `docker-compose.yml` to deploy the project
  locally, for example:
```shell script
docker-compose build
docker-compose up
```

**Note!** Depending on your configuration, sometimes the root permissions might
  be required. In this case, just run these commands with`sudo`:
```shell script
sudo docker-compose build
sudo docker-compose up
```

### Manually

#### Pre-requirements

First of all, make sure that you have already installed:
* [Docker](https://docs.docker.com/engine/install/ubuntu/);
* [Docker Compose](https://docs.docker.com/compose/install/);
* [Python 3.9](#python-39-installation);


Install pip-requirements
```shell script
pip install -r ./requirements.txt
```

##### Python 3.9 Installation

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

Once, your project is setup, up the database via docker-compose
```shell script
docker-compose up -d db
```

Optionally, activate virtual environment
```shell script
source venv/bin/activate
```

Optionally, install your project locally with:
```shell script
pip install -e .
```

#### Running the Admin

Setup environment variables
```shell script
export SANIC_ADMIN_USER='admin'
export SANIC_ADMIN_PASSWORD='123456'
```

Start application:
```shell script
python -m admin
```

#### Running the API

Start application:
```shell script
python -m api
```

### Finalizing

Well done! Now, if you've setup the project right, then:
* **Admin application** will be available on
  [0.0.0.0:4999](http://0.0.0.0:4999/);
* **REST API** will be available on [0.0.0.0:5000](http://0.0.0.0:5000/)


## Production deployment

Instruction how to deploy the project on production...

## Built With

* [Aiohttp]();
* [Alembic]();
* [Docker](https://docs.docker.com/engine/install/ubuntu/);
* [Docker Compose](https://docs.docker.com/compose/install/);
* [Gino ORM]();
* [Python]();
