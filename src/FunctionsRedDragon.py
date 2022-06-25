import sys
import os
import socket
import subprocess
from time import sleep

class FunctionsRedDragon:


    def main(self, option):

        try:

            self.option = option

            print('''

             \t##===========================================##
             \t##================Red Dragon#================##
             \t##===========================================##
             \t1) Red Dragon tools
             \t2) Linux manager
             \t3) Install tools of pentest
             \t4) Install kali repositors
             \t-1 EXIT


            ''')

            self.option = int(input("Option: "))

            if self.option > 7 or self.option < -1:
                print("Option Invalid. Try Again!")
                self.main(-1)

        except Exception as error:

            print("Error: {}".format(error))

        return self.option


    def dragon_tools(self):

        try:

            print("""

            \t\t1) Scan of ports
            \t\t2) get-ip of domain
            \t\t3) get information about system:
            \t\t-1 EXIT

                  """)

        except Exception as error:

            print("Error: {}".format(error))


    def scan_of_ports(self, option):

        try:

            domain = str(input("Domain: "))
            ports_main = [21, 22, 25, 80, 443, 3000, 5000, 8080, 8888]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)

            for port_loop in ports_main:

                conn = sock.connect_ex((domain, port_loop))

                if conn == 0:

                    print('\nPort {} Open\n'.format(port_loop))

                else:

                    print('Port {} Closed'.format(port_loop))


        except Exception as error:

            print('Error: {}'.format(error))


    def get_ip_of_domain(self, option):

        try:

            print('aa')

        except Exception as error:

            print('Error: '.format(error))


    def get_information_about_system(self, option):

        try:

            print('cc')

        except Exception as error:

            print('Error: {}'.format(error))
