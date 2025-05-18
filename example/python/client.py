import os
import sys
import time
import signal
import grpc

import helpers.mw as mw
import helpers.chat as chat

from examples.chat_examples import simple_chat, simple_chat_w_rag, simple_chat_w_image_query
from examples.client_examples import switch_model

# Unset proxy environment variables
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)

# Disable the proxy by setting the environment variable
os.environ["grpc.enable_http_proxy"] = "0"

stub = None
channel = None

def signal_handler(sig, frame):
    global stub
    print("Stopping execution.")
    if stub is not None:
        print("Disconnecting AAB")
        mw.disconnect(stub, channel)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run_examples():
    complete = False

    print("\n========================================")
    actionInput = "Select which example to run:\n1. Execute simple chat\n2. Execute simple chat with Knowledge Base\n3. Execute Image Query\n\n0. Exit\n\nEnter number: "
    option = input(actionInput).strip().lower()
    if option == "0":
        print("Exiting...")
        complete = True
    elif option == "1":
        print("Executing simple chat example...")
        simple_chat(stub)
        complete = True
    elif option == "2":
        print("Executing simple chat with knowledge base example...")
        simple_chat_w_rag(stub)
        complete = True
    elif option == "3":
        print("Executing image query example...")
        simple_chat_w_image_query(stub)
        complete = True
    ## This option is not available as getting 'ERROR: Access to the path 'UDDC0C1.tmp' is denied.'
    # elif option == "4":
    #     print("Executing model switch example...")
    #     switch_model(stub)
    #     complete = True
    else:
        raise Exception('Invalid option. Exiting.')

    return complete, option

def main():
    # Connect to the AAB
    global successfulConnect, stub, channel
    grpc_address = 'localhost:5006'
    channel = grpc.insecure_channel(grpc_address)
    for attempt in range(5):
        successfulConnect, stub = mw.connect(channel)
        if successfulConnect:
            print("Connected successfully!")
            break
        else:
            print(f"Connection attempt {attempt + 1} failed. Retrying...\n")
            time.sleep(5)
    if successfulConnect:
        llm_ready = mw.check_pybackend(stub)
        if llm_ready:
            print("LLM backend is ready.")
            chat.warmup(stub)
            while True:
                try:
                    complete, example = run_examples()
                    if complete and example != "0":
                        print(f"\n\nExample {example} completed.")
                        continue
                    else:
                        mw.disconnect(stub, channel)
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    mw.disconnect(stub, channel)
                    break
        else:
            print("LLM backend is not ready. Exiting.")
            mw.disconnect(stub, channel)
            exit()
    else:
        print("Connection failed. Exiting.")


if __name__ == '__main__':
    main()
        