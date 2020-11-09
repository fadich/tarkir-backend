from .app import app

from tarkir import config


if __name__ == '__main__':
    app.run_app(
        host=config.api_server_host,
        port=config.api_server_port)
