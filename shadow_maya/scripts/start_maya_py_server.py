import sys

print(sys.argv)
port = sys.argv[1]

import maya.standalone

maya.standalone.initialize()

import skyhook.server as shs
from skyhook.constants import HostPrograms

SHADOW_MAYA_SKYHOOK_SERVER = shs.start_blocking_server(host_program=HostPrograms.maya, port=int(port),
                                                       load_modules=["maya_mod"])


def close_shadow_server():
    SHADOW_MAYA_SKYHOOK_SERVER.stop_listening()
    return True
