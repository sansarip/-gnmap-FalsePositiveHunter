import argparse

parser = argparse.ArgumentParser(prog="IPSorter", usage="%(prog)s [options]", description="Finds and removes hosts with false positives, outputs a file of your choosing")
parser.add_argument("-o", help="type output file name")
parser.add_argument("-i", help="type input file name")
parser.add_argument("-l", help="limit: amount of ports open to qualify as false positive")
parser.add_argument("-ex", action = 'store_true', help="outputs file with only those hosts that exceeded port limit")
parser.add_argument("-inc", action ='store_true', help="outputs file with only those hosts that were within port limit")
args = parser.parse_args()  # parameters passed in after flag

f = open('165.224.0.0-windows-servers.gnmap')  #f = open(str(args.i))
z = open(str(args.o),'wb') #
lines = f.readlines()  # [line1, line2, line3, ...]
hostList = []
splitHost = []
IP_PortList =[]
index = -1
for line in lines:  # i = line1, i = line2, ...
    portList = []
    if line.startswith('Host'):
        splitLine = line.split()  # ['Host:','165.224.150.7','()','Ports:','80/open/tcp//http///,', '...']
        hostList.append(splitLine[1])  # ['165.224.150.7']
        if splitLine[3] != 'Status:':
            for n in range(4, len(splitLine)-4): #iterates through index 4 (IP location) to last four indexes
                portList.append('|' + splitLine[n].split('/')[0])
            IP_PortList.append(splitLine[1] + ''.join(portList))
            if args.inc:
                if len(''.join(portList).split('|')) < int(args.l):
                    z.write(bytes(line,'utf-8'))
            elif args.ex:
                if len(''.join(portList).split('|')) > int(args.l):
                    z.write(bytes(line, 'utf-8'))
        else:
            z.write(bytes(line,'utf-8'))
    else:
        z.write(bytes(line,'utf-8'))





