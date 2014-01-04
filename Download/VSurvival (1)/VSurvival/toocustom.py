
def secret(startwith=0,length=64):
    f=open("/Users/dsaff/Desktop/VSurvival/world/world1.txt","a+")
    for i in range(startwith, startwith+length+1, 16):
        j=str(i)
        f.write("\n"+"3,"+j+",64")
        f.write("\n"+"2,"+j+",80")
        f.write("\n"+"1,"+j+",96")
        f.write("\n"+"16,"+j+",112")
    f.close()
