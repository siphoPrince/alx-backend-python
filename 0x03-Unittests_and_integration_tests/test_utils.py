#!/usr/bin/env python3
"""unit test and integration"""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """class map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
        ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_message):
        """access map"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """test class"""
    @patch('utils.requests.get')
    @unittest.mark.parametrize("test_url, test_payload", [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, mock_get, test_url, test_payload):
        """test get jason"""
        mock_json = Mock(return_value=test_payload)
        mock_get.return_value.json = mock_json

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        test_instance = self.TestClass()

        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        mock_a_method.assert_called_once()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
if __name__ == '__main__':
    unittest.main()
