from django.db import models
from django.contrib.auth.models import Group,Permission

# Create your models here.
PERMISSIONS=[
        ('basic','Basic Perm'),
        ('Pro','Pro Perm'),
        ('advanced','Advanced Perm'),
        ('Enterprise','Enterprise Perm')
    ]

 
class Subscription(models.Model):
    name=models.CharField(max_length=20)
    groups=models.ManyToManyField(Group)
    isactive=models.BooleanField(default=True)
    permissions=models.ManyToManyField(Permission,limit_choices_to={"content_type__app_label":"subscriptions",
    "codename__in" :[x[0] for x in PERMISSIONS]                                                              })

    #Alternative->"codename__in":['basic',"pro",'advanced' etc ...]

    class Meta:
        permissions=PERMISSIONS

    def __str__(self):
        return self.name    