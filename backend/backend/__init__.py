from __future__ import absolute_import, unicode_literals

# Asegúrate de que Celery esté siempre disponible
from .celery import app as celery_app

__all__ = ('celery_app',)