'''
Created on 8 Feb 2017

@author: frank
'''
import unittest

from st.parse.parseIt import ProcessParse


class TestParseIt(unittest.TestCase):

    parse = ProcessParse()
    

    def setUp(self):
        pass

    def tearDown(self):
        pass

 
    def testGetNumDays(self):
        dateStr="12 months 15 days"
        num = self.parse.getNumberOfDays(dateStr)
        print num
        self.assertTrue(num==360)
        
    def testTooLong(self):
        dateStr="12 months 15 days"
        result = self.parse.tooLong(dateStr)
        self.assertTrue(result)

        dateStr="7 days overdue now"
        result = self.parse.tooLong(dateStr)
        self.assertFalse(result)

        