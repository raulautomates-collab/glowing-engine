from typing import Any
from django.core.management.base import BaseCommand
from SUBSCRIPTIONS.models import *


class Command(BaseCommand):#sync subs function
    
    def handle(self, *args: Any, **options: Any):
        print('Homie ,you trippin,gay ass motherfuc**er')
        my_queryset=Subsricption.objects.filter(active=True)
        for object in my_queryset:
            print(object.groups.all())
            print(object.permissions.all())
            for group in object.groups.all():
                for perm in object.permissions.all():
                    group.permissions.add(perm)