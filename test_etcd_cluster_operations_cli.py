import unittest
from unittest.mock import patch, MagicMock
import io
import etcd_config.command_line_app as cli_app

class TestCommandLineApp(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_keys_and_exit(self, mock_stdout, mock_input):
        cli_app.list_keys()
        expected_output = "Retrieving all keys from port 2379:\n1 - mykey\n2 - mykey2\n3 - mykey3\n4 - mykey4\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['mykey'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_value(self, mock_stdout, mock_input):
        # etcd_mock = MagicMock()
        # etcd_mock.get.return_value = ('firstvalue1', None)
        # with patch('etcd3.client', return_value=etcd_mock):
        cli_app.get_value()
        expected_output = "Enter the key to get the value:\nValue for key mykey in port 2379:\nmyvalue\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['new_key', 'new_value'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_put_pair(self, mock_stdout, mock_input):
        # etcd_mock = MagicMock()
        # with patch('etcd3.client', return_value=etcd_mock):
        cli_app.put_pair()
        expected_output = "Enter the key\nEnter the value\nKey-Value pair inserted in the cluster through port 2379\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['testkey'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_pair(self, mock_stdout, mock_input):
        # etcd_mock = MagicMock()
        # with patch('etcd3.client', return_value=etcd_mock):
        cli_app.delete_pair()
        expected_output = "Enter the key to delete:\nKey-Value pair deleted in the cluster through port 2379\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
