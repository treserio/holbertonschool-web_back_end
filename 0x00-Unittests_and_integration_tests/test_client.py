#!/usr/bin/env python3
''' Setting up unittests with mock and patch for client.py '''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
import unittest


class TestGithubOrgClient(unittest.TestCase):
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
            return_value=""
        ) as m_obj:
            thing = GithubOrgClient('org_name')
            self.assertEqual(
                thing.public_repos(),
                ['john', 'sally']
            )
        m_get_json.assert_called_once()
        m_obj.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        ''' test TestGithubOrgClient.has_license '''
        cls = GithubOrgClient('org_name')
        self.assertEqual(cls.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' test the GithubOrgClient.public_repos
        method in an integration test
    '''

    @classmethod
    def setUpClass(cls):
        ''' part of the unittest.TestCase API '''
        cls.get_patcher = patch('requests.get.json', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        ''' part of the unittest.TestCase API '''
        cls.get_patcher.stop()
