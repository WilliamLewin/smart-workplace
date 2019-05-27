data = ['5','100','200','300','400','500','600','700','800','900','1000','1100']

for xyz in range(0,len(data)):
    file = open(data[xyz],'r')
    packets = file.read()
    buffer = []
    for i in range(0, len(packets)):
        if packets[i] != '\n':
            buffer.append(packets[i])
    str = ''.join(buffer)
    str = str.replace(" ","")
    str = str.split("Payload:")
    x = 0
    counter = 0
    for i in range(0,len(str)):
        x = str[i].count("5920.12345920.1234")
        counter = counter + x
    txt = "Range: " + data[xyz] + " meter"
    print(txt)
    print(counter)
