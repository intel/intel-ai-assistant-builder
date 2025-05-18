import unittest
import json
from unittest.mock import MagicMock, patch
from helpers.chat import warmup, get_chat_history, generate_random_session_id, init_chat_session, set_chat_request, get_chat_response, remove_session

class TestChatHelpers(unittest.TestCase):

    @patch('helpers.chat.sb.LoadModelsRequest')
    def test_warmup(self, MockLoadModelsRequest):
        stub = MagicMock()
        warmup(stub)
        stub.LoadModels.assert_called_once_with(MockLoadModelsRequest())

    @patch('helpers.chat.sb.GetChatHistoryRequest')
    def test_get_chat_history(self, MockGetChatHistoryRequest):
        stub = MagicMock()
        stub.GetChatHistory.return_value.data = json.dumps([{"sid": 1}, {"sid": 2}])
        result = get_chat_history(stub)
        self.assertEqual(result, [{"sid": 1}, {"sid": 2}], "Test get_chat_history failed")

    def test_generate_random_session_id(self):
        chat_history = [{"sid": 1}, {"sid": 2}]
        result = generate_random_session_id(chat_history)
        self.assertNotIn(result, [1, 2], "Test generate_random_session_id failed: ID is in existing IDs")
        self.assertIsInstance(result, int, "Test generate_random_session_id failed: ID is not an integer")

    @patch('helpers.chat.get_chat_history')
    @patch('helpers.chat.generate_random_session_id')
    def test_init_chat_session(self, mock_generate_random_session_id, mock_get_chat_history):
        stub = MagicMock()
        mock_get_chat_history.return_value = [{"sid": 1}, {"sid": 2}]
        mock_generate_random_session_id.return_value = 3
        result = init_chat_session(stub)
        self.assertEqual(result, 3, "Test init_chat_session failed")

    @patch('helpers.chat.init_chat_session')
    @patch('helpers.chat.sb.ChatRequest')
    def test_set_chat_request(self, MockChatRequest, mock_init_chat_session):
        stub = MagicMock()
        mock_init_chat_session.return_value = 12345678
        prompt = "Hello, world!"
        result = set_chat_request(stub, prompt)
        MockChatRequest.assert_called_once_with(
            name="Python Client Example",
            prompt=prompt,
            sessionId=12345678,
            attachedFiles="[]",
            queryType=None
        )
        stub.Chat.assert_called_once_with(MockChatRequest())

    @patch('helpers.chat.sb.RemoveSessionRequest')
    def test_remove_session(self, MockRemoveSessionRequest):
        stub = MagicMock()
        session_id = 12345678
        remove_session(stub, session_id)
        stub.RemoveSession.assert_called_once_with(MockRemoveSessionRequest(sessionId=session_id))

    def test_get_chat_response(self):
        response_iterator = [
            MagicMock(message=json.dumps({"message": "Hello"})),
            MagicMock(message=json.dumps({"message": "World"}))
        ]
        result = get_chat_response(response_iterator, verbose=False)
        self.assertEqual(result, "HelloWorld", "Test get_chat_response_non_verbose failed")


if __name__ == '__main__':
    unittest.main()