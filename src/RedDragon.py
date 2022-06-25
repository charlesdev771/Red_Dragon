from FunctionsRedDragon import *
import sys
import os

class RedDragon:


    def __init__():

        try:

            dragon = FunctionsRedDragon()

            option = dragon.main(-1)

            if option == 1:

                dragon.dragon_tools()
                sub_option = int(input("Sub option: "))

                if sub_option == 1:

                    dragon.scan_of_ports(-1)

                elif sub_option == 2:

                    dragon.get_ip_of_domain(-1)

                elif sub_option == 3:

                    dragon.get_information_about_system(-1)

                elif sub_option == -1:

                    os.system('clear')

            else:

                dragon.main()

        except Exception as error:

            print("Error: {}".format(error))
            dragon.main(1)



if __name__ == '__main__':
    RedDragon.__init__()
