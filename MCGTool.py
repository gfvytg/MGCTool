import re
stop=0
while stop!=1:
    grid=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    keystring=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("\nWelcome to Mendicino Grid Cipher tool!")
    loop=1
    while loop==1:
        task=input("Would you like to: \n [1] encode \n [2] decode \n")
        if task==("1"):
            rose=0
            loop=0
        if task==("2"):
            rose=4
            loop=0
    loop=1
    while loop==1:
        key=input("\nEnter a key letter, word, phrase, or alphabet: \n(if no key is selected, the standard alphabet will be used) \n")
        key=key.lower()
        key=key.replace(" ","")
        if key.isalpha():
            loop=0
        elif len(key)==0:
            loop=0
        else:
            print("The cipher does not support numbers in the key in its current form.")
    ltag=len(key)
    keypointer=0
    alphapointer=0
    loop=1
    while loop==1:
        remove=input("\nSelect letter to omit. If no choice is made, Q will automatically be chosen. \n")
        if len(remove)==0:
            remove=('q')
            loop=0
        if len(remove)==1:
            if remove.isalpha():
                remove=remove.lower()
                loop=0
            else:
                print("The cipher does not support numbers in its current form.")
        if len(remove)>1:
            print("Only one letter can be removed.")
    gridpointer=0
    while gridpointer<25:
        if keypointer<ltag:
            if key[keypointer] in keystring:
                keypointer=keypointer+1
            else:
                if key[keypointer]==remove:
                    keypointer=keypointer+1
                else:
                    keystring[gridpointer]=key[keypointer]
                    keypointer=keypointer+1
                    gridpointer=gridpointer+1
        else:
            if alphabet[alphapointer] in keystring:
                alphapointer=alphapointer+1
            else:
                if alphabet[alphapointer]==remove:
                    alphapointer=alphapointer+1
                else:
                    keystring[gridpointer]=alphabet[alphapointer]
                    alphapointer=alphapointer+1
                    gridpointer=gridpointer+1
    stringpointer=0
    gridcounter=0
    gridx=0
    gridy=0
    while gridcounter<25:
        grid[gridy][gridx]=keystring[stringpointer]
        gridcounter=gridcounter+1
        stringpointer=stringpointer+1
        gridx=gridx+1
        if gridx==5:
            gridx=0
            gridy=gridy+1
    loop=1
    while loop==1:
        if task==("1"):
            workingstring=input("\nInput plaintext to be encoded: \n")
        if task==("2"):
            workingstring=input("\nInput ciphertext to be decoded: \n")
        loop=0
    loop=1
    while loop==1:
        sandc=input("\nParse all spaces and special characters (including numbers) by: \n [1] maintaining \n [2] removing \n")
        if sandc==("1"):
            workingstring=workingstring.lower()
            loop=0
        if sandc==("2"):
            workingstring=workingstring.lower()
            workingstring=re.sub(r'[^a-zA-Z]', '', workingstring)
            loop=0
    ltag=len(workingstring)
    if sandc==("1"):
        loop=1
        while loop==1:
            reset=input("\nReset compass rose after every word? \n [1] yes \n [2] no \n")
            if reset==("1"):
                loop=0
            if reset==("2"):
                loop=0
    outputlist=[]
    charpointer=0
    while len(outputlist)<ltag:
        startchar=workingstring[charpointer]
        if startchar.isalpha():
            if startchar==remove:
                outputlist.append(startchar)
                charpointer=charpointer+1
            else:
                for gridy, sublist in enumerate(grid):
                    if startchar in sublist:
                        gridx=sublist.index(startchar)
                        break
                if rose==0:
                    gridy=gridy-1
                elif rose==1:
                    gridy=gridy-1
                    gridx=gridx+1
                elif rose==2:
                    gridx=gridx+1
                elif rose==3:
                    gridy=gridy+1
                    gridx=gridx+1
                elif rose==4:
                    gridy=gridy+1
                elif rose==5:
                    gridy=gridy+1
                    gridx=gridx-1
                elif rose==6:
                    gridx=gridx-1
                elif rose==7:
                    gridy=gridy-1
                    gridx=gridx-1
                if gridy==5:
                    gridy=0
                if gridy==-1:
                    gridy=4
                if gridx==5:
                    gridx=0
                if gridx==-1:
                    gridx=4
                outputlist.append(grid[gridy][gridx])
                charpointer=charpointer+1
                rose=rose+1
                if rose==8:
                    rose=0
        else:
            if startchar==(" "):
                if reset==("1"):
                    if task==("1"):
                        rose=0
                    if task==("2"):
                        rose=4
                outputlist.append(startchar)
                charpointer=charpointer+1
            else:
                outputlist.append(startchar)
                charpointer=charpointer+1
    outputstring="".join(outputlist)
    if task==("1"):
        print("Your ciphertext is: \n")
    else:
        print("Your plaintext is: \n")
    print(outputstring)
    loop=1
    while loop==1:
        repeat=input("\nWould you like to continue using the software?\n [1] yes \n [2] no, end the program\n")
        if repeat==("1"):
            loop=0
        if repeat==("2"):
            stop=1
            loop=0