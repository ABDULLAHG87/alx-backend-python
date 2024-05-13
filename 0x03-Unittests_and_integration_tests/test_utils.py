#!/usr/bin/env python3
"""Familiarization with utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """class for testing access_nested_map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a,"), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path,
                               expected_output):
        """method to test access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @paramertized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """method to test access_nested_map exception"""
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class to test Get Json using unittest"""
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """Method for testing get json"""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('request.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """Class for testing Memoize
    """
    def test_memoize(self):
        """Method for testing memoize"""

        class TestClass:
            """Test cases
            """
            def a_method(self):
                """method a"""
                return 42

            @memoize
            def a_property(self):
                """method for property in memoize"""
                return self.a_method()

    test_object = TestClass()

    with patch.object(test_obj, 'a_method') as mock_method:
        mock_method.return_value = 42

        result1 = test_obj.a_property
        result2 = test_obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()
