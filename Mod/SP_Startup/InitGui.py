__author__ = "Studio Petrikas"
__credits__ = "Mindaugas Petrikas"
__license__ = "CC0"
__version__ = "1.0"
__contact__ = "http://twitter.com/MPetrikas"

def runMacro():
    
    FreeCADGui.getMainWindow().workbenchActivated.disconnect(runMacro)
    
    import SP_Startup
    SP_Startup.run()

import __main__
__main__.runMacro = runMacro

FreeCADGui.getMainWindow().workbenchActivated.connect(runMacro)