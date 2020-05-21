"""
Branding API endpoint urls.
"""


from django.conf.urls import url

from branding.views import footer, Handle_Post

urlpatterns = [
    url(r"^footer$", footer, name="branding_footer"),
    url(r'^blog/(?P<slug>[-\w]+)$', Handle_Post.as_view(), name='blog_post'),
    url(r'^blog$', Handle_Post.as_view(), name='all_posts')
]
