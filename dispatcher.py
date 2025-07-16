# title      : dispatcher.py
# description: set of functions to write to controls and read from indicators of a LabVIEW program
# version    : 20250715

#
# Use this as a module to be imported in a Python script, for example:
#
# import dispatcher as vi
#
# Then use this to write a value to a control (or an indicator):
#
# vi.write("control label","value")
#
# or this to read a value from an indicator (or a control)
#
# value = vi.read("indicator label")
#

import win32com.client

timer0 = 0.0

# create objects for labview objects
def connect(path):
    global labview
    labview = win32com.client.Dispatch("Labview.Application")
    global VI
    VI = labview.getvireference(path)
    vipath = VI.getcontrolvalue('vi path')
    global VIdirect
    VIdirect = labview.getvireference(vipath)

# write a value through the dispatcher
def write(varname,varvalue):
    VI.setcontrolvalue('writing',(True,varname,varvalue))
    while (VI.getcontrolvalue('writing')[1] != '' ):
        pass

# read a value through the dispatcher
def read(varname):
    VI.setcontrolvalue('reading',(True,varname,''))
    while (VI.getcontrolvalue('reading')[1] != '' ):
        pass
    return VI.getcontrolvalue('reading')[2]

# write a value directly e.g. a Numeric/Boolean/String/Array/Cluster
def writethis(varname, varvalue):
    #varname=''+varname
    VIdirect.setcontrolvalue(varname, varvalue)

# read a value directly e.g. a Numeric/Boolean/String/Array/Cluster
def readthis(varname):
    varname=''+varname
    return VIdirect.getcontrolvalue(varname)

# read the time (seconds since) from the dispatcher
def readtime():
    return float(VI.getcontrolvalue('time'))

# read the timestamp from the dispatcher
def readtimestamp():
    return VI.getcontrolvalue('time stamp')

# wait until the next sync period starts (first period is expected to be different/shorter)
def sync(sync):
    sstart = readtime() // sync
    while ((readtime() // sync) == sstart):
        pass
        pass
        pass

# wait a number of seconds
def wait(wait):
    tstart = readtime()
    while ((readtime()-tstart)<wait):
        pass
        pass
        pass

def tmrruntime():
    global timer0
    rtval = timer0 - readtime()
    return(rtval)

def tmrrunning():
    global timer0
    rtval = readtime() < timer0
    # print("running " + str(rtval))
    return(rtval)

def tmrset(tset):
    global timer0
    timer0 = float(tset) + readtime()
    # print("set " + str(timer0) + " ("+ str(tset) + ")")



#### USER ALIASES ####

def valve(**valves):
    for v in range(len(valves)):
        write(v,"1")

def valve_open(*valves):
    for v in valves:
        write(v,"1")

def valve_close(*valves):
    for v in valves:
        write(v,"0")

def mfc_close(varname):
    pass

def status(text):
    VI.setcontrolvalue('status',text)

         