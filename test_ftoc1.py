# -*- coding: utf-8 -*-
"""
test_cap.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


import unittest
import ftoc1

class Testftoc1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ftoc_positive_F(self):
        deg_f = 40.0
        result = round(ftoc1.ftoc(deg_f), 3)
        self.assertEqual(result, 4.444)
    
        f_degs = [40.0, 0.0, 32.0, 100.0, 212.0]
        c_degs = [4.444, -17.778, 0.000, 37.778, 100.000]
        
        for i,deg_f in enumerate(f_degs):
            result = round(ftoc1.ftoc(deg_f),3)
            self.assertEqual(result, c_degs[i])
    
    def test_ftoc_negative_F(self):
        deg_f = -40.0
        result = ftoc1.ftoc(deg_f)
        self.assertEqual(result, -40.0)

        f_degs = [-40.0, -0.0, -32.0, -100.0, -212.0]
        c_degs = [-40.0, -17.778, -35.556, -73.333, -135.556]
#        c_degs = [-40.0, -17.778, -35.556, -73.333, -135.55] # fails for -135.55
       
        for i,deg_f in enumerate(f_degs):
            result = round(ftoc1.ftoc(deg_f),3)
            self.assertEqual(result, c_degs[i])

if __name__ == '__main__':
    unittest.main()
