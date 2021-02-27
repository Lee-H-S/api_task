from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTests(TestCase):
    """
    Model Testing Class
    """

    def test_create_user_with_email(self):
        """
        Testing creating a Player Account
        """
        account_type = models.AccountType(name="Player")
        account_type.save()
        email = "test@email.com"
        display_name = "djangoboii420"
        password = "Testpassword1234"
        user = get_user_model().objects.create_user(
            email=email,
            display_name=display_name,
            password=password,
            account_type=account_type,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_game(self):
        """
        Testing creating a Game
        """
        account_type = models.AccountType(name="Studio")
        account_type.save()
        title = "Run Escape"
        studio = models.User(
            email="test@test.com",
            display_name="djangoboii420studios",
            password="testpassword1234",
            account_type=account_type,
        )
        studio.save()
        game = models.Game.objects.create(title=title, studio=studio)

        self.assertEqual(game.title, title)
        self.assertEqual(game.studio, studio)

    def test_create_subscription(self):
        """
        Testing creating a new Subscription
        """
        account_type = models.AccountType(name="Player")
        account_type.save()
        player = models.User(
            email="test@test.com",
            display_name="djangoboii420",
            password="testpassword1234",
            account_type=account_type,
        )
        player.save()
        studio = models.User(
            email="test@testagain.com",
            display_name="djangoboii420Studios",
            password="testpassword1234",
            account_type=account_type,
        )
        studio.save()
        game = models.Game.objects.create(title="Run Escape", studio=studio)
        game.save()
        sub = models.Subscription.objects.create(player=player, game=game, active=True)

        self.assertEqual(sub.player, player)
        self.assertEqual(sub.game, game)
        self.assertEqual(sub.active, True)
