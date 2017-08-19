import xlrd

data = xlrd.open_workbook('1.xlsx')
table = data.sheets()[0]
iplist = []
for i in range(300):
    iplist.append(table.cell(i,0).value+':'+str(int(table.cell(i,1).value)))

#for ip in iplist:
    #print(ip)

print(iplist)