import unittest
from unittest.mock import patch

from entityClass import Entity





class TestEntity(unittest.TestCase):
    """Test Suite"""

    def setUp(self):
            self.Ent = Entity()

    @patch (bulitins.input)
    def test_CreatingWizardEntity(self):
            self.assertEqual('Wizard',Wizard.name)



if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)