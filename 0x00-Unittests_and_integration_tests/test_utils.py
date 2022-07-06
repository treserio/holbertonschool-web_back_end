#!/usr/bin/env python3
''' Setting up unittests with mock and patch '''
from utils import access_nested_map
import unittest
import typing as typ
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    ''' access_nested_map tester '''
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: dict,
        keys: tuple,
        ret: typ.Union[int, dict]) -> None:
        ''' self explanatory test for access_nested_map '''
        self.assertEqual(access_nested_map(nested_map, keys), ret)

    @parameterized.expand([
        ({}, ('a'))
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: dict,
        keys: tuple) -> None:
        ''' test invalid keys for access_nested_map '''
        self.assertRaises(KeyError, access_nested_map, nested_map, keys)
