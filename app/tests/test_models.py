from django.test import TestCase
from django.contrib.auth import get_user_model
from api import models

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
        email = 'test@email.com'
        password = 'Testpassword1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            account_type=account_type
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_game(self):
        """
        Testing creating a Game
        """
        account_type = models.AccountType(name="Player")
        account_type.save()
        title="Some game"
        user = models.User(
            email="test@test.com",
            password="testpassword1234",
            account_type=account_type
        )
        user.save()
        game = models.Game.objects.create(
            title=title,
            publisher_id=user
        )

        self.assertEqual(game.title, title)
        self.assertEqual(game.publisher_id, user)

    def test_create_subscription(self):
        """
        Testing creating a new Subscription
        """
        account_type = models.AccountType(name="Player")
        account_type.save()
        user = models.User(
            email="test@test.com",
            password="testpassword1234",
            account_type=account_type
        )
        user.save()
        game = models.Game.objects.create(
            title="Some game",
            publisher_id=user
        )
        game.save()
        sub = models.Subscription.objects.create(
            player=user,
            game=game,
            active=True
        )

        self.assertEqual(sub.player, user)
        self.assertEqual(sub.game, game)
        self.assertEqual(sub.active, True)