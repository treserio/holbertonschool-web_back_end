#!/usr/bin/env python3
''' Setting up unittests with mock and patch '''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch
import typing as typ
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(TestCase):
    ''' access_nested_map tester '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: dict,
        keys: tuple,
        ret: typ.Union[int, dict]
    ) -> None:
        ''' test access_nested_map with valid keys in nested_map '''
        self.assertEqual(access_nested_map(nested_map, keys), ret)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: dict,
        keys: tuple
    ) -> None:
        ''' test access_nested_map with invalid keys '''
        self.assertRaises(KeyError, access_nested_map, nested_map, keys)


class TestGetJson(TestCase):
    ''' get_json tester '''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, url: str, json: dict) -> None:
        ''' test get_json with mock.patch requests.get '''
        with patch('requests.get') as m_g:
            m_g.return_value.json.return_value = json
            self.assertEqual(get_json(url), json)


class TestMemoize(TestCase):
    ''' memoize function tester '''
    def test_memoize(self):
        ''' test to confirm memoize sets attribute of test object '''
        class TestClass:
            ''' test class to use memoize on '''
            def a_method(self):
                ''' method in test class '''
                return 42

            @memoize
            def a_property(self):
                ''' property in test class '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=99) as mocked:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, 99)
            self.assertEqual(test_obj.a_property, 99)
        mocked.assert_called_once()
