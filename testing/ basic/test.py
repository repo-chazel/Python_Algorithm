import unittest
import add 

class Test(unittest.TestCase):
    def test_check(self):
        result=add.func(5,10)
        self.assertTrue(result, 15)    

  
if __name__ == '__main__':
    unittest.main()