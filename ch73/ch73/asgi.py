"""
ASGI config for ch73 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ch73.settings')

application = ASGIStaticFilesHandler(get_asgi_application())
