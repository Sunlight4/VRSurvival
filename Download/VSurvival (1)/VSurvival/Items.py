import ItemClass,getpass, getfile

user = getpass.getuser()

def air():
    air = ItemClass.Item("air",getfile.getfile("images/air.png",0,1)
    return air

def apple():
    apple = ItemClass.Item("apple",getfile.getfile("images/apple.png",0,1)
    return apple

def fish():
    fish = ItemClass.Item("fish",getfile.getfile("images/apple.png",0,1)
    return fish

def bomb():
    bomb = ItemClass.Item("bomb",getfile.getfile("images/bomb.png",0,1)

def secretitem():
    secretitem = ItemClass.Item("SecretItem",getfile.getfile("images/lol.png",0,1)
    return secretitem
