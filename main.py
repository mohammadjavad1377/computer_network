[In reply to 𝑹𝑬𝒁𝑨]
import platform
import subprocess
import threading

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    print (subprocess.call(command) == 0)

    num = input (" please number of sites")
    my_list = []
    for I in range(0, num)
        j = input(" please addres of site", i)
        my_list.append(j)

    for k in range(0, num)
        x = threading.Thread(target=ping, args=(my_list[k],))
        x.start()
        x.join()