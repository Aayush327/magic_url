
from celery.decorators import task
from celery.utils.log import get_task_logger


from endpoint import (
    models as endpoint_models,
    utils as endpoint_utils
)

logger = get_task_logger(__name__)

@task()
def delete_expired_urls():
    """
    Task to delete the Expired url.
    """
    # Update is_expired field of url
    endpoint_utils.update_expiry_of_urls()
    
    # Delete expired urls
    endpoint_models.Url.objects.filter(is_expired=True).delete()
