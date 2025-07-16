# LabRecipy
_control a LabVIEW program with a Python script_

This project aims to replace LabRecipe, which uses a propriatary scripting language to control a LabVIEW program, with LabRecipy, which uses Python to control a LabVIEW program.

A Python script can read values from an indicator or write to a control of a LabVIEW program by using getcontrolvalue and setcontrolvalue after "win32com.client" has been imported and some initial configuration steps. Writing new values to a control however, doesn't trigger a value change event. A separate LabVIEW program can be used to recieve write (and read) request and pass these on to the LabVIEW program under control using the 'Value (Signal)' property.

LabRecipy consists of 2 main parts.
1) dispatcher.vi which serves as a helper program as described above.
2) dispatcher.py which is a module with functions such as read and write


