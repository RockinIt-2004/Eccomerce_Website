import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

from eccom.settings import BASE_DIR

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
