# -*- encoding: utf-8 -*-
"""
Module with some send code functions
"""

import socket
import logging
import json

logging.basicConfig(level=logging.INFO)

HOST = '127.0.0.1'

def send_python_code_to_maya(code, port, variables=None):
    try:
        # Prepare the data to send
        data_to_send = {
            'script': code,
            'variables': variables if variables is not None else {}
        }
        serialized_data = json.dumps(data_to_send)
        
        # Send the data over the socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, port))
            s.sendall(serialized_data.encode())
            logging.info(f"Code and variables sent to instance : {port}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")