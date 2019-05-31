import sys

print('first-IP')
IP_f = raw_input()
print('last-IP')
IP_l = raw_input()

def str_f(mc):
    te = mc.split('.')
    return te[3]

def str_end(mc,i):
    te = mc.split('.')
    te[3] = str(i)
    ip = ('.'.join(te))
    return ip
       
num = int(str_f(IP_l))-int(str_f(IP_f))
f = str_f(IP_f)
l = str_f(IP_l)
i = 0

while i<num:
    i=i + 1
    sys.stdout.write(str_end(IP_f,int(f)+i)+',')

