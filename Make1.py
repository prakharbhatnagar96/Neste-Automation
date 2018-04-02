import glob
import time,os
import xlrd
modified= []
list_of_files = glob.glob("D:\Data for Pc\Adven Automation\Adven\*")
for file in list_of_files:
    timeStamp = time.ctime(os.path.getmtime(file))
    stamp = timeStamp.split(" ")
    Date_Of_file = stamp[2]+"/"+stamp[1]+"/"+stamp[4]
    timeStamp = time.ctime()
    stamp = timeStamp.split(" ")
    todays_date = stamp[2]+"/"+stamp[1]+"/"+stamp[4]
    if Date_Of_file==todays_date:
        file = open(file,"r")
        str=file.read()
        list = str.split("\n")
        nol = len(list)
        l=3
        while(l<nol-1):
            str = list[l]
            data = str.split(";")
            workbook = xlrd.open_workbook('D:\Data for Pc\Adven Automation\Adven.xlsx')
            sheet = workbook.sheets()
            for row in range(1, sheet[0].nrows):
                if(sheet[0].cell_value(row,1)==data[0]):
                    print True
                else:
                    modified.append(str)
            l = l+1
