import json
import random
import string
import superbuilder_middleware_pb2 as sb

def warmup(stub):
    """
    Sends a warmup request to the server to initialize LLM models.
    
    Args:
        stub: The gRPC stub for making requests to the server.
    """
    if stub is not None:
        print("Warming Up LLM Models...")
        stub.LoadModels(sb.LoadModelsRequest())

def get_chat_history(stub):
    """
    Retrieves the chat history from the server.
    
    Args:
        stub: The gRPC stub for making requests to the server.
    
    Returns:
        A list of chat history entries.
    """
    if stub is not None:
        return json.loads(stub.GetChatHistory(sb.GetChatHistoryRequest()).data)

def generate_random_session_id(chatHistory):
    """
    Generates a unique random session ID that does not exist in the current chat history.
    
    Args:
        chatHistory: A list of existing chat sessions.
    
    Returns:
        A unique session ID as an integer.
    """
    existing_ids = {session['sid'] for session in chatHistory}

    while True:
        new_session_id = ''.join(random.choices(string.digits, k=8))
        if int(new_session_id) not in existing_ids:
            return int(new_session_id)

def init_chat_session(stub):
    """
    Initializes a new chat session by retrieving the chat history and generating a unique session ID.
    
    Args:
        stub: The gRPC stub for making requests to the server.
    
    Returns:
        A unique session ID as an integer.
    """
    response = get_chat_history(stub)
    return generate_random_session_id(response)

def set_chat_request(stub, prompt, session_id=None, name="Python Client Example", attachments=[], query=None):
    """
    Sends a chat request to the server with the given prompt and session details.
    
    Args:
        stub: The gRPC stub for making requests to the server.
        prompt: The chat prompt to send.
        session_id: The session ID for the chat (optional).
        name: The name of the client (default is "Python Client Example").
        attachments: A list of attachments to include in the request (default is an empty list).
        query: The query type for the request (optional).
    
    Returns:
        The server's response to the chat request.
    """
    attachments_str = "[]" if attachments == [] else json.dumps(attachments)
    if session_id is None:
        session_id = init_chat_session(stub)
    request = sb.ChatRequest(name=name, prompt=prompt, sessionId=session_id, attachedFiles=attachments_str, queryType=query)
    print("\nPrompt:\n", prompt)
    return stub.Chat(request)

def get_chat_response(response_iterator, verbose=True):
    """
    Iterates over the chat response from the server and optionally prints the output.
    
    Args:
        response_iterator: An iterator for the server's chat response.
        verbose: Whether to print the response as it streams (default is True).
    
    Returns:
        The entire chat response as a string.
    """
    entireResponse = ""
    if verbose:
        print("Response:")
    for jsonResponse in response_iterator:
        responseObj = json.loads(jsonResponse.message)
        response = responseObj.get('message', "")
        if verbose:
            print(response, end='', flush=True)
        entireResponse += response
    if verbose: 
        print("\n")
    return entireResponse

def remove_session(stub, session_id):
    """
    Sends a request to the server to remove a chat session.
    
    Args:
        stub: The gRPC stub for making requests to the server.
        session_id: The session ID of the chat to remove.
    
    Returns:
        The server's response to the remove session request.
    """
    if stub is not None:
        return stub.RemoveSession(sb.RemoveSessionRequest(sessionId=session_id))