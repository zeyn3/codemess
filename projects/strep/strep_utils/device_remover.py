from datetime import datetime

now = datetime.now()
time = now.strftime("%D")
recieved = input("Please enter the name of device to be removed: ")

def deactive(value):
    
    with open("../strep-master/devices.txt","r+") as devices:
        if "T-01" in value:
            devices.seek(62)
            devices.write(" #deactivated on " + time)
        elif "T-02" in value:
            devices.seek(123)
            devices.write(" #deactivated on " + time)
        elif "T-03" in value:
            devices.seek(184)
            devices.write(" #deactiveted on " + time)
        elif "T-04" in value:
            devices.seek(245)
            devices.write(" #deactivated on " + time)
        elif "B-01" in value:
            devices.seek(307)
            devices.write(" #deactivated on " + time)
        elif "B-02" in value:
            devices.seek(368)
            devices.write(" #deactivated on " + time)
        elif "B-03" in value:
            devices.seek(430)
            devices.write(" #deactivated on " + time)
        else:
            print("There isn't device such {}".format(value))


deactive(recieved)
