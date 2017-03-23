import unittest
import vim_hardhat as sut


@unittest.skip("Don't forget to test!")
class VimHardhatTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_hardhat_example()
        self.assertEqual("Happy Hacking", result)
