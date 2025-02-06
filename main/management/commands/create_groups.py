from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import Therapist

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        therapist_group, created = Group.objects.get_or_create(name='Therapist')
        patient_group, created = Group.objects.get_or_create(name='Patient')
        admin_group, created = Group.objects.get_or_create(name='Admin')

        # Assign permissions to groups
        content_type = ContentType.objects.get_for_model(Therapist)
        assign_permission = Permission.objects.get(codename='can_assign_patients', content_type=content_type)
        
        therapist_group.permissions.add(assign_permission)
        admin_group.permissions.add(assign_permission)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions.'))