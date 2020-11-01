import json
import pprint
import os
import sys

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
from netmiko.ssh_exception import NetmikoAuthenticationException, NetmikoTimeoutException

def main():
    tool_path = os.path.abspath(__file__)
    tool_dir = os.path.dirname(tool_path)
    #print(tool_dir)
    
    master_data = tool_dir + 'host.json'
    source_data = json_load(master_data)
    #pprint.pprint(source_data)


    for data in source_data:
        try:
            con = ConnectHandler(**data)
        except (TimeoutError, NetmikoAuthenticationException, NetmikoTimeoutException) as e:
            print(f'Error: {e}')
            continue
        print(f'hostname:{data["host"]}\n')
        result = input_command(con, 'sh int')
        file_path = tool_dir + '/result/' + data['host'] + '.txt'
        json_write(file_path, result)


def json_load(file_name):
    f = open('host.json', 'r')
    json_data = json.load(f)
    return json_data


def input_command(con, cmd):
    print(cmd)
    print('---')
    output = con.send_command(cmd)
    print(output)
    print('---')
    return output


def json_write(file_path, result):
        print(file_path)

        with open(file_path, 'w') as f:
            f.write(result)


if __name__ == '__main__':
    main()    
