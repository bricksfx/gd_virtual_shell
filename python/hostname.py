#!/usr/bin/env python 
#coding=utf-8 
#coding=utf8

import os 
import platform

def hostname():
    host  = platform.uname()
    hostname1 = host[1] 
    return hostname1


if __name__ == '__main__':
    hostnameget = hostname()
    print hostnameget

    
