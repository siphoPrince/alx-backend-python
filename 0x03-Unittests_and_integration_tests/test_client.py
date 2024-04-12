#!/usr/bin/env python3
""".GithubOrgClient"""


import unittest
from unittest.mock import patch
from github_org_client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
