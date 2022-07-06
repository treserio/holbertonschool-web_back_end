#!/usr/bin/env python3
''' Setting up unittests with mock and patch for client.py '''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch, MagicMock
import typing as typ
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    ''' GithubOrgClient.public_repos integration test '''
    @parameterized.expand([
        ('cpp-netlib'),
        ('dagger')
    ])
    def test_org(self, org_name):
        ''' confirm the org property returns the correct info '''
        with patch.object(GithubOrgClient, 'org', return_value={'a': 'b'}) as mocked:
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org(), {'a': 'b'})
        mocked.assert_called_once()




