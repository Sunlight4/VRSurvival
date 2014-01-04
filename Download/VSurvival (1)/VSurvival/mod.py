import os,getpass, getfile

user = getpass.getuser()

def search_and_run(searchfor=None):
    folder = getfile.getfile("mod")
    if os.path.exists(folder):
        for fl in os.listdir(folder):
            if searchfor==None or fl==searchfor:
                flnm = folder+"/"+fl
                execfile(flnm)

def runpythonfiles():
    folder = getfile.getfile(mod)
    
    for fl in os.listdir(folder):
        flnm = folder+"/"+fl
        execfile(flnm)
        
    

  
