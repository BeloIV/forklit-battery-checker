from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType
from api.models import Forklift, Battery, ChargeSession

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        manager, _ = Group.objects.get_or_create(name="Manager")
        employee, _ = Group.objects.get_or_create(name="Employee")

        models = [Forklift, Battery, ChargeSession]
        perms_all = []
        perms_add_view = []
        for m in models:
            ct = ContentType.objects.get_for_model(m)
            perms_all += list(Permission.objects.filter(content_type=ct))
            perms_add_view += list(Permission.objects.filter(content_type=ct, codename__in=[
                f"add_{m._meta.model_name}", f"view_{m._meta.model_name}"
            ]))
        manager.permissions.set(perms_all)
        employee.permissions.set(perms_add_view)
        self.stdout.write("Roles created")
