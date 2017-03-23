from unittest import TestCase
import os
from crawler.settings import IMAGES_STORE


class TestImageDirectory(TestCase):
    def test(self):
        assert os.path.exists(IMAGES_STORE)
