from typing import Any
from django.core.management.base import BaseCommand
from subscriptions.models import Subscription

class Command(BaseCommand):#syn subscriptions functions
    
    def handle(self, *args: Any, **options: Any):
        print('Homie ,you trippin,gay ass motherfuc**er')
        mysubs=Subscription.objects.filter(isactive=True)
        for sub in mysubs:
            print(sub.groups.all())
            print(sub.permissions.all())