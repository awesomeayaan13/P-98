def switchFile():
    data1=input("Enter the file name: ")
    data2=input("Enter the file name to be swapped: ")

    with open(data1,'r') as a:
        data_a=a.read()
        
    with open(data2,'r') as b:
        data_b=b.read()

    with open(data1,'w') as a:
        a.write(data_b)
      
        
    with open(data2,'w') as b:
        b.write(data_a)


switchFile()
    