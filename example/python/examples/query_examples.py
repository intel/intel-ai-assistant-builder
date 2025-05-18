import superbuilder_middleware_pb2 as sb
import helpers.chat as chat
import helpers.parameters as param

def image_query(stub):
    session_id = chat.init_chat_session(stub)
    success = False
    print(f"Start image query, setting params")
    parametersReq = param.init_default_params()
    reply = param.set_parameters(stub, parametersReq)

    # set up the image files
    file_input=input("Enter the path to the first image file: ")
    attached_files = [file_input]

    prompt = "Describe the images"
    response_iterator = chat.get_chat_response(stub, name='SuperBuilder Python Clients!', prompt=prompt, session_id=session_id, attachments=attached_files, query='image')
    response = chat.get_chat_response(response_iterator)

    return session_id,response