import unittest
import vim_hardhat as sut

class VimHardhatTests(unittest.TestCase):

    def test_matching(self):
        self.assertEqual(None, sut.find_test_case_name(""))
        self.assertEqual("my_helmet_test_case_1", sut.find_test_case_name("TEST_CASE(my_helmet_test_case_1)\n"))
        self.assertEqual("my_helmet_test_case_2", sut.find_test_case_name(" \t TEST_CASE(my_helmet_test_case_2 \t , \t some_other_thing \t ) \t { \t \n"))
        self.assertEqual("my_helmet_test_case_with_base_3", sut.find_test_case_name("TEST_CASE_WITH_BASE(MyFixture, my_helmet_test_case_with_base_3)\n"))
        self.assertEqual("my_helmet_test_case_with_base_4", sut.find_test_case_name(" \t TEST_CASE_WITH_BASE \t ( \t BaseFixture \t , \t my_helmet_test_case_with_base_4 \t , \t some_other_thing \t ) \t { \t \n"))

    def test_find_helmet_test_case_under_cursor(self):
        self.assertEqual("my_helmet_test", sut.find_test_case_under_cursor(["TEST_CASE(my_helmet_test)"]))

        lines = "some C++ code\n"
        lines += "TEST_CASE(my_helmet_test_case_1)\n"
        lines +=  "{\n"
        lines += "    ASSERT_EQUALS(1, 0);\n"
        lines += "    ASSERT_EQUALS(1, 0);\n"
        lines +=  "}\n"
        lines +=  "\n"
        lines += "TEST_CASE_WITH_BASE(MY_BASE, my_helmet_test_case_2, additional, junk)\n"
        lines +=  "{\n"
        lines += "    ASSERT_EQUALS(1, 0);\n"
        lines += "    ASSERT_EQUALS(1, 0);\n"
        lines +=  "}\n"
        lines = lines.split("\n")

        for n in range(1,7):
            l = lines[0:n + 1]
            self.assertEqual("my_helmet_test_case_1", sut.find_test_case_under_cursor(l))

        for n in range(8,15):
            l = lines[0:n + 1]
            self.assertEqual("my_helmet_test_case_2", sut.find_test_case_under_cursor(l))
