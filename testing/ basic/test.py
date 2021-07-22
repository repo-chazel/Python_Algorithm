import unittest
import add 

class Test(unittest.TestCase):
    def check(self):
        result=add.func(5,10)
        self.assertTrue(result, 15)    

  
unittest.main() 