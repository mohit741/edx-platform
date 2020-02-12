""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']

LMS_BASE = 'localhost:18000'
CMS_BASE = 'localhost:18010'
SITE_NAME = LMS_BASE
LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)
LMS_INTERNAL_ROOT_URL = LMS_ROOT_URL

ECOMMERCE_PUBLIC_URL_ROOT = 'http://localhost:18130'
ECOMMERCE_API_URL = 'http://edx.devstack.ecommerce:18130/api/v2'

COMMENTS_SERVICE_URL = 'http://edx.devstack.forum:4567'

ENTERPRISE_API_URL = '{}/enterprise/api/v1/'.format(LMS_INTERNAL_ROOT_URL)

CREDENTIALS_INTERNAL_SERVICE_URL = 'http://localhost:18150'
CREDENTIALS_PUBLIC_SERVICE_URL = 'http://localhost:18150'

OAUTH_OIDC_ISSUER = '{}/oauth2'.format(LMS_ROOT_URL)

JWT_AUTH.update({
    'JWT_ISSUER': OAUTH_OIDC_ISSUER,
})

FEATURES.update({
    'AUTOMATIC_AUTH_FOR_TESTING': True,
    'ENABLE_COURSEWARE_SEARCH': False,
    'ENABLE_COURSEWARE_SEARCH_FOR_COURSE_STAFF': True,
    'ENABLE_COURSE_DISCOVERY': False,
    'ENABLE_DASHBOARD_SEARCH': False,
    'ENABLE_DISCUSSION_SERVICE': True,
    'SHOW_HEADER_LANGUAGE_SELECTOR': True,
    'ENABLE_ENTERPRISE_INTEGRATION': False,
})

ENABLE_MKTG_SITE = os.environ.get('ENABLE_MARKETING_SITE', False)
MARKETING_SITE_ROOT = os.environ.get('MARKETING_SITE_ROOT', 'http://localhost:8080')

MKTG_URLS = {
    'ABOUT': '/about',
    'ACCESSIBILITY': '/accessibility',
    'AFFILIATES': '/affiliate-program',
    'BLOG': '/blog',
    'CAREERS': '/careers',
    'CONTACT': '/support/contact_us',
    'COURSES': '/course',
    'DONATE': '/donate',
    'ENTERPRISE': '/enterprise',
    'FAQ': '/student-faq',
    'HONOR': '/edx-terms-service',
    'HOW_IT_WORKS': '/how-it-works',
    'MEDIA_KIT': '/media-kit',
    'NEWS': '/news-announcements',
    'PRESS': '/press',
    'PRIVACY': '/edx-privacy-policy',
    'ROOT': MARKETING_SITE_ROOT,
    'SCHOOLS': '/schools-partners',
    'SITE_MAP': '/sitemap',
    'TRADEMARKS': '/trademarks',
    'TOS': '/edx-terms-service',
    'TOS_AND_HONOR': '/edx-terms-service',
    'WHAT_IS_VERIFIED_CERT': '/verified-certificate',
}

ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS = {}

CREDENTIALS_SERVICE_USERNAME = 'credentials_worker'

COURSE_CATALOG_API_URL = 'http://localhost:18381/api/v1/'

# Uncomment the lines below if you'd like to see SQL statements in your devstack LMS log.
# LOGGING['handlers']['console']['level'] = 'DEBUG'
# LOGGING['loggers']['django.db.backends'] = {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False}

SYSTEM_WIDE_ROLE_CLASSES = os.environ.get("SYSTEM_WIDE_ROLE_CLASSES", SYSTEM_WIDE_ROLE_CLASSES)
SYSTEM_WIDE_ROLE_CLASSES.extend(['system_wide_roles.SystemWideRoleAssignment'])

if FEATURES['ENABLE_ENTERPRISE_INTEGRATION']:
    SYSTEM_WIDE_ROLE_CLASSES.extend(['enterprise.SystemWideEnterpriseUserRoleAssignment'])

########################## THEMING  #######################
# If you want to enable theming in devstack, uncomment this section and add any relevant
# theme directories to COMPREHENSIVE_THEME_DIRS

# We have to import the private method here because production.py calls
# derive_settings('lms.envs.production') which runs _make_mako_template_dirs with
# the settings from production, which doesn't include these theming settings. Thus,
# the templating engine is unable to find the themed templates because they don't exist
# in it's path. Re-calling derive_settings doesn't work because the settings was already
# changed from a function to a list, and it can't be derived again.

# from .common import _make_mako_template_dirs
# ENABLE_COMPREHENSIVE_THEMING = True
# COMPREHENSIVE_THEME_DIRS = [
#     "/edx/app/edxapp/edx-platform/themes/"
# ]
# TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
# derive_settings(__name__)
