import CSVCombiner
import unittest
import os


class TestCombiner(unittest.TestCase):

    def test_invalid_input(self):
        combiner = CSVCombiner.CSVCombiner()
        result = combiner.parseArgs(["invalidFile", "invalid File"])
        self.assertEqual(result, False)

    def test_invalid_input_combine_igonred(self):
        combiner = CSVCombiner.CSVCombiner()
        combiner.parseArgs(["invalidFile", "invalid File"])
        result = combiner.combine()
        self.assertEqual(result, False)

    def test_valid_input(self):
        combiner = CSVCombiner.CSVCombiner()
        result = combiner.parseArgs(["filename", "fixtures/accessories.csv", "fixtures/clothing.csv"])
        self.assertEqual(result, True)

    def test_valid_input_combine(self):
        combiner = CSVCombiner.CSVCombiner()
        combiner.parseArgs(["filename", "fixtures/accessories.csv", "fixtures/clothing.csv"])
        result = combiner.combine()
        self.assertEqual(result, True)
        os.remove("combined/accessories-clothing")


    def test_combine_file_created(self):
        combiner = CSVCombiner.CSVCombiner()
        combiner.parseArgs(["filename", "fixtures/accessories.csv", "fixtures/clothing.csv"])
        combiner.combine()
        self.assertTrue(os.path.exists("combined/accessories-clothing"))
        os.remove("combined/accessories-clothing")


    
if __name__ == '__main__':
    unittest.main()