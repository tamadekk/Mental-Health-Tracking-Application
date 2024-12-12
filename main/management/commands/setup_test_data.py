from django.core.management.base import BaseCommand

from main.factories import UserFactory, DailyGoalFactory, MoodEntryFactory, ActivityLogFactory, TherapistFactory, UserProfileFactory
class Command(BaseCommand):
    help = 'Populates the database with fake data using Factory Boy'

    def handle(self, *args, **kwargs):
        # Create 10 fake users with associated profiles, goals, mood entries, and logs
        for _ in range(10):
            user = UserFactory()
            UserProfileFactory(user=user)

            # Create 5 fake daily goals for the user
            DailyGoalFactory.create_batch(5, user=user)

            # Create 5 fake mood entries for the user
            MoodEntryFactory.create_batch(5, user=user)

            # Create 3 fake activity logs for the user
            ActivityLogFactory.create_batch(3, user=user)

        # Create 5 fake therapists
        TherapistFactory.create_batch(5)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data using Factory Boy.'))