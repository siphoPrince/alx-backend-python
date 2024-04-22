#!/usr/bin/env python3
""".GithubOrgClient"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name, mock_get_json):
        expected_url = f"https://api.github.com/orgs/{org_name}"
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(expected_url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        test_payload = {"repos_url": "http://example.com/repos"}
        mock_org.return_value = test_payload

        test_client = GithubOrgClient("test_org")
        result = test_client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_public_repos_url.return_value = "http://example.com/repos"
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        test_client = GithubOrgClient("test_org")
        result = test_client.public_repos()

        mock_get_json.assert_called_once_with("http://example.com/repos")
        self.assertEqual(result, test_payload)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo_payload, license_key, expected):
        test_client = GithubOrgClient("test_org")
        result = test_client.has_license(repo_payload, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
