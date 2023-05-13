import os
import tempfile
import unittest
from unittest import mock
from src import http_connection

class TestHTTPConnection(unittest.TestCase):

    @mock.patch('requests.get')
    def test_save_endpoint_response_saved(self, mock_get):
        
        # Create a mock object for the get request
        mock_response = mock.Mock()
        mock_response.content = b"test content"
        mock_get.return_value = mock_response

        # Create a temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:

            # Save the returned object to disk
            http_connection.save_endpoint_response('about:blank/test', 'txt', tmpdir)

            # Check if file exists
            self.assertEqual(os.listdir(tmpdir), ['test.txt'])

    @mock.patch('requests.get')
    def test_save_endpoint_response_content(self, mock_get):
        
        # Create a mock object for the get request
        content = b"test content"
        mock_response = mock.Mock()
        mock_response.content = content
        mock_get.return_value = mock_response

        # Create a temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:

            # Save the returned object to disk
            http_connection.save_endpoint_response('about:blank/test', 'txt', tmpdir)

            # Open file and check if content is the same as sent to module
            filepath = os.path.join(tmpdir, 'test.txt')
            with open(filepath, 'rb') as f:
                self.assertEqual(f.read(), content)