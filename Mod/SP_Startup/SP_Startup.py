__author__ = "Studio Petrikas"
__credits__ = "Mindaugas Petrikas"
__license__ = "CC0"
__version__ = "1.0"
__contact__ = "http://twitter.com/MPetrikas"

from PySide2 import QtCore, QtGui, QtWidgets
import FreeCAD as App
import FreeCADGui as Gui
from threading import Timer

# ---- User editable ----

# Change StartupFile to False if you want to load Start Workbench.
StartupFile = False 
StartupDirectory = "C:\\Users\\Gus\\AppData\\Roaming\\FreeCAD\\Startup Files\\New Design.FCStd"

# ---- End user editable ----

class SP_Startup():

    def __init__(self):
        mw = Gui.getMainWindow()
        # mw.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Activates each Enabled workbench to load all toolbars
        for k in App.ParamGet("User parameter:BaseApp/Workbenches").GetString("Enabled").split(','):
            if k != "":
                Gui.activateWorkbench(k)    

        if StartupFile == True:
            try:
                App.openDocument(StartupDirectory)
            except:
                Gui.activateWorkbench("StartWorkbench")
        else:
            Gui.activateWorkbench("StartWorkbench")

        # Timed Stuff
        #def ticktock():
        #    try:
        #    except:
        #        pass
        ## Timer, so this tool doesn't get run before UI Loads.
        #t = Timer(4, ticktock) # Adjust this number if the command happens too soon.
        #t.start()

def run():
    SP_Startup()