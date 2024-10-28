# config.py
class Config:
    CELERY_BROKER_URL = 'amqp://explorer:password@localhost:5672//'
    CELERY_RESULT_BACKEND = 'rpc://'
    UPLOAD_FOLDER = 'uploads'
    