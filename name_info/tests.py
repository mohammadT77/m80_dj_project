from django.test import TestCase

# Create your tests here.
from name_info.utils import *


class UtilsTest(TestCase):

    def test_get_name_age_info(self):
        print("Age of Akbar:",get_age("Akbar"))
        print("Gender of Akbar:",get_gender("Akbar"))
        print("Nationality of Akbar:", get_nationalities("Akbar"))