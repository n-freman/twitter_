from django.core.mail import send_mail

from blogposts.services import PostsFeedService


class LastPostsNotifier:

    @staticmethod
    def notify_user_about_last_posts(
        user,
        n_posts: int = 5
    ):
        posts = PostsFeedService \
                .get_posts_feed_for_user(user.id)[:n_posts]
        message = build_message(posts, user.username)
        send_mail(
            'New Posts on Feed',
            message,
            'notifications@twitter.com',
            [user.email],
            fail_silently=False,
        )


def build_message(posts, username):
    message = f'''
    Hey, {username}!
    
    We got news posts on feed for you
    '''
    for post in posts:
        message += f'\n* {post.title}'
    return message

