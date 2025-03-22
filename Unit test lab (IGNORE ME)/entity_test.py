import unittest
from unittest.mock import patch

from entityClass import Entity

class TestEntity(unittest.TestCase):
    """Test Suite"""

    def setUp(self):
            self.Ent = Entity()

    @patch ('bulitins.input',the_wizard = ['Wizard','throws fireballs','{}','1','100'])
    def test_CreatingWizardEntity(self):
            self.assertEqual('Wizard',Entity.name)
            self.assertEqual('throws fireballs',Entity.description)
            self.assertEqual('{}',Entity.inventory)
            self.assertEqual('1',Entity.team)
            self.assertEqual('100',Entity.hitpoints)
            



if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)