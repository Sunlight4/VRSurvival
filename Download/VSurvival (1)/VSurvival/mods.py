import getpass,os,ItemClass,BlockClass,CreatureClass

user = getpass.getuser()

# Modding System! :)
# Make text files readable!
# Oops... this is a computer handwriting doesn't matter.
# Just spelyng :)

def delete(var, delete):
    var = var.replace(delete,"")
    return var


def activatemods():
    newstuff = []
    for folder in os.listdir("/Users/" + user + "/Desktop/VSurvival/mods"):
        if folder != ".DS_Store": # That anyoying .DS_Store!!!
            for fldir in os.listdir("/Users/" + user + "/Desktop/VSurvival/mods/" + folder):
                fl = open("/Users/" + user + "/Desktop/VSurvival/mods/" + folder + "/" + fldir,'r')
                code = fl.readlines()

                for line in code:
                    line = line.replace("\n","")

                    if line.startswith("addnewblock "):
                        line = delete(line,"addnewblock ")

                        blockinfo = line.split(",")

                        name = blockinfo[0]
                        texture = blockinfo[1]
                        hardness = blockinfo[2]
                        blockid = blockinfo[3]
                        size = blockinfo[4]
                        newblock = BlockClass.Block(name,hardness,size,texture)
                        newstuff.append(newblock)
                    if line.startswith("addnewitem "):
                        line = delete(line,"addnewitem ")

                        iteminfo = line.split(",")

                        name = iteminfo[0]
                        texture = iteminfo[1]
                        itemid = iteminfo[2]
                        size = iteminfo[3]
                        newitem = ItemClass.Item(name,texture,itemid,size)
                        newstuff.append(newitem)
                    if line.startswith("addnewanimal "):
                        line = delete(line,"addnewanimal")
                        newcreature = CreatureClass.Animal(line)
                        newstuff.append(newcreature)
    return newstuff
