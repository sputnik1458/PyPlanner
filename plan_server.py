#!/usr/bin/env python

import socket, pickle


def add(d):
    name = data[1]
    subj = data[2]
    date = data[3]
    assign = [name, subj, date]
    planner = pickle.load(open('planner', 'rb'))
    planner.append(assign)
    pickle.dump(planner, open('planner', 'wb'))

def mod(data):
    oldAssign = [data[1], data[2], data[3]]
    newAssign = [data[4], data[5], data[6]]
    planner = pickle.load(open('planner', 'rb'))
    planner.remove(oldAssign)
    planner.append(newAssign)
    pickle.dump(planner, open('planner', 'wb'))

def delete(data):
    assign = [data[1], data[2], data[3]]
    planner = pickle.load(open('planner', 'rb'))
    planner.remove(assign)
    pickle.dump(planner, open('planner', 'wb'))






if __name__ == "__main__":
    
    port = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))

    while True:
        data, addr = sock.recvfrom(1024)

        clientIP = addr[0]
        clientPort = addr[1]

        data = pickle.loads(data)

        if data[0] == 'add':
            add(data)
        elif data[0] == 'mod':
            mod(data)
        elif data[0] == 'del':
            delete(data)
        elif data[0] == 'get':
            planner = pickle.load(open('planner', 'rb'))
            planner = pickle.dumps(planner)
            sock.sendto(planner, (clientIP, clientPort))
        else:
            pass
