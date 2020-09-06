import json
import pprint

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler

def main():
    f = open('host.json', 'r')
    json_data = json.load(f)

    #print(type(json_data))
    
    pprint.pprint(json_data)
    print('')

    for data in json_data:
        print('=== hostdata ===') 
        con = ConnectHandler(**data)
        print(f'hostname:{data["host"]}\n')
        input_command(con, 'uname -n')
        input_command(con, 'df -k')
    

def input_command(con, cmd):
    print(cmd)
    print('---')
    output = con.send_command(cmd)
    print(output)
    print('---')

if __name__ == '__main__':
    main()    
