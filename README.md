# LabRecipy
_control a LabVIEW program with a Python script_

## Introduction
This project aims to replace LabRecipe, which uses a proprietary scripting language to control a LabVIEW program, with LabRecipy, which uses Python to control a LabVIEW program.

A Python script can read values from an indicator or write to a control of a LabVIEW program by using getcontrolvalue and setcontrolvalue after "win32com.client" has been imported and some initial configuration steps have been made. Writing new values to a control however, doesn't trigger a value change event. A separate LabVIEW helper program can be used to recieve write (and read) requests and apply these, using the 'Value (Signal)' property, on controls of the LabVIEW program.

LabRecipy consists of 2 main parts.
1) dispatcher.vi which serves as a helper program as described above.
2) dispatcher.py which is a module with functions such as read and write.

## Requirements
The dispatcher.py module depends on the win32com module, which is part of the pywin32 package. In a Windows command prompt use the following command to install the package:
```
python -m pip instal pywin32
```

## Status
LabRecipy, at a functional level, fully replaces LabRecipe.

## Future versions
Future enhancements could be some of the following:
1) allowing to run multiple scripts alongside of each other, e.g. one to automate a process and one or more for condition monitoring.
2) simulating mouse clicks for latched Booleans because for these the 'Value (Signal)' property cannot be used.
3) changing other properties, e.g. colors, visibility, than just the value.
