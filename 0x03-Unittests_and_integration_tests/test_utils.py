#!/usr/bin/env python3
"""Familiarization with utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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
