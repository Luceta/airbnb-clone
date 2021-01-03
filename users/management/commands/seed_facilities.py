from django.core.management.base import BaseCommand
from rooms.models import Facility

# amentiy에만 사용하기 위해 import amenity로 해줌


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
        """

    def handle(self, *args, **kwargs):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for item in facilities:
            Facility.objects.create(name=item)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))