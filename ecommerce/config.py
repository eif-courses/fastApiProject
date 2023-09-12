import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 't3ryKxwsbyGGjveU8dWE')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'containers-us-west-144.railway.app:6560')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'railway')
