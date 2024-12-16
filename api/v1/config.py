#!/usr/bin/python3

import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


class Config:
    """
        Config class for application settings.

        Attributes:
        ----------
            SECRET_KEY (str): The secret key for Flask application.
            JWT_SECRET_KEY (str): The secret key for JWT token encoding.
            SWAGGER (dict): A dictionary containing configuration
                            settings for Swagger UI.
                Keys:
                    - "title" (str): The title of the
                                     Swagger UI documentation.
                    - "uiversion" (int): The version of the
                                     Swagger UI interface to be used.
    """
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) 
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    SWAGGER = {
        "title": "bloodlink RESTful API",
        "uiversion": 3
    }