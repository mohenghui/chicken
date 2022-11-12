# from time import time
import serial
import time
# ser = serial.Serial("COM5", 9600, 8, "E", timeout=50,stopbits=1)

# # 数据帧
# NO1_open='01 05 00 00 FF 00 8C 3A' #"上灯"
# NO1_down="01 05 00 00 00 00 CD CA"

# NO2_open="01 05 00 01 FF 00 DD FA"
# NO2_down="01 05 00 01 00 00 9C 0A"

# NO3_open="01 05 00 02 FF 00 2D FA"
# NO3_down="01 05 00 02 00 00 6C 0A"

# NO4_open="01 05 00 03 FF 00 7C 3A"
# NO4_open="01 05 00 03 00 00 3D CA"
# k=bytes.fromhex(NO1_open)
# d=bytes.fromhex(NO1_down)

# # 串口发送数据
# ser.write(k)
# time.sleep(1)
# ser.write(d)


# count=ser.inWaiting()

# ser.close()
import serial
import serial.tools.list_ports
 
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备。")
else:
    print("可用的串口设备如下：")
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])