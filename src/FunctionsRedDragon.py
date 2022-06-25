import sys
import os
import socket
import subprocess
from time import sleep
from socket import gethostbyname

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

    def manager_of_linux(self):

        try:

            print("""

               1) Update repositories
               2) Upgrade System
               3) Dist-upgrade
               4) Poweroff
               5) Reboot
               -1) EXIT

               """)

            option = str(input("Option: "))

            if self.option == 1:

                os.system("sudo apt update")

            elif self.option == 2:

                os.system("sudo apt upgrade")

            elif self.option == 3:

                os.system("sudo apt dist-upgrade")

            elif self.option == 4:

                os.system("sudo poweroff")

            elif self.option == 5:

                os.system("sudo reboot")

            elif self.option == -1:

                self.exit()

            else:

                print("Option no avaible")
                self.main()

        except Exception as error:
            print("Error: {}".format(error))

    def install_tools_of_pentest(self):


        try:

            print("""

            1) Install arpspoof
            2) Install crunch
            3) Install dig
            4) Install dnsenum
            5) Install dnsrecon
            6) Install dnsmap
            7) Install dnsspoof
            8) Install ettercap
            9) Install fierce
            10) Install hydra
            11) Install iptables
            12) Install maltego
            13) Install medusa
            14) Install metasploit
            15) Install mitmf
            16) Install netcat
            17) Install netdiscover
            18) Install nmap
            19) Install netcat
            20) Install sslsplit
            21) Install sslsplit
            22) Install tcpdump
            23) Install zenmap
            -1) EXIT

            """)

            option = int(input("Option: "))

            if option == 1:

                os.system("apt install arpspoof")
                self.main()

            elif option == 2:

                os.system("apt upgrade crunch")
                self.main()

            elif option == 3:

                os.system("apt install dig")
                self.main()

            elif option == 4:

                os.system("apt install dnsenum")
                self.main()

            elif option == 5:

                os.system("apt install dnsrecon")
                self.main()

            if option == 6:

                os.system("apt install dnsmap")
                self.main()

            elif option == 7:

                os.system("apt upgrade dnsspoof")
                self.main()

            elif option == 8:

                os.system("apt install ettercap")
                self.main()

            elif option == 9:

                os.system("apt install fierce ")
                self.main()

            elif option == 10:

                os.system("apt install hydra")
                self.main()

            if option == 11:

                os.system("apt install iptables")
                self.main()

            elif option == 12:

                os.system("apt upgrade maltego")
                self.main()

            elif option == 13:

                os.system("apt install medusa")
                self.main()

            elif option == 14:

                os.system("apt install metasploit-framework")
                self.main()

            elif option == 15:

                os.system("apt install mitmf")
                self.main()

            if option == 16:

                os.system("apt install netcat")
                self.main()

            elif option == 17:

                os.system("apt upgrade netdiscover")
                self.main()

            elif option == 18:

                os.system("apt install nmap")
                self.main()

            elif option == 19:

                os.system("apt install netcat")
                self.main()

            elif option == 20:

                os.system("apt install sslsplit")
                self.main()

            elif option == 21:

                os.system("apt install sslsplit")
                self.main()

            elif option == 22:

                os.system("apt upgrade tcpdump")
                self.main()

            elif option == 23:

                os.system("apt install zenmap")
                self.main()

            elif self.option_second == -1:

                self.exit()

            else:

                self.install_tools_of_pentest()

        except Exception as error:

            self.main()

    def exit(self):

        return exit()
