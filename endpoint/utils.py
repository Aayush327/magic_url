from datetime import timedelta

from django.utils import timezone

from endpoint import (
    constants as endpoint_constants,
    models as endpoint_models
)

def update_expiry_of_urls():
    """
    
    """
    endpoint_models.Url.objects.filter(
        created_at__lte=timezone.now() - timedelta(seconds=endpoint_constants.URL_EXPIRY_TIME_IN_SECONDS)
    ).update(is_expired=True)
