import grpc
import os
import sys
SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(SCRIPT_DIR,'..')))

import helpers.chat as chat
import helpers.rag as rag
import helpers.parameters as param

def simple_chat(stub):
    try:     
        prompt = "Who are you"

        session_id = chat.init_chat_session(stub)

        response_iterator = chat.set_chat_request(stub, prompt, session_id)
        response = chat.get_chat_response(response_iterator)
        chat.remove_session(stub, session_id)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
    except Exception as e:
        print(f"Error: {e}")

def simple_chat_w_rag(stub):
    try:
        file_path = ["examples/resources/Minimum Wages Order 2022.pdf"]
        prompt = "What is the minimum wages order for 2022 in Malaysia?"

        # Upload the file to the knowledge base
        rag.upload_file_to_knowledge_base(stub, file_path)
        rag.list_uploaded_files(stub)
        session_id = chat.init_chat_session(stub)

        response_iterator = chat.set_chat_request(stub, prompt, session_id)
        response = chat.get_chat_response(response_iterator)

        rag.remove_uploaded_file(stub, file_path)
        chat.remove_session(stub, session_id)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
    except Exception as e:
        print(f"Error: {e}")

def simple_chat_w_image_query(stub):
    try:
        file_input = ["examples/resources/image.jpg"]
        prompt = "Describe the images"    

        session_id = chat.init_chat_session(stub)

        response_iterator = chat.set_chat_request(stub, name='SuperBuilder Python Clients!', prompt=prompt, session_id=session_id, attachments=file_input, query='image')
        response = chat.get_chat_response(response_iterator)

        chat.remove_session(stub, session_id)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
    except Exception as e:
        print(f"Error: {e}")
