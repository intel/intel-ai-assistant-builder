import grpc
import json
import superbuilder_middleware_pb2 as sb

def get_config(stub):
    response = stub.GetClientConfig(sb.GetClientConfigRequest())
    return json.loads(response.data)

def set_config(stub, assistant, config_data):
    response = stub.SetActiveAssistant(sb.SetActiveAssistantRequest(assistant=assistant, models_json=config_data))
    return response.message