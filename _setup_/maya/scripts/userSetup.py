import sys
import site
import inspect
import os

def _shadow_maya_site_dir_setup():
    dirname = os.path.dirname
    
    # Add site-packages to sys.path
    package_dir = dirname(dirname(dirname(dirname(inspect.getfile(inspect.currentframe())))))
    
    if package_dir not in sys.path:
        site.addsitedir(package_dir)

_shadow_maya_site_dir_setup()


try:
    import shadow_maya
    shadow_maya.startup()
except StandardError as e:
    print(e)




