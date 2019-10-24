import tr
import re
import os
import argparse
import json
import sys
import socket

class PlateRecognize():

    def __init__(self):
        self.path = opt.path
        self.ip = opt.ip
        self.port = opt.port
        self.temp = []

    def os_path(self):
        dir_list = os.listdir(self.path)
        # print(dir_list)
        dirs = []
        for i in dir_list:
            dirs.append(i)

        return dirs

    def plate_recognize(self):
        
        dirs = PlateRecognize().os_path()
        # print(dirs)

        plate_list = {}
        for filename in dirs:
            pth = self.path + os.sep + filename
         
            plate = tr.recognize(pth)[0].upper()
            last_num = re.findall(r"[0-9A-Z]{4}$", plate)

            if plate[:3].isalpha():
                char = []
                
                for i in last_num[0]:
                    if i == "I":
                        char.append("1") 
                    elif i == "O":
                        char.append("0")        
                    elif i == "Z":
                        char.append("2")
                    elif i == "J":
                        char.append("1")
                    elif i == "L":
                        char.append("2")

                    else:
                        char.append(i)
              #print(char) 
                
                real_plate = ""
                for i in plate[:3]:
                    real_plate += i
                for i in char:
                    real_plate += i
               
                #real_plate = real_plate + char
                plate_list.update({filename : real_plate})
                
            else: 
            # x = plate[:2].isalpha()
            # print(x)
                old_plate = ""
                for i in plate:
                    if i != "-":
                        old_plate += i
                plate_list.update({filename : old_plate})

        return plate_list

    def result_to_json(self):
        
        getDict = self.plate_recognize()
        result_json = json.dumps(getDict)

        return result_json


    def client(self):

        HOST, PORT = self.ip, self.port
        #HOST, PORT = "192.168.140.193", 5000
        #HOST, PORT = "localhost", 9527
        data = self.result_to_json()
        
        print("data: ",data)
        print("temp: ", self.temp)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if len(self.temp) > 5:
            self.temp = []

        try:

            sock.connect((HOST, PORT))
            sock.send(bytes(json.dumps(data), 'UTF-8'))

            # if data not in self.temp:
            #     self.temp.append(data)
            #     # Connect to server and send data
            #     sock.connect((HOST, PORT))
            #     sock.send(bytes(json.dumps(data), 'UTF-8'))
            #     print("send")
            # else:
            #     print("not send")
            #     pass
            
        finally:
            sock.close()


if __name__ == "__main__":
    import time

    parse = argparse.ArgumentParser()
    parse.add_argument("--path", "-p", type=str ,default="/home/ubuntu/Desktop/result", help="pic path")
    parse.add_argument("--ip", "-i", type=str, default="192.168.140.193", help="host ip")
    parse.add_argument("--port", '-port', type=int, default=5000, help="host port")
    opt = parse.parse_args()
    print(opt)

    pr = PlateRecognize()
    #print(pr.result_to_json())
    while True:
        pr.client()
        time.sleep(2)
        print("*" * 10)

