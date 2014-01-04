import os, getpass, CreateWorld

user = getpass.getuser()

print "VSurival Server maker"
print

print "Making server folder"
try:
    os.mkdir("/Users/" + user + "/Desktop/VSurvival/server")
except:
    print "Server folder exists!"
    print "Overwriting server folder"
print "Creating server world file"
world = open("/Users/" + user + "/Desktop/VSurvival/server/world.txt", "w+")
print "Creating world. This may take a while"
worldcode = CreateWorld.create()
print "Saving world"
print "Please wait. This may take a while"
world.write(worldcode)
print "Creating config file"
optionfile = open("/Users/" + user + "/Desktop/VSurvival/server/config.txt",
                  "w+")
optionfile.write('allowallplayers = True')
optionfile.close()
print "Creating allowedplayers file"
ap = open("/Users/" + user + "/Desktop/VSurvival/server/allowed.txt","w+")
ap.close()
print "Created server!"
world.close()
