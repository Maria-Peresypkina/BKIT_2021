import unittest
import sys, os
from unittest.mock import patch

from features.steps import builder

sys.path.append(os.getcwd())

from features.steps.builder import *


class Clothes_Builder_Test(unittest.TestCase):
    @patch.object(builder.Clothes_Builder(), 'pullover')
    def test_pullover(self, mock_pullover):
        mock_pullover.return_value = None
        self.assertEqual(Clothes_Builder().pullover(), None)
