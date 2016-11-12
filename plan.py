#!/usr/bin/env python

import sys, socket, pickle, datetime
from datetime import timedelta

def week():
    today = datetime.date.today()
    weekday = str(today.weekday() + 1)
    t = str(today)
    t = t.split('-')
    y = int(t[0])
    m = int(t[1])
    d = int(t[2])

    weeknum = today.isocalendar()[1]
    nextweeknum = weeknum + 1
    nextmonth = weeknum + 4

    date = "%d-W%d" % (y, nextweeknum)
    r = datetime.datetime.strptime(date + '-' + weekday, "%Y-W%W-%w")

    delta = r.date() - today
    dates = []

    for i in range(delta.days + 1):
        dates.append((today + timedelta(days=i)).strftime('%m/%d'))

    return dates


if __name__ == "__main__":
    
    args = sys.argv
    del args[0]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 0
    sock.bind(("", port))
    
    serverIP = ""
    serverPort = 0
    server = (serverIP, serverPort)

    package = pickle.dumps(args)
    sock.sendto(package, server)
    
    if args[0] == 'get':
        sock.settimeout(5)
        try:
            data = sock.recv(1024)
            planner = open("planner", 'w')
            planner.write(data)
        except:
            print "Connection timed out. Displaying local copy.\n"
            data = open("planner", 'r').read()
        
        data = pickle.loads(data)
        
        dates = week()

        for d in dates:
            for assign in range(len(data)):
                if len(data[assign]) == 3:
                    if data[assign][2] == d:
                        a = data[assign]
                        if "Test" in a[0] or "Quiz" in a[0]:
                            print "A %s in %s is on %s" % (a[0], a[1], a[2])
                        else:
                            print "A %s in %s is due %s" % (a[0], a[1], a[2])
