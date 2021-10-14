from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['register', 
        'profile', 
        'login',
        'logout',
        # 'password_reset',
        # 'password_reset_done',
        # 'password_reset_confirm',
        # 'password_reset_complete',
        'firsthome',
        'blog-home',
        'posts-follow-view',
        'user-posts',
        'post-detail',
        'post-update',
        'post-delete',
        'post-create',
        'post-like',
        'all-like',
        'post-save',
        'all-save',
        'comment-like',
        'blog-about',
        'search',
        # chat 
        'room-enroll',
        'room-choice',
        'room',
        # user 
        'profile-list-view',
        'follow-unfollow-view',
        'profile-detail-view',
        'public-profile',
        # notification 
        'show-notifications',
        # friends 
        'list',
        'friend-request',
        'friend-requests',
        'friend-request-accept',
        'remove-friend',
        'friend-request-decline',
        'friend-request-cancel']

        # 'notifications',
        # 'chats',
        # 'friend'

    def location(self, item):
        return item