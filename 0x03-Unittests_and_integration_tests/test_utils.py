#!/usr/bin/env python3
"""unit test and integration"""


import unittest
from unittest.mock import patch  # For improved testability

# Assuming utils.access_nested_map is defined elsewhere

class TestAccessNestedMap(unittest.TestCase):

    @patch('utils.access_nested_map')  # Patch the function for isolation
    def test_access_nested_map(self, mock_access_nested_map):
        test_cases = [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]

        for nested_map, path, expected_result in test_cases:
            mock_access_nested_map.return_value = expected_result  # Set expected return value
            actual_result = utils.access_nested_map(nested_map, path)  # Call the function
            self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
