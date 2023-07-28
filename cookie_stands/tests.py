from django.test import TestCase

# Create your tests here.

class cookie_standsTests(TestCase):
    # TODO: test your app
    def test_your_app(self):
        self.assertEqual("I have many tests", "I have no tests")

    def test_database_engine_config(self):
        from django.conf import settings
        database_engine = settings.DATABASES["default"]["ENGINE"]
        self.assertEqual(database_engine, "django.db.backends.postgresql")

    def test_database_connection(self):
        from django.db import connection
        self.assertTrue(connection.is_usable())

    def test_database_table_existence(self):
        from django.db import connection
        table_names = connection.introspection.table_names()
        self.assertIn("django_migrations", table_names)  # Change "django_migrations" to the table you expect to exist
