# -*- encoding: utf-8 -*-
"""
Module with some send code functions
"""

import os
import socket
import logging
import json
import tempfile

logging.basicConfig(level=logging.INFO)

HOST = '127.0.0.1'

def send_python_code_to_maya(code, port, variables=None):
    try:

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
        temp_file.write(code.encode('utf-8'))
        temp_file.close()

        data_to_send = {
            'script': temp_file.name,
            'variables': variables if variables is not None else {}
        }

        serialized_data = json.dumps(data_to_send)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, port))
            s.sendall(serialized_data.encode())
            logging.info(f"Code and variables sent to instance : {port}")
        #os.remove(temp_file.name)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
