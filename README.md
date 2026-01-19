# web-factory (2 sites demo)

Monorepo with shared Django apps and two separate Django projects ("sites"):

- sites/friend_ada
- sites/friend_boris

Each site can be deployed as its own service (Railway/Render). Shared apps live in `shared/`.

## Quick start (local)
Create venv, install deps:
- `python -m venv .venv`
- activate venv
- `pip install -r requirements.txt`

Run Ada:
- `python sites/friend_ada/manage.py migrate`
- `python sites/friend_ada/manage.py createsuperuser`
- `python sites/friend_ada/manage.py runserver`

Run Boris (port 8001):
- `python sites/friend_boris/manage.py migrate`
- `python sites/friend_boris/manage.py createsuperuser`
- `python sites/friend_boris/manage.py runserver 8001`

## Notes
- In production you should use Postgres and an object storage (S3-compatible) for uploaded images.
- For demo purposes, SQLite + local MEDIA are used.
