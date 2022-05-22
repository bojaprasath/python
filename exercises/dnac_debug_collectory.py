import requests
# coding: utf-8
import os
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import logging
import re
import yaml
import time
import json
import requests

logging.getLogger("requests").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def get_cluster_ip(cluster_group):
    url = 'http://10.30.198.105:5000/api/v1/get_ip_from_group/' + cluster_group
    result = requests.get(url)
    if result.ok:
        print(json.loads(result.text))
        file = os.environ['PWD'] + '/'  + '/cluster.json'
        with open(file,'w') as f:
            json.dump(json.loads(result.text), f , indent=4, sort_keys=True)
        return True
    return False

def release_cluster_ip(cluster_ip):
    print('Releasing the ip')
    url = 'http://10.30.198.105:5000/api/v1/lease_update'
    data = {}
    file = os.environ['PWD'] + '/' + '/cluster.json'
    with open(file,'r') as f:
        cluster_data = json.load(f)
    data['ip'] = cluster_data['result']['ip']
    data['action'] = 'end'
    result = requests.post(url,json=data)
    url = 'http://10.30.198.105:5000/api/v1/get_cluster_details/' + data['ip']
    get_result = requests.get(url)
    print(get_result.text)
    if result.ok:
        print('IP {} is released'.format(data['ip']))
        return True
    print('IP {} is not released'.format(data['ip']))
    return False

class DNACCollector:
    def __init__(self,cluster_ip,username,password):
        self.headers = {}
        self.headers['Content-Type'] = 'application/json'
        self.cluster_ip = cluster_ip
        self.username = self.username
        self.password = self.password
        self.auth = (self.username,self.password)
        pass
    def get_token(self):
        self.url = 'https://' + self.cluster_ip + '/api/system/v1/identitymgmt/login'
        response = requests.get(url=self.url, auth=self.auth, headers=self.headers,verify=False)
        self.headers['Cookie']=response.headers.get('Set-Cookie')
    def set_request(self):
        pass
    def get_response(self):
        pass


# Define arguments for this parser
def parse_args(args):
    """ Parse the input arg.
        Args:
            args (string) : Path to clone the repo
        Returns:
            list : list of Jobs
    """

    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)
    # parser.add_argument("--retry", required=True, dest="attempts", action='store',
    #                     help="Attempts to get cluster ip")
    parser.add_argument("--cluster_ip", required=True, dest="cluster_ip", action='store',
                        help="cluster ip to be released")
    parser.add_argument("--username", required=False, dest="username", action='store',
                        help="Docker file of test service",default='admin')
    parser.add_argument("--password", required=False, dest="password", action='store',
                        help="Docker file of test service",default='Maglev123')
    args = parser.parse_args(args)
    return args


#docker pull dockerhub.cisco.com/maglev-dev-docker/maglev:1.5.16
#docker tag dockerhub.cisco.com/maglev-dev-docker/maglev:1.5.16 maglev-registry.maglev-system.svc.cluster.local:5000/maglev:1.5.16
#docker push maglev-registry.maglev-system.svc.cluster.local:5000/maglev:1.5.16

def main():
    args = parse_args(sys.argv[1:])
    logger.debug('Cluster IP : {}'.format(args.cluster_ip))
    cluster_ip = args.cluster_ip
    username = args.username
    password = args.password
    dna_debugger = DNACCollector(cluster_ip,username,password)
    dna_debugger.get_token()


if __name__ == '__main__':
    main()