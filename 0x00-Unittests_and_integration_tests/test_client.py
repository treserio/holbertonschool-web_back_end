#!/usr/bin/env python3
''' Setting up unittests with mock and patch for client.py '''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch, PropertyMock
import typing as typ
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    ''' GithubOrgClient.public_repos integration test '''
    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json', return_value={'a': 'b'})
    def test_org(self, org_name: str, m_get_json):
        ''' confirm the org property returns the correct info '''
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'a': 'b'})
        m_get_json.assert_called_once()

    def test_public_repos_url(self):
        ''' test for GithubOrgClient._public_repos_url by patching
            GithubOrgClient.org
        '''
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value={'repos_url': [{'name': 'john'}, {'name': 'sally'}]}
        ) as m_obj:
            thing = GithubOrgClient('org_name')
            self.assertEqual(
                thing._public_repos_url,
                [{'name': 'john'}, {'name': 'sally'}]
            )
        m_obj.assert_called_once()

    @patch(
        'client.get_json',
        return_value={'repos_url': [{'name': 'john'}, {'name': 'sally'}]}
    )
    def test_public_repos(self, m_get_json):
        ''' test GithubOrgClient.public_repos while mocking get_json
            with a decorator, and GithubOrgClient._public_repos_url using with
        '''
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value={'repos_url': [{'name': 'john'}, {'name': 'sally'}]}
        ) as m_obj:
            thing = GithubOrgClient('org_name')
            self.assertEqual(
                thing.public_repos(),
                ['john', 'sally']
            )
        m_get_json.assert_called_once()
        m_obj.assert_called_once()
