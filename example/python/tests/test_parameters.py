import unittest
from unittest.mock import MagicMock, patch
import superbuilder_middleware_pb2 as sb
from helpers.parameters import set_parameters, init_default_params

class TestParametersHelpers(unittest.TestCase):

    @patch('helpers.parameters.sb.SetParametersRequest')
    def test_init_default_params(self, MockSetParametersRequest):
        params = init_default_params()
        MockSetParametersRequest.assert_called_once_with(
            max_token=1024,
            temperature=1.0,
            retriever_top_k=13,
            reranker_top_k=4,
            reranker_threshold=0.0,
            max_num_references=2,
            reference_threshold=0.1,
            input_prompt_safety_threshold=0.75,
            streaming_batch_size=1,
            rag_system_message=(
                "Using the information contained in the context, give a comprehensive answer to the question.\n\n"
                "Please provide answer with full sentence, and don't end a sentence with colon.\n\n"
                "If the context is not relevant, please answer the question by using your own knowledge about the topic."
            )
        )
        self.assertEqual(params, MockSetParametersRequest(), "Test init_default_params failed")

    @patch('helpers.parameters.sb.SetParametersRequest')
    def test_set_parameters(self, MockSetParametersRequest):
        stub = MagicMock()
        params = init_default_params()
        stub.SetParameters.return_value = "Parameters set successfully"
        result = set_parameters(stub, params)
        self.assertEqual(result, "Parameters set successfully", "Test set_parameters failed")
        stub.SetParameters.assert_called_once_with(params)

if __name__ == '__main__':
    unittest.main()