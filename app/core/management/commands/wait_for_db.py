import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Pausing execution until the database is available
    """

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for db...")
        conn = None
        while not conn:
            try:
                conn = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database available!"))
            except OperationalError:
                self.stdout.write("Database still unavailable...")
                time.sleep(1)
