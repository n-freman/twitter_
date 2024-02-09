Twitter clone / Test project

## How to run

```bash
docker-compose up
```

## How to dump fake data

```bash
python manage.py shell < scripts/dump_data.py
```

## Run celery

```python
export DJANGO_SETTINGS_MODULE=core.settings && celery -A apps.interactions.celery worker --pool=solo
export DJANGO_SETTINGS_MODULE=core.settings && celery -A apps.interactions.celery beat 
```
