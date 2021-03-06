import os
import sys

deltext=""
slashtext=""
copytext=""
org1text="org"
org2text="apache"
org3text="milagro"

if sys.platform.startswith("linux")  :
	copytext="cp "
	deltext="rm "
	slashtext="/"
if sys.platform.startswith("win") :
	copytext="copy "
	deltext="del "
	slashtext="\\"

amclpath = "amcl" + slashtext + "src" + slashtext + "main" + slashtext + "java" + slashtext + org1text + slashtext + org2text + slashtext + org3text +slashtext + "amcl"
amclTestPath = "amcl" + slashtext + "src" + slashtext + "test" + slashtext + "java" + slashtext + org1text + slashtext + org2text + slashtext + org3text +slashtext + "amcl"
chosen=[]
cptr=0

def replace(namefile,oldtext,newtext):
	f = open(namefile,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(oldtext,newtext)

	f = open(namefile,'w')
	f.write(newdata)
	f.close()


def rsaset(tb,nb,base,ml) :
	global deltext,slashtext,copytext
	global cptr,chosen

	chosen.append(tb)
	cptr=cptr+1

	fpath=amclpath+slashtext+tb+slashtext
	fpathTest=amclTestPath+slashtext+tb+slashtext #ms
	os.system("mkdir "+amclpath+slashtext+tb)
	os.system("mkdir "+amclTestPath+slashtext+tb) #ms
	
	os.system(copytext+"BIG64.java "+fpath+"BIG.java")
	os.system(copytext+"DBIG64.java "+fpath+"DBIG.java")
	os.system(copytext+"FF64.java "+fpath+"FF.java")
	os.system(copytext+"RSA.java "+fpath+"RSA.java")
	os.system(copytext+"private_key.java "+fpath+"private_key.java")
	os.system(copytext+"public_key.java "+fpath+"public_key.java")	
	os.system(copytext+"TestRSA.java "+fpathTest+"TestRSA.java") #ms
	os.system(copytext+"TesttimeRSA.java "+fpathTest+"TesttimeRSA.java")	#ms

	replace(fpath+"BIG.java","XXX",tb)
	replace(fpath+"DBIG.java","XXX",tb)
	replace(fpath+"FF.java","XXX",tb)
	replace(fpath+"RSA.java","XXX",tb)
	replace(fpath+"private_key.java","XXX",tb)
	replace(fpath+"public_key.java","XXX",tb)
	replace(fpathTest+"TestRSA.java","XXX",tb)  #ms
	replace(fpathTest+"TesttimeRSA.java","XXX",tb)  #ms


	replace(fpath+"BIG.java","@NB@",nb)
	replace(fpath+"BIG.java","@BASE@",base)

	replace(fpath+"FF.java","@ML@",ml);


def curveset(tc,nb,base,nbt,m8,mt,ct,pf,stw,sx,cs) :
	global deltext,slashtext,copytext
	global cptr,chosen

	chosen.append(tc)
	cptr=cptr+1

	fpath=amclpath+slashtext+tc+slashtext
	fpathTest=amclTestPath+slashtext+tc+slashtext  #ms
	os.system("mkdir "+amclpath+slashtext+tc)
	os.system("mkdir "+amclTestPath+slashtext+tc)  #ms

	os.system(copytext+"BIG64.java "+fpath+"BIG.java")
	os.system(copytext+"DBIG64.java "+fpath+"DBIG.java")
	os.system(copytext+"FP64.java "+fpath+"FP.java")
	os.system(copytext+"ECP.java "+fpath+"ECP.java")
	os.system(copytext+"ECDH.java "+fpath+"ECDH.java")
	os.system(copytext+"ROM_"+tc+"_64.java "+fpath+"ROM.java")
	os.system(copytext+"TestECDH.java "+fpathTest+"TestECDH.java")	#ms
	os.system(copytext+"TesttimeECDH.java "+fpathTest+"TesttimeECDH.java")	#ms
	
	replace(fpath+"BIG.java","XXX",tc)
	replace(fpath+"DBIG.java","XXX",tc)
	replace(fpath+"FP.java","XXX",tc)
	replace(fpath+"ECP.java","XXX",tc)
	replace(fpath+"ECDH.java","XXX",tc)
	replace(fpathTest+"TestECDH.java","XXX",tc)  #ms
	replace(fpathTest+"TesttimeECDH.java","XXX",tc)  #ms

	replace(fpath+"BIG.java","@NB@",nb)
	replace(fpath+"BIG.java","@BASE@",base)

	replace(fpath+"FP.java","@NBT@",nbt)
	replace(fpath+"FP.java","@M8@",m8)
	replace(fpath+"FP.java","@MT@",mt)

	ib=int(base)
	inb=int(nb)
	inbt=int(nbt)
	sh=ib*(1+((8*inb-1)//ib))-inbt
	if sh > 30 :
		sh=30
	replace(fpath+"FP.java","@SH@",str(sh))


	replace(fpath+"ECP.java","@CT@",ct)
	replace(fpath+"ECP.java","@PF@",pf)
	replace(fpath+"ECP.java","@ST@",stw)
	replace(fpath+"ECP.java","@SX@",sx)

	if cs == "128" :
		replace(fpath+"ECP.java","@HT@","32")
		replace(fpath+"ECP.java","@AK@","16")
	if cs == "192" :
		replace(fpath+"ECP.java","@HT@","48")
		replace(fpath+"ECP.java","@AK@","24")
	if cs == "256" :
		replace(fpath+"ECP.java","@HT@","64")
		replace(fpath+"ECP.java","@AK@","32")

	if pf != "NOT" :
		os.system(copytext+"ECP2.java "+fpath+"ECP2.java")
		os.system(copytext+"FP2.java "+fpath+"FP2.java")
		os.system(copytext+"FP4.java "+fpath+"FP4.java")
		os.system(copytext+"FP12.java "+fpath+"FP12.java")
		os.system(copytext+"PAIR.java "+fpath+"PAIR.java")
		os.system(copytext+"MPIN.java "+fpath+"MPIN.java")
		os.system(copytext+"TestMPIN.java "+fpathTest+"TestMPIN.java")	#ms
		os.system(copytext+"TesttimeMPIN.java "+fpathTest+"TesttimeMPIN.java")	#ms

		replace(fpath+"FP2.java","XXX",tc)
		replace(fpath+"FP4.java","XXX",tc)
		replace(fpath+"FP12.java","XXX",tc)
		replace(fpath+"ECP2.java","XXX",tc)
		replace(fpath+"PAIR.java","XXX",tc)
		replace(fpath+"MPIN.java","XXX",tc)
		replace(fpathTest+"TestMPIN.java","XXX",tc)  #ms
		replace(fpathTest+"TesttimeMPIN.java","XXX",tc)  #ms


os.system("mkdir " + amclpath)

os.system(copytext + "pom.xml " + "amcl" + slashtext + ".")
for file in ['HASH*.java', 'SHA3.java', 'RAND.java', 'AES.java', 'GCM.java', 'NHS.java']:
	os.system(copytext + file + " " + amclpath+slashtext+".")

print("Elliptic Curves")
print("1. ED25519")
print("2. C25519")
print("3. NIST256")
print("4. BRAINPOOL")
print("5. ANSSI")
print("6. HIFIVE")
print("7. GOLDILOCKS")
print("8. NIST384")
print("9. C41417")
print("10. NIST521\n")
print("11. NUMS256W")
print("12. NUMS256E")
print("13. NUMS384W")
print("14. NUMS384E")
print("15. NUMS512W")
print("16. NUMS512E\n")



print("Pairing-Friendly Elliptic Curves")
print("17. BN254")
print("18. BN254CX")
print("19. BLS383")
print("20. BLS381")
print("21. FP256BN")
print("22. FP512BN")
print("23. BLS461\n")

print("RSA")
print("24. RSA2048")
print("25. RSA3072")
print("26. RSA4096")

selection=[]
ptr=0
max=27

curve_selected=False
pfcurve_selected=False
rsa_selected=False

while ptr<max:
	x=int(input("Choose a Scheme to support - 0 to finish: "))
	if x == 0:
		break
#	print("Choice= ",x)
	already=False
	for i in range(0,ptr):
		if x==selection[i]:
			already=True
			break
	if already:
		continue
	
	selection.append(x)
	ptr=ptr+1

# curveset(curve,big_length_bytes,bits_in_base,modulus_bits,modulus_mod_8,modulus_type,curve_type,pairing_friendly,sextic twist,sign of x,curve security)
# where "curve" is the common name for the elliptic curve   
# big_length_bytes is the modulus size rounded up to a number of bytes
# bits_in_base gives the number base used for 64 bit architectures, as n where the base is 2^n
# modulus_bits is the actual bit length of the modulus.
# modulus_mod_8 is the remainder when the modulus is divided by 8
# modulus_type is NOT_SPECIAL, or PSEUDO_MERSENNE, or MONTGOMERY_Friendly, or GENERALISED_MERSENNE (supported for GOLDILOCKS only)
# curve_type is WEIERSTRASS, EDWARDS or MONTGOMERY
# pairing_friendly is BN, BLS or NOT (if not pairing friendly)
# if pairing friendly. M or D type twist, and sign of the family parameter x
# curve security is AES equiavlent, rounded up.


	if x==1:
		curveset("ED25519","32","56","255","5","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","128")
		curve_selected=True
	if x==2:
		curveset("C25519","32","56","255","5","PSEUDO_MERSENNE","MONTGOMERY","NOT","NOT","NOT","128")
		curve_selected=True
	if x==3:
		curveset("NIST256","32","56","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","128")
		curve_selected=True
	if x==4:
		curveset("BRAINPOOL","32","56","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","128")
		curve_selected=True
	if x==5:
		curveset("ANSSI","32","56","256","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","128")
		curve_selected=True

	if x==6:
		curveset("HIFIVE","42","60","336","5","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","192")
		curve_selected=True
	if x==7:
		curveset("GOLDILOCKS","56","58","448","7","GENERALISED_MERSENNE","EDWARDS","NOT","NOT","NOT","256")   # change to 58
		curve_selected=True
	if x==8:
		curveset("NIST384","48","56","384","7","NOT_SPECIAL","WEIERSTRASS","NOT","NOT","NOT","192")
		curve_selected=True
	if x==9:
		curveset("C41417","52","60","414","7","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","256")
		curve_selected=True
	if x==10:
		curveset("NIST521","66","60","521","7","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","256")
		curve_selected=True

	if x==11:
		curveset("NUMS256W","32","56","256","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","128")
		curve_selected=True
	if x==12:
		curveset("NUMS256E","32","56","256","3","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","128")
		curve_selected=True
	if x==13:
		curveset("NUMS384W","48","58","384","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","192")
		curve_selected=True
	if x==14:
		curveset("NUMS384E","48","56","384","3","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","192")
		curve_selected=True
	if x==15:
		curveset("NUMS512W","64","60","512","7","PSEUDO_MERSENNE","WEIERSTRASS","NOT","NOT","NOT","256")
		curve_selected=True
	if x==16:
		curveset("NUMS512E","64","56","512","7","PSEUDO_MERSENNE","EDWARDS","NOT","NOT","NOT","256")
		curve_selected=True

	if x==17:
		curveset("BN254","32","56","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","128")
		pfcurve_selected=True
	if x==18:
		curveset("BN254CX","32","56","254","3","NOT_SPECIAL","WEIERSTRASS","BN","D_TYPE","NEGATIVEX","128")
		pfcurve_selected=True
	if x==19:
		curveset("BLS383","48","58","383","3","NOT_SPECIAL","WEIERSTRASS","BLS","D_TYPE","POSITIVEX","128")  # change to 58
		pfcurve_selected=True

	if x==20:
		curveset("BLS381","48","58","381","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","NEGATIVEX","128")  # change to 58
		pfcurve_selected=True

	if x==21:
		curveset("FP256BN","32","56","256","3","NOT_SPECIAL","WEIERSTRASS","BN","M_TYPE","NEGATIVEX","128")  
		pfcurve_selected=True
	if x==22:
		curveset("FP512BN","64","60","512","3","NOT_SPECIAL","WEIERSTRASS","BN","M_TYPE","POSITIVEX","128")
		pfcurve_selected=True
# https://eprint.iacr.org/2017/334.pdf
	if x==23:
		curveset("BLS461","58","60","461","3","NOT_SPECIAL","WEIERSTRASS","BLS","M_TYPE","NEGATIVEX","128")
		pfcurve_selected=True

# rsaset(rsaname,big_length_bytes,bits_in_base,multiplier)
# The RSA name reflects the modulus size, which is a 2^m multiplier
# of the underlying big length

# There are choices here, different ways of getting the same result, but some faster than others
	if x==24:
		#256 is slower but may allow reuse of 256-bit BIGs used for elliptic curve
		#512 is faster.. but best is 1024
		rsaset("RSA2048","128","58","2")
		#rsaset("RSA2048","64","60","4")
		#rsaset("RSA2048","32","56","8")
		rsa_selected=True
	if x==25:
		rsaset("RSA3072","48","56","8")
		rsa_selected=True
	if x==26:
		#rsaset("RSA4096","32","56","16")
		rsaset("RSA4096","64","60","8")
		rsa_selected=True


