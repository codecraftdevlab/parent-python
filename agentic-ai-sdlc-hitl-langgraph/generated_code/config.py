"""
Configuration file for the application
"""

import os

class Config:
    """
    Base configuration class
    """
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DATABASE_URI')
    SPRING_BOOT_VERSION = '4'

class DevelopmentConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration class
    """
    TESTING = True

class ProductionConfig(Config):
    """
    Production configuration class
    """
    pass