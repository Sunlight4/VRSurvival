import socket, gui

s = socket.socket()

def chatterbox(): # Chatterbox: Blah Blah Blah!
    return gui.textinput()

def send(text,ips, username):
    for ip in ips:
        s.connect((ip,12345))
        s.send(username + ": " + text)

def secretfunctionhahaha():
    for ip in ips:
        s.connect((1p,12345))
        s.send("VSurvival: random Python code: print 'Hello World!'")
        s.send("VSurvival: LOL")

def donotuseorelseyouwillbesorryimeanitthisfunctioncausesconfusion(user):
    for ip in ips:
        s.connect((ip,12345))
        s.send("move" + user + ",[0,150,0]")

def nothing():
    return None
