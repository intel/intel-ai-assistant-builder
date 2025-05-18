import unittest
from unittest.mock import MagicMock, patch
import grpc
from helpers.mw import check_pybackend, connect, disconnect

class TestMWHelpers(unittest.TestCase):

    @patch('helpers.mw.sb.SayHelloRequest')
    def test_check_pybackend_success(self, MockSayHelloRequest):
        stub = MagicMock()
        stub.SayHelloPyllm.return_value.message = "Hello from server"
        result = check_pybackend(stub)
        self.assertTrue(result, "Test check_pybackend_success failed")
        stub.SayHelloPyllm.assert_called_once_with(MockSayHelloRequest(name='SuperBuilder Python Clients!'))

    @patch('helpers.mw.sb.SayHelloRequest')
    def test_check_pybackend_failure(self, MockSayHelloRequest):
        stub = MagicMock()
        stub.SayHelloPyllm.return_value.message = ""
        result = check_pybackend(stub)
        self.assertFalse(result, "Test check_pybackend_failure failed")
        stub.SayHelloPyllm.assert_called_once_with(MockSayHelloRequest(name='SuperBuilder Python Clients!'))

    @patch('helpers.mw.sbg.SuperBuilderStub')
    @patch('grpc.channel_ready_future')
    def test_connect_success(self, mock_channel_ready_future, MockSuperBuilderStub):
        channel = MagicMock()
        mock_channel_ready_future.return_value.result.return_value = None
        success, stub = connect(channel)
        self.assertTrue(success, "Test connect_success failed")
        MockSuperBuilderStub.assert_called_once_with(channel)

    @patch('helpers.mw.sbg.SuperBuilderStub')
    @patch('grpc.channel_ready_future')
    def test_connect_failure(self, mock_channel_ready_future, MockSuperBuilderStub):
        channel = MagicMock()
        mock_channel_ready_future.return_value.result.side_effect = grpc.FutureTimeoutError()
        success, stub = connect(channel)
        self.assertFalse(success, "Test connect_failure failed")
        MockSuperBuilderStub.assert_not_called()

    @patch('helpers.mw.sb.ClientDisconnectedRequest')
    def test_disconnect(self, MockClientDisconnectedRequest):
        stub = MagicMock()
        channel = MagicMock()
        disconnect(stub, channel)
        stub.ClientDisconnected.assert_called_once_with(MockClientDisconnectedRequest())
        channel.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()