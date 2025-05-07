from django.test import TestCase
from django.contrib.auth.models import User
from .models import City, Category, Place, Review
from django.utils import timezone


class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a city
        self.city = City.objects.create(name='Riyadh', description='Capital city of Saudi Arabia')

        # Create a category
        self.category = Category.objects.create(name='Restaurant')

        # Create a place
        self.place = Place.objects.create(
            name='Nice Place',
            description='A very nice place to eat.',
            location='123 Street, Riyadh',
            city=self.city,
            category=self.category,
            user=self.user
        )

        # Create a review
        self.review = Review.objects.create(
            content='Great place!',
            place=self.place,
            user=self.user
        )

    # City tests
    def test_city_str(self):
        self.assertEqual(str(self.city), 'Riyadh')

    def test_city_description_blank_allowed(self):
        city2 = City.objects.create(name='Abha')
        self.assertEqual(city2.description, '')

    # Category tests
    def test_category_str(self):
        self.assertEqual(str(self.category), 'Restaurant')

    # Place tests
    def test_place_str(self):
        self.assertEqual(str(self.place), 'Nice Place')

    def test_place_city_relation(self):
        self.assertEqual(self.place.city.name, 'Riyadh')

    def test_place_category_relation(self):
        self.assertEqual(self.place.category.name, 'Restaurant')

    def test_place_user_relation(self):
        self.assertEqual(self.place.user.username, 'testuser')

    def test_place_created_at(self):
        now = timezone.now()
        self.assertLessEqual(self.place.created_at, now)

    # Review tests
    def test_review_str(self):
        self.assertEqual(str(self.review), 'Great place!')

    def test_review_place_relation(self):
        self.assertEqual(self.review.place, self.place)

    def test_review_user_relation(self):
        self.assertEqual(self.review.user, self.user)

    def test_place_review_count(self):
        self.assertEqual(self.place.reviews.count(), 1)

    def test_add_another_review(self):
        Review.objects.create(content='Second review', place=self.place, user=self.user)
        self.assertEqual(self.place.reviews.count(), 2)
