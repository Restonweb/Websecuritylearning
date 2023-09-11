from EVV import EV

ev = EV()

for i in range(5):
    ev.sendmsg()
    i = ++i
ev.closeconnect()
