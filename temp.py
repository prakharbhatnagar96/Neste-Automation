file = open("D:\Data for Pc\Adven Automation\NOAdven2920180329233216","r")
str=file.read()
list = str.split("\n")
nol = len(list)
print nol
l=3
while(l<nol-1):
    str = list[l]
    data = str.split(";")
    print data[0],l
    l = l+1