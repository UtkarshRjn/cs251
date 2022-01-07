import gdb

rbp_arr = []

def printer(event):
    rsp = int(gdb.parse_and_eval("$rsp"))
    rbp = int(gdb.parse_and_eval("$rbp"))

    toPrint = False
    if rbp >= rsp:
        rbp_arr.append(rbp)
        toPrint = True
    
    i = gdb.inferiors()[0]
    j = 0
    while toPrint:
        print("+" + "-"*25 + "+")
        print("|", end=" ")
        if(rsp+8*j == rbp): 
            if j==0:
                for k in range(8):
                    print(i.read_memory(rsp+8*j,8).tobytes().hex()[k:k+2], end = " ")
                print("| <- rsp rbp")                    
            else:
                for k in range(8):
                    print(i.read_memory(rsp+8*j,8).tobytes().hex()[k:k+2], end = " ")
                print("| <- rbp")
        elif(rsp+8*j == rsp):
            for k in range(8):
                print(i.read_memory(rsp+8*j,8).tobytes().hex()[k:k+2], end = " ")
            print("| <- rsp")
        else: 
            for k in range(8):
                print(i.read_memory(rsp+8*j,8).tobytes().hex()[k:k+2], end = " ")
            print("|")

        if(rsp+8*j == rbp_arr[0]):
            print("+" + "-"*25 + "+") 
            break
        j = j+1

gdb.events.stop.connect(printer)
