import unittest
class item:
    def __init__(self,name, desc, uses, dmg):
        """create name, description, damage for an item"""
        self.name = name
        self.desc = desc
        self.uses = uses
        self.dmg = dmg

    def use(self):
        """tbd"""
        if rock.uses > 0:
            return(True)
        else:
            return(False)
        
rock = item('rock', 'oogabooga', 1, 5)

class TestItem(unittest.TestCase):

    def test_use_item_rock_expect_attack(self):
        self.assertEqual(True, rock.use())
    def test_use_item_rock_expect_fail(self):
        self.assertEqual(False, rock.use())

if __name__ == '__main__':
    #this will not run due to unittest looking for 
    #sys.argv which is used in jupyter app under test
    #unittest.main() 
    unittest.main(argv=['first-arg-is-ignored'], exit=False)