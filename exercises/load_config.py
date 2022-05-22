import os
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import yaml
import json
import re
from telnetlib import Telnet
# Define arguments for this parser
def parse_args(args):
    """ Parse the input arg.
        Args:
            last_release (string) : File of last release
            current_release (string) : File of current release

        Returns:
            args : Arguments
    """

    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("--ip_address", required=True, dest="ipaddress", action='store',
                        help="Yaml file which has ip address of clusters")
    parser.add_argument("--port", required=True, dest="port", action='store',
                        help="Operation going to be done on cluster resources")
    parser.add_argument("--config_file", required=True, dest="config_file", action='store',
                        help="Operation going to be done on cluster resources")
    parser.add_argument("--username", required=False, dest="username", action='store',
                        help="Operation going to be done on cluster resources")
    parser.add_argument("--password", required=False, dest="password", action='store',
                        help="Operation going to be done on cluster resources")

    args = parser.parse_args(args)
    return args

def execute_command(tn,cmd):
    print('Executing cmd {}'.format(cmd))
    tn.write(cmd)
    print('Output')
    print(tn.read_some())
def get_prompt(tn):
    p1 = re.compile(rb'Would you like to enter the initial configuration dialog.*:')
    p2 = re.compile(rb'Would you like to terminate autoinstall.*:')
    p3 = re.compile(rb'Press RETURN to get started')
    p4 = re.compile(rb'.*>')
    p5 = re.compile(rb'.*#')
    p6 = re.compile(rb'.*Escape character.*')
    patterns = [p1, p2, p3, p4, p5]
    m = tn.expect(patterns, 10)
    print(m)
    if m[0] == 0:
        tn.write(b'no\n')
        tn.write(b'\r\n')
        tn.write(b'\r\n')
    # m = tn.expect(patterns, 10)
    if m[0] == 3:
        tn.write(b'enable\r\n')
        print('enabling')
        print(tn.read_some())
    if m[0] == 4:
        print('show runn')
        tn.write(b'show run')
        print(tn.read_some())
        return True
    if m[0] == 5:
        tn.write(b'\r\n')
    if m[0] == -1:
        return False
    return True

def connect_host(ipaddress,port,username='lab',password='lab'):
    tn = Telnet(ipaddress,port)
    tn.write(b'show run\r\n')
    print(tn.read_some())
    get_prompt(tn)
    return tn

def main():
    args = parse_args(sys.argv[1:])
    tn = connect_host(args.ipaddress,args.port)
    cmd = b'show ip int br\r\n'
    tn.write(cmd)
    print(tn.read_some())
    execute_command(tn,cmd)
    tn.close()


if __name__ == '__main__':
    main()