import unittest
import main


class Test(unittest.TestCase):
    def test_error(self):
        result = main.get_data('test.json')
        self.assertEqual(result, None)

    def test_value(self):
        result = main.get_value({"params": [{
            "id": -100,
            "title": "testcaseId",
            "value": 298
        }]})
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
