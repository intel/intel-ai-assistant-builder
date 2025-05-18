import unittest
import json
from unittest.mock import MagicMock, patch
from helpers.config import get_config, set_config

class TestConfigHelpers(unittest.TestCase):

    @patch('helpers.config.sb.GetClientConfigRequest')
    def test_get_config(self, MockGetClientConfigRequest):
        stub = MagicMock()
        stub.GetClientConfig.return_value.data = json.dumps({"key": "value"})
        result = get_config(stub)
        self.assertEqual(result, {"key": "value"}, "Test get_config failed")
        stub.GetClientConfig.assert_called_once_with(MockGetClientConfigRequest())

    @patch('helpers.config.sb.SetActiveAssistantRequest')
    def test_set_config(self, MockSetActiveAssistantRequest):
        stub = MagicMock()
        config_data = json.dumps({"model": "example_model"})
        assistant = "example_assistant"
        response_message = "Config set successfully"
        stub.SetActiveAssistant.return_value.message = response_message
        result = set_config(stub, assistant, config_data)
        self.assertEqual(result, response_message, "Test set_config failed")
        MockSetActiveAssistantRequest.assert_called_once_with(assistant=assistant, models_json=config_data)
        stub.SetActiveAssistant.assert_called_once_with(MockSetActiveAssistantRequest())

if __name__ == '__main__':
    unittest.main()