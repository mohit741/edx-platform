"""
URLs for static_template_view app
"""


from django.conf import settings
from django.conf.urls import url, include
from branding.views import Handle_Post, Notification_Post, BlogSearchView
from static_template_view import views

urlpatterns = [
    # Semi-static views (these need to be rendered and have the login bar, but don't change)
    url(r'^404$', views.render, {'template': '404.html'}, name="404"),
    # display error page templates, for testing purposes
    url(r'^404$', views.render_404, name='static_template_view.views.render_404'),
    url(r'^500$', views.render_500, name='static_template_view.views.render_500'),

    # Blog Posts and notifications handling in single url and view -mohit741
    url(r'^blog$', Handle_Post.as_view(), name="blog"),
    url(r'^notifications$', Notification_Post.as_view(), name="notify"),
    url(r'^messages/', include('messages_extends.urls')),
    url(r'^blog_search/', BlogSearchView.as_view(), name='blog_search'),

    url(r'^contact$', views.render, {'template': 'contact.html'}, name="contact"),
    url(r'^donate$', views.render, {'template': 'donate.html'}, name="donate"),
    url(r'^faq$', views.render, {'template': 'faq.html'}, name="faq"),
    url(r'^help$', views.render, {'template': 'help.html'}, name="help_edx"),
    url(r'^jobs$', views.render, {'template': 'jobs.html'}, name="jobs"),
    url(r'^news$', views.render, {'template': 'news.html'}, name="news"),
    url(r'^press$', views.render, {'template': 'press.html'}, name="press"),
    url(r'^media-kit$', views.render, {'template': 'media-kit.html'}, name="media-kit"),
    url(r'^copyright$', views.render, {'template': 'copyright.html'}, name="copyright"),
    url(r'^access_till_pass$', views.render, {'template': 'access_till_pass.html'}, name="access_till_pass"),
    url(r'^complete_study_material$', views.render, {'template': 'complete_study_material.html'}, name="complete_study_material"),
    url(r'^doubt_clear$', views.render, {'template': 'doubt_clear.html'}, name="doubt_clear"),
    url(r'^lecture_videos$', views.render, {'template': 'lecture_videos.html'}, name="lecture_videos"),
    url(r'^mock_tests$', views.render, {'template': 'mock_tests.html'}, name="mock_tests"),
    url(r'^question_bank$', views.render, {'template': 'question_bank.html'}, name="question_bank"),
    url(r'^sample_paper$', views.render, {'template': 'sample_paper.html'}, name="sample_paper"),
    url(r'^study_planner$', views.render, {'template': 'study_planner.html'}, name="study_planner"),
    url(r'^tp1$', views.render, {'template': 'tp1_info.html'}, name="tp1"),
    url(r'^tp2$', views.render, {'template': 'tp2_info.html'}, name="tp2"),
    url(r'^instructors_profile$',views.render,{'template' : 'instructors_profile.html'},name="instructors_profile"),
    url(r'^about_mf$',views.render,{'template' : 'about_mf.html'},name="about_mf"),
    url(r'^our_expertise$',views.render,{'template' : 'our_expertise.html'},name="our_expertise"),
    # Press releases
    url(r'^press/([_a-zA-Z0-9-]+)$', views.render_press_release, name='press_release'),
]

# Only enable URLs for those marketing links actually enabled in the
# settings. Disable URLs by marking them as None.
for key, value in settings.MKTG_URL_LINK_MAP.items():
    # Skip disabled URLs
    if value is None:
        continue

    # These urls are enabled separately
    if key == "ROOT" or key == "COURSES":
        continue

    # The MKTG_URL_LINK_MAP key specifies the template filename
    template = key.lower()
    if '.' not in template:
        # Append STATIC_TEMPLATE_VIEW_DEFAULT_FILE_EXTENSION if
        # no file extension was specified in the key
        template = "%s.%s" % (template, settings.STATIC_TEMPLATE_VIEW_DEFAULT_FILE_EXTENSION)

    # Make the assumption that the URL we want is the lowercased
    # version of the map key
    urlpatterns.append(url(r'^%s$' % key.lower(), views.render, {'template': template}, name=value))
