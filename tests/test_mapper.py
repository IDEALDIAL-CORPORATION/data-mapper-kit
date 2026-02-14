import unittest
from src.mapper import DataMapper
class TestDataMapper(unittest.TestCase):
    def setUp(self) -> None:
        self.mapping = {'name': 'full_name', 'age': 'years'}
        self.mapper = DataMapper(self.mapping)

    def test_map_data(self) -> None:
        input_data = {'name': 'Alice', 'age': 25}
        expected_output = {'full_name': 'Alice', 'years': 25}
        result = self.mapper.map_data(input_data)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()
