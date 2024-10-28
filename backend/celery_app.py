# backend/celery_app.py
from celery import Celery

def create_celery(app=None):
    """Create a Celery instance and configure it with the Flask app context."""
    celery = Celery(app.import_name if app else __name__, broker=app.config['CELERY_BROKER_URL'] if app else 'pyamqp://guest@localhost//')
    
    if app:
        celery.conf.update(app.config)
    
    return celery

# Initialize the Celery instance without the Flask app context for now
celery = create_celery()

# Optional: You can define tasks here or in separate files
@celery.task
def example_task(param):
    """An example Celery task."""
    return f"Processed {param}"
