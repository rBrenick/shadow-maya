# shadow-maya
What if we put a Maya inside your Maya?

Basically have a separate instance of Maya for heavy tasks. Things we don't want taking up the current session.

Like:
- Long exports
- Destructive scene operations
- Basically anything you would send to a batch machine

This system uses [skyhook](https://github.com/EmbarkStudios/skyhook/) to communicate with the instance.

# Install

<pre>
1. Download this package and unzip it in a good location 
    1.B (or git clone it directly if you have git installed)
2. Run installer.bat (will walk you through some options for install)
3. Restart the DCC
</pre>

# Using the system
<pre>
import shadow_maya
sm = shadow_maya.main()

# Open the current maya scene in the ShadowMaya instance 
sm.open_current_maya_scene()

# Execute arbitrary python in the ShadowMaya instance
sm.client.execute("execute_python", {"python_script": "print('Eyo')"})
</pre>




