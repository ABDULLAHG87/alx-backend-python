#!/usr/bin/env python3

import unittest
from unittest.mock import PropertyMock, patch
from typing import Dict

from paramerterized import paramerterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    "class for testing GithubOrgClient"

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """method to test GithubOrgClient"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """method that test the result of public repos url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """method for testing public repos"""
        json_payload - [{'name': "Google"}, {'name': "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [index["name"] for index in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"licence": {"key": "my_licencse"}}, "my_licence", True),
        ({"licence": {"key": "other_licencse"}}, "my_licence", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """method for testing license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @paramerterized_class(
        ("org_payload", "repos_payload", "expected_repos",
         "apache2_repos")
        TEST_PAYLOAD
    )
    class TestIntegerationGithubOrgClient(unittest.TestCase):
        """class for testing integraration of fixtures"""

        @classmethod
        def setUpClass(cls):
            """method to run setupclass"""

            config = {'return_value.json.side_effect':
                      [
                          cls.org_payload, cls.repos_payload,
                          cls.org_payload, cls.repos_payload
                      ]
                      }
            cls.get_patcher = patch('requests.get', **config)
            cls.mock = cls.get_patcher.start()

        def test_public_repos(self):
            """ method for integrate test of public repos"""
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.org, self.org_payload)
            self.assertEqual(test_class.repos_payload,
                             self.repos_payload)
            self.assertEqual(test_class.public_repos(),
                             self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.mock.assert_called()

        def test_pubic_repos_with_licence(self):
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.public_repos,
                             self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.assertEqual(test_class.public_repos("apache-2.0"),
                             self.apache2_repos)
            self.mock.assert_called()

        @classmethod
        def tearDownClass(cls):
            """Class method after test o classes"""
            cls.get_patcher.stop()
