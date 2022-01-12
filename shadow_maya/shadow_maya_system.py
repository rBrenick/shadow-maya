import os
import subprocess
import sys

import pymel.core as pm
import skyhook

PORT_START_NUMBER = 65510

open_server_script_path = os.path.join(os.path.dirname(__file__), "scripts", "start_maya_py_server.py")


class ShadowMayaInstance(object):
    def __init__(self):

        self.port = get_open_port()

        self.maya_py_path = sys.executable.replace(".exe", "py.exe")
        self.process = None  # type: subprocess.Popen
        self.is_stopped = False
        self.start_process()
        self.client = self.get_skyhook_client()

    def start_process(self):
        self.process = subprocess.Popen(
            [
                self.maya_py_path,
                "-i",
                open_server_script_path,
                str(self.port)
            ],
            env=os.environ
        )
        self.is_stopped = False

    def stop_process(self):
        self.process.terminate()
        self.is_stopped = True

    def get_skyhook_client(self):
        client = skyhook.client.Client()
        client.port = self.port
        client.set_echo_execution(False)

        return client

    def new_scene(self):
        self.client.execute("new_scene")

    def open_current_maya_scene(self):
        """
        send the active maya instance scene to the shadow maya
        
        """
        current_scene_path = pm.sceneName()

        temp_file_path = "C:/temp/shadow_maya_scenes/_transfer_scene.ma"
        if not os.path.exists(os.path.dirname(temp_file_path)):
            os.makedirs(os.path.dirname(temp_file_path))

        pm.renameFile(temp_file_path)
        pm.saveFile(force=True)

        if current_scene_path:
            pm.renameFile(temp_file_path)

        result = self.client.execute(
            "execute_python",
            {"python_script": "pm.openFile('{}', force=True)".format(temp_file_path)}
        )
        return result


def get_open_port():
    return PORT_START_NUMBER
