#!/usr/bin/env python3
''' Setting up unittests with mock and patch for client.py '''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch, Mock
import typing as typ
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    ''' GithubOrgClient.public_repos integration test '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'a': 'b'})
    def test_org(self, org_name, m_get_json):
        ''' confirm the org property returns the correct info '''
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'a': 'b'})
        m_get_json.assert_called_once()
