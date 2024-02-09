from concurrent.futures import ThreadPoolExecutor

from django.contrib.auth import get_user_model
from celery import shared_task

from interactions.services import LastPostsNotifier

User = get_user_model()


@shared_task
def notify_all_users():
    print('Users count is')
    with ThreadPoolExecutor(16) as executor:
        users = User.objects.all()
        executor.map(
            LastPostsNotifier.notify_user_about_last_posts,
            users
        )

