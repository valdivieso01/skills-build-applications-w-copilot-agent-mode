from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Workout, LeaderboardEntry
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            UserProfile.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            UserProfile.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            UserProfile.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            UserProfile.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=40, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create leaderboard entries
        LeaderboardEntry.objects.create(user=users[0], team=marvel, points=100)
        LeaderboardEntry.objects.create(user=users[1], team=marvel, points=80)
        LeaderboardEntry.objects.create(user=users[2], team=dc, points=120)
        LeaderboardEntry.objects.create(user=users[3], team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
