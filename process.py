'''
RoMoSo
Processing the file mtainfo.csv
'''

#open csv:
file = open("mtainfo.csv", "r")
csv = file.readlines()
file.close()
            
#split the CSV by commas to make an array:
def splitCommas(list):
    ctr = 0
    while ctr < len(list):
        list[ctr] = list[ctr].split(", ")
        ctr += 1
    ctr = 0
    while ctr < len(list):
        list[ctr] = list[ctr][0].split(",")
        ctr += 1        
    return list

splitCommas(csv)
#print ("split commas")
#print(csv[:10])

#remove all whitespace characters such as \n and \t
def rmWhiteSp(list):
    ctr = 0
    while ctr < len(list):
        subctr = 0
        while subctr < len(list[ctr]):
            list[ctr][subctr] = list[ctr][subctr].strip()
            subctr += 1
        ctr += 1
    return list

rmWhiteSp(csv)
#print("rm white space: ")
#print(csv[:10])

#remove unnecessary columns: (ID, etc)
def rmCol(num):
    ctr = 0
    while ctr < len(csv):
        csv[ctr] = csv[ctr][0:num]+ csv[ctr][num + 1:]
        ctr += 1

'''
def makeFloat(col):
    ctr = 1
    while ctr < len(csv):
        csv[ctr][col] = float(csv[ctr][col])
        ctr += 1
'''

rmCol(0)
rmCol(0)
rmCol(0)
rmCol(0)
rmCol(0)
rmCol(3)
#print(csv[:5])
#makeFloat(4)
#makeFloat(3)

#test function to be able to print out all of the stations in a subway line:
def printLine(line):
    print(line) 
    print ("train:")
    for i in csv:
        try: 
            if i[2].index(line) >= 0:
                print i
        except:
            pass
    print("=====================================================")

printLine("6")
printLine("L") #whack
printLine("1") 
printLine("7")
printLine("C")
printLine("A")
printLine("F") #whack
printLine("G") #whack
printLine("J") #last two should be at top
printLine("N")
printLine("W")
printLine("Q")
printLine("S") #unconnected, different lines (maybe choose which shuttle?)

#create new file, named Driver.java:
file = open("Driver.java", "w")
#heading:
s = "/*\nRoMoSo\nClara Mohri, Rohan Ahammed, Soojin Choi\n*/\n"
s += "//This file has been written by the Python file process.py\n\n"
s += "import java.util.LinkedList;\n"
s += "public class Driver{\n\tpublic static void main (String[] args){\n"
file.write(s)

#method write takes arguments string line and string name
#it creates a LinkedList called name in Driver.java that contains Stations from line 
def write(line, name):
    #construct new LinkedList:
    listdec = "\n\t\tLinkedList<Station> "
    listdec += name
    listdec += " = new LinkedList<Station>();\n"
    file.write(listdec)
    #add all of the Stations:
    for i in csv:
        try:
            if i[2].index(line) >= 0:
                file.write("\t\t")
                file.write(name)
                file.write(".add(")
                file.write("new Station(")
                s = ""
                for x in i:
                    item = x
                    if (x == i[2]):
                        item = line
                    s += "\""
                    s += item
                    s += "\"" 
                    s += ", "
                s = s[:-2] #remove last comma
                s += "));"
                file.write(s)                
                file.write("\n")                
        except: 
            pass

    
write("1", "one")
write("6", "six")
write("C", "c")
write("N", "n")
write("7", "seven")
file.write("\t}\n")
file.write("}")
file.close()
