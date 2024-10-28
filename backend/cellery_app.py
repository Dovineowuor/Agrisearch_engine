from celery import Celery

def create_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

@celery.task
def process_media_async(audio_path):
    # Task to process media asynchronously
    # Implement embedding generation and storage in ChromaDB here
    pass
