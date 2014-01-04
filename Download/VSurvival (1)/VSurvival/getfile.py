import os
def getfile(name):
    x=os.environ.get("HOME", "~")
    return os.path.join(x, "VSurvival", name)
