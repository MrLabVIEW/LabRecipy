# LabRecipy
control a LabVIEW program with a Python script

This project aims to replace LabRecipe, which uses a propriatary scripting language to control a LabVIEW program, with LabRecipy, which uses Python to control a LabVIEW program.

A Python script can read values from an indicator or write to a control of LabVIEW by using getcontrolvalue and setcontrolvalue after "win32com.client" has been imported and some initial configuration step.
