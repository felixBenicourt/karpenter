# -*- encoding: utf-8 -*-
"""
Module with core functions
"""


import CONSTANTS
import json
import subprocess
import threading
import sendCodeSocket



def getToolsConfigData():
    with open(CONSTANTS.jsonToolsConfig, "r") as json_file:
        data = json.load(json_file)
    return data

def remove_untitled_keys(scripts):
    keys_to_remove = [key for key in scripts.keys() if "Untitled" in key]
    for key in keys_to_remove:
        del scripts[key]
    return scripts
    

def updateToolsConfigData(data):
    curentDict = {}
    for key, value in data.items():
        curentDict[key] = value
    with open(CONSTANTS.jsonToolsConfig, "w") as json_file:
        json.dump(curentDict, json_file, indent=4)


def executeCommandScript(buttonText, instancesID = None):
    jsonData = getToolsConfigData()
    try:
        def run_subprocess():
            if jsonData[buttonText]["type"] == "rez":
                try:
                    subprocess.run(jsonData[buttonText]["cmd"], shell=True, check=True, capture_output=True, text=True)
                except FileNotFoundError:
                    print("Error: The script {} does not exist.".format(jsonData[buttonText]["cmd"]))
                except Exception as e:
                    print("An error occurred: {}".format(e))
            if jsonData[buttonText]["type"] == "python" and instancesID:
                instID = instancesID.split("PID: ")[-1]
                sendCodeSocket.send_python_code_to_maya(jsonData[buttonText]["cmd"], int(instID))
        subprocess_thread = threading.Thread(target=run_subprocess)
        subprocess_thread.start()
    except Exception as e:
        print("An error occurred while executing the script:", e)


