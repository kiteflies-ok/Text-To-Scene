import os
from celery import Celery
from ai_processing.document_processor import process_document

celery = Celery(__name__)
celery.conf.broker_url = os.getenv("CELERY_BROKER_URL")
celery.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND")

@celery.task(name="process_document_task")
def process_document_task(file_path: str):
    return process_document(file_path)