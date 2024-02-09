import json

from blogposts.models import Post
from django.contrib.auth import get_user_model
from interactions.models import Follow

User = get_user_model()

with open('scripts/users.json') as file:
    users_data = json.load(file)

with open('scripts/follows.json') as file:
    follows_data = json.load(file)

with open('scripts/posts.json') as file:
    posts_data = json.load(file)


for user in users_data:
    User.objects.create_user(**user)
print('[Finished dumping users]')

for follow in follows_data:
    follower, blog = follow
    try:
        Follow.objects.create(follower_id=follower, blog_id=blog)
    except Exception:
        print(follower, blog)
print('[Finished dumping followers]')

for post in posts_data:
    title, content, blog = post
    try:
        Post.objects.create(title=title, content=content, blog_id=blog)
    except Exception:
        print(title, content)
print('[Finished dumping posts]')

