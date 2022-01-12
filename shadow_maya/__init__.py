instance = None

# noinspection PyUnreachableCode
if 0:
    import shadow_maya.shadow_maya_system

    isinstance(instance, shadow_maya.shadow_maya_system.ShadowMayaInstance)


def main(refresh=False, *args, **kwargs):
    from . import shadow_maya_system

    global instance  # type: shadow_maya_system.ShadowMayaInstance

    if instance is not None:
        if refresh:
            instance.stop_process()
        else:
            return instance

    print("Creating ShadowMaya Instance...")
    instance = shadow_maya_system.ShadowMayaInstance()

    return instance


def reload_modules():
    import sys
    if sys.version_info.major >= 3:
        from importlib import reload
    else:
        from imp import reload

    from . import shadow_maya_system
    from . import shadow_maya_ui
    reload(shadow_maya_system)
    reload(shadow_maya_ui)


def startup():
    from maya import cmds
    if cmds.optionVar(query="ShadowMayaAutoStart"):
        main()
