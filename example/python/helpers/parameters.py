import superbuilder_middleware_pb2 as sb

def init_default_params():
    parametersReq = sb.SetParametersRequest(
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
    ))
    return parametersReq

def set_parameters(stub, params):
    reply = stub.SetParameters(params)
    return reply