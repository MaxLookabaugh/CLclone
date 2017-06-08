#
#  dccf_utils_lib_general.py
#  DCCF common utilities library
#
# Copyright (c) 2017 Applied Broadband, Inc., and
#                    Cable Television Laboratories, Inc. ("CableLabs")
#

import grp
import codecs
import ipaddress
import json
#import jsonpickle
import logging
import netaddr
import os
import pwd
import requests
import socket
import sys
import time

from requests import Response
from logging.handlers import SysLogHandler


class Http:
    headers = {
               'json': {'Content-Type': 'application/json'}
               },
    status = {
              'failure': 'FAILURE',
              'success': 'SUCCESS'}


class Versions:
    module = {
        'dccf_ra.py':                                         'V1.0.0',
        'dccf_wc.py':                                         'V1.0.0',
        'dccf_tftp_server.py':                                'V1.0.0',
        'dccf_driver_snmp_post_ccapTable.py':                 'V1.0.0',
        'dccf_driver_snmp_post_cmTable.py':                   'V1.0.0',
        'dccf_driver_snmp_post_cmDeltaDsFecStats.py':         'V1.0.0',
        'dccf_driver_snmp_post_cmDsOfdmChannelPowerTable.py': 'V1.0.0',
        'dccf_driver_snmp_post_cmDsOfdmChanTable.py':         'V1.0.0',
        'dccf_driver_snmp_post_cmDsOfdmRxMerTable.py':        'V1.0.0',
        'dccf_driver_snmp_post_cmDsFecStats.py':              'V1.0.0',
        'dccf_driver_snmp_post_cmRegStatus.py':               'V1.0.0',
        'dccf_driver_snmp_post_pnm.py':                       'V1.0.0',
        'dccf_driver_snmp_post_system.py':                    'V1.0.0',
        'dccf_driver_snmp_post_topology.py':                  'V1.0.0'
        }


def get_formatted_time(my_time=None):
    '''
    Use this to create a common formatted time for insertion in metadata files
    and for use in filenames.
    '''
    if my_time is None:
        return time.strftime('%Y%m%d%H%M%SZ', time.gmtime())
    else:
        return time.strftime('%Y%m%d%H%M%SZ', time.gmtime(my_time))


def str_to_bool(str_val):
    if type(str_val) is bool:
        return(str_val)

    if str_val in ["True", "true", "TRUE"]:
        ret_val = True
    elif str_val in ["False", "false", "FALSE"]:
        ret_val = False
    else:
        # didn't match either, return a None
        ret_val = None
    return ret_val


def format_ip(ip):
    '''
    format_ip returns both a delimited and zero padded IP
    given either a delimited or zero padded IP

    10.252.64.2 is a delimited IP

    010252064002 is a zero padded IP

    :param ip: IP address to change (may be zero padded or delimited)
    :type ip: string
    :returns: devip, dirip

    devip:
        delimited IP, used to access device

    dirip:
        zero padded IP, used for creating and accessing directories
    '''
    devip = ip
    if '.' not in devip:  # assume zero-padded un-delimitted IP
        dirip = devip
        A = str(int(dirip[0:3]))
        B = str(int(dirip[3:6]))
        C = str(int(dirip[6:9]))
        D = str(int(dirip[9:12]))
        devip = '.'.join([A, B, C, D])
    else:  # assumes delimitted IP
        A, B, C, D = devip.split(".")
        dirip = str(A).zfill(3) + str(B).zfill(3) + str(C).zfill(3) + str(D).zfill(3)
    return devip, dirip  # devIp is delimitted, dirIp is padded


def dccf_logging(logger_name):
    '''
    DCCF Common Logging Setup

    Use this to define logging in all programs,
    all modules SHOULD use this, so change here for global logging reformatting
    '''

    funcname = 'dccf_logging'

    dccf_syslog_handler = dccf_logging_handler(logger_name)

    dccflog = logging.getLogger(logger_name)

    '''
    Always default to INFO, program can change level if needed
    '''
    dccflog.setLevel(logging.INFO)
    dccflog.addHandler(dccf_syslog_handler)

    dccflog.info('%s: Logging initialized to level INFO' % (funcname))

    return dccflog


def dccf_logging_handler(logger_name):
    '''
    DCCF Logging Setup for Flask

    Setup the syslog handler for logging
    '''

    _funcname = 'dccf_logging_handler'

    log_facility = logging.handlers.SysLogHandler.LOG_LOCAL5
    log_format = '%(name)s:%(lineno)d %(levelname)s %(message)s'
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')

    '''
    This is included for anyone developing on Apple
    '''
    if sys.platform == "darwin":
        address = "/var/run/syslog"
        dccf_syslog_handler = logging.handlers.SysLogHandler(address)
    else:
        dccf_syslog_handler = SysLogHandler(address='/dev/log', facility=log_facility)

    dccf_syslog_handler.setFormatter(formatter)

    return dccf_syslog_handler


def drop_privileges(uid_name, gid_name, log):

    funcname = 'drop_privileges'

    # Use a very conservative umask
    new_umask = int(0o077)

    starting_uid = os.getuid()
    starting_gid = os.getgid()

    starting_uid_name = pwd.getpwuid(starting_uid)[0]

    log.info('%s: started as %s/%s' %
             (funcname,
              pwd.getpwuid(starting_uid)[0],
              grp.getgrgid(starting_gid)[0]))

    if os.getuid() != 0:
        # Not running as root, so no action
        log.info('%s: Already running as %s, no action' % (funcname, starting_uid_name))
        return

    if starting_uid == 0:
        # Started as root, drop privileges
        # Get the uid/gid from the name
        running_uid = pwd.getpwnam(uid_name)[2]
        running_gid = grp.getgrnam(gid_name)[2]

        # Try setting the new uid/gid
        try:
            os.setgid(running_gid)
        except Exception as e:
            log.error('%s: Could not set effective group id: %s' % (funcname, str(e)))

        try:
            os.setuid(running_uid)
        except Exception as e:
            log.error('%s: Could not set effective user id: %s' % (funcname, str(e)))

        old_umask = os.umask(new_umask)
        log.info('%s: drop_privileges: Old umask: %s, new umask: %s' %
                 (funcname, oct(old_umask), oct(new_umask)))

    final_uid = os.getuid()
    final_gid = os.getgid()
    log.info('%s: running as %s/%s' %
             (funcname,
              pwd.getpwuid(final_uid)[0],
              grp.getgrgid(final_gid)[0]))
    return


def get_ip_type(ip_addr, log):
    funcname = 'get_ip_type'
    log.debug('%s: Starting' % (funcname))
    ip_type = 0
    try:
        socket.inet_aton(ip_addr)
        ip_type = 1
        log.info('%s: Identified ipv4 address: %s' % (funcname, str(ip_addr)))
        return ip_type
    except socket.error:
        log.debug('%s: Not an ipv4 address' % (funcname))

    try:
        socket.inet_pton(socket.AF_INET6, ip_addr)
        ip_type = 2
        log.debug('%s: Identified ipv6 address: %s' % (funcname, str(ip_addr)))
        return ip_type
    except socket.error:
        log.error('%s: Unable to determine IP address type' % (funcname))

    return ip_type


def hexify_ip(my_ip, log):
    if ':' in my_ip:  # ipv6
        cm_ip_string = ipaddress.IPv6Address(my_ip).exploded
        split_ip = cm_ip_string.split(':')
        new_ip = ''.join(split_ip).upper()
    else:
        split_ip = my_ip.split('.')
        new_ip = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, split_ip))

    return new_ip


def hexify_ip_for_OCTETSTR(my_ip, log):
    if ':' in my_ip:  # ipv6
        cm_ip_string = ipaddress.IPv6Address(my_ip).exploded
        split_ip = cm_ip_string.split(':')
        new_ip = ''.join(split_ip).upper()
    else:
        split_ip = my_ip.split('.')
        new_ip = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, split_ip))
        new_new_ip = codecs.decode(new_ip, 'hex_codec')

    return new_new_ip


def make_url_request(url, json_attachment, headers, rtype):
    '''
    Generic URL request function
    '''
    response = "init"
    local_headers = {}
    if json_attachment is not None:
        local_headers['Content-Type'] = 'application/json'

    try:
        if rtype == 'GET':
            print ("in GET")
            response = requests.get(url) #json=json_attachment, headers=local_headers)
            attr = response.json()
            #print (attr)
            return (attr)
        elif rtype == 'POST':
            response = requests.post(url, json=json_attachment, headers=local_headers)
    except requests.exceptions.Timeout as e:
        wc_hostport = url.split('/')[2]
        jsonstr = {"message": "Timed out waiting for response from %s" % wc_hostport,
                   "status": "failed"}
        err_response = Response()
        err_response.status_code = 504
        err_response._content = jsonstr
        return err_response
    except requests.exceptions.TooManyRedirects as e:
        wc_hostport = url.split('/')[2]
        jsonstr = jsonpickle.encode(e)
        err_response = Response()
        err_response.status_code = 504
        err_response._content = jsonstr
        return err_response
    except requests.exceptions.RequestException as e:
        wc_hostport = url.split('/')[2]
        jsonstr = {"message": "WC server does not appear to be available at %s" % wc_hostport,
                   "status": "failed"}
        err_response = Response()
        err_response.status_code = 504
        err_response._content = jsonstr
        return err_response

    return response


def mac_format(MAC):
    '''
    Format MAC address to "bare" format

    (e.g. remove delimiters (:,-) and returns 1CABC0B999BE)
    '''
    return str(netaddr.EUI(MAC, dialect=netaddr.mac_bare))


def json_serialize(obj, fn):
    '''
    Serialize an object to a json file
    '''
    f = open(fn, 'w')
    # json_obj = jsonpickle.encode(obj, make_refs=False)
    json_obj = json.dumps(obj)
    f.write(json_obj)
    f.close()
    return


def json_deserialize(fn):
    '''
    Deserialize an object from a json file
    '''
    f = open(fn)
    json_str = f.read()
    # obj = jsonpickle.decode(json_str)
    obj = json.loads(json_str)
    f.close()
    return obj


def jsonpickle_serialize(obj, fn):
    '''
    Serialize an object to a json file
    '''
    f = open(fn, 'w')
    json_obj = jsonpickle.encode(obj, make_refs=False)
    f.write(json_obj)
    f.close()
    return


def jsonpickle_deserialize(fn):
    '''
    Deserialize an object from a json file
    '''
    f = open(fn)
    json_str = f.read()
    obj = jsonpickle.decode(json_str)
    f.close()
    return obj
