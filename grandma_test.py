import sys
import unittest

from grandma import *

class TestGrandma(unittest.TestCase):

    def test_speak_to_grandma(self):
        self.assertEqual(speak_to_grandma("hi grandma, how are you?"), "HUH?! SPEAK UP, SONNY!")
        self.assertEqual(speak_to_grandma("Can you hear me granny?"), "HUH?! SPEAK UP, SONNY!")
        self.assertEqual(speak_to_grandma("CAN YOU HEAR ME NOW?"), "NO, NOT SINCE 1938!")

if __name__ == '__main__':
    unittest.main()
