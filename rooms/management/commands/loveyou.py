from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me "

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do you want tell you")

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.WARNING("I love you"))
