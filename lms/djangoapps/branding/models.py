"""
Model used by Video module for Branding configuration.

Includes:
    BrandingInfoConfig: A ConfigurationModel for managing how Video Module will
        use Branding.
"""

import logging
import json

from config_models.models import ConfigurationModel
from django.core.exceptions import ValidationError
from django.db.models import TextField

from django.db import models
from django.contrib.auth.models import User

log = logging.getLogger(__name__)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        app_label = 'branding'

    def __str__(self):
        return self.title


class BrandingInfoConfig(ConfigurationModel):
    """
    Configuration for Branding.

    Example of configuration that must be stored:
        {
            "CN": {
                    "url": "http://www.xuetangx.com",
                    "logo_src": "http://www.xuetangx.com/static/images/logo.png",
                    "logo_tag": "Video hosted by XuetangX.com"
            }
        }

    .. no_pii:
    """
    class Meta(ConfigurationModel.Meta):
        app_label = "branding"

    configuration = TextField(
        help_text=u"JSON data of Configuration for Video Branding."
    )

    def clean(self):
        """
        Validates configuration text field.
        """
        try:
            json.loads(self.configuration)
        except ValueError:
            raise ValidationError('Must be valid JSON string.')

    @classmethod
    def get_config(cls):
        """
        Get the Video Branding Configuration.
        """
        info = cls.current()
        return json.loads(info.configuration) if info.enabled else {}


class BrandingApiConfig(ConfigurationModel):
    """Configure Branding api's

    Enable or disable api's functionality.
    When this flag is disabled, the api will return 404.

    When the flag is enabled, the api will returns the valid reponse.

    .. no_pii:
    """
    class Meta(ConfigurationModel.Meta):
        app_label = "branding"
