import os
import sys
from pathlib import Path
from django.core.asgi import get_asgi_application

repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friend_ada.settings.prod")
application = get_asgi_application()
