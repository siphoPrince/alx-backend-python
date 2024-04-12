#!/usr/bin/env python3
""".GithubOrgClient"""


import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from utils import get_json
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    @patch('github_org_client.GithubOrgClient.get_json')
    @patch('github_org_client.GithubOrgClient._public_repos_url', new_callable=lambda: "http://example.com/repos")
    def test_public_repos(self, mock_repos_url, mock_get_json):
        test_payload = [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]

        mock_get_json.return_value = test_payload

        client = GithubOrgClient("test_org")

        repos = client.public_repos()

        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
        self.assertEqual(repos, test_payload)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test class for repos """

    @classmethod
    def setUpClass(cls):
        """ class forGithubOrgClient"""
        pass

    def tearDownClass(self):
        """ Teardown"""
        pass

    def test_public_repos_with_license(self):
        """ Test method"""
        pass

    def test_public_repos(self):
        """ Test method """
        pass

    def test_public_repos_with_license(self):
        """ Test public"""
        pass

if __name__ == "__main__":
    unittest.main()
