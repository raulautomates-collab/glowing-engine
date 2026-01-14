from django.db import models
from django.contrib.auth.models import Group,Permission


SUBSCRIPTION_PERMISSIONS=[
            ('advanced','Advanced Permissions'),#subsricptions.advanced...
            ('Pro','Pro Permissions'),
            ('basic','Basic Permissions'),
            ('Basic Ai','Basic Ai Perm')
        ]

class Subsricption(models.Model):
    name=models.CharField(max_length=130)
    groups=models.ManyToManyField(Group)
    active=models.BooleanField(default=True)
    #correlating permissions to a group
    permissions=models.ManyToManyField(Permission,limit_choices_to={"content_type__app_label":"subscriptions",
                                                                    "codename__in":[x[0] for x in SUBSCRIPTION_PERMISSIONS]}) 
    #limit choices->limits the choices to a required set                                                              
    #meta class
    class Meta:
        permissions=[
            ('advanced','Advanced Permissions'),#subsricptions.advanced...
            ('Pro','Pro Permissions'),
            ('basic','Basic Permissions'),
            ('Basic Ai','Basic Ai Perm')
        ]