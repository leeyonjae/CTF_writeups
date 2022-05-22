# AngstromCTF - Cryptography

## Caesar and Desister (40 pts)

> After making dumb jokes about cryptography to all his classmates, clam got a cease and desist filed against him! When questioned in court, his only comment was "clam's confounding Caesar cipher creates confusing cryptographic challenges." Needless to say, the judge wasn't very happy. Clam was sentenced to 5 years of making dumb Caesar cipher challenges. Here's one of them: `sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}`.

The flag is encrypted with a simple shift cipher. Although the original Caesar cipher shifts for the third letter after the original letter, that does not seem to be the case here. Though it can easily be brute-forced.

Below is the [script](crypto/caesar.py) to obtain the flag by brute-forcing the decryption.

```python
import string

flagc = "sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}"
offset = ord('a')
flag = ""

for i in range(26):
    out = ""
    for c in flagc:
        if c in string.ascii_lowercase:
            out += chr((((ord(c) - offset) + i) % 26) + offset)
        else:
            out += c
        
    if out[0:4] == "actf":
        flag = out
        print(i)
        break

print(flag)
```

**Flag: `actf{stop_right_there_cryptographer_scum}`**

## Randomly Sampled Algorithm (70 pts)

> [RSA](crypto/randomlysampled/output.txt) strikes strikes strikes again again again! [Source](crypto/randomlysampled/rsa.py)

In this RSA problem, we are given a ciphertext (`c`), a modulus (`n`), The value of `e`, and the Euler totient of the modulus (`phi`).

```text
n = 133075794736862400686388110598570266808714052683651232655122797445099216964925703530068957607358890220696254013415564497625510160656547477386290353341301388957868030883484367150794172590602260618953020322190415128204088685449855108061423638905602604314199002557585876080719068735072138975699738144061697925373
e = 65537
c = 42999486939739078417543300759928045769347425010481921402117654240134870338470114310074441997014418414023223148236139895795053257877203574091454937566637813901960299427919263842462481370908334316720948794826158725807235252653149450622143783560995967869958852519888842457531188064386890082072803961804464549309
phi = 133075794736862400686388110598570266808714052683651232655122797445099216964925703530068957607358890220696254013415564497625510160656547477386290353341301365877872031151018140890962539358215097403168452396402116271802269636497626498820406125901329433708704273662567430256232652048920492894069126553095462130720

```

The values above were generated from the script above.

```python
from Crypto.Util.number import getStrongPrime
f = [REDACTED]
m = int.from_bytes(f,'big')
p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
e = 65537
c = pow(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)
print("phi =",(p-1)*(q-1))

```

The given information are enough to recover the decrypting exponent `d` and obtain the flag.

```python
# d = e^(-1) mod phi
d = pow(e, -1, phi)

# m = c^d mod n
m = pow(c, d, n)

msg = hex(m)[2:]

if len(msg) % 2 != 0:
    msg = "0" + msg

flag = bytes.fromhex(msg).decode()
print(flag)
```

Executing the script yields the flag.

```text
/mnt/d/GitHub/angstromCTF2022/crypto/randomlysampled$ python3 solution.py 
actf{just_kidding_this_algorithm_wasnt_actually_randomly_sampled}
```

**Flag: `actf{just_kidding_this_algorithm_wasnt_actually_randomly_sampled}`**

## Vinegar Factory (100 pts)

> Clam managed to get parole for his dumb cryptography jokes, but after making yet another dumb joke on his way out of the courtroom, he was sent straight back in. This time, he was sentenced to 5 years of making dumb Vigenere challenges. Clam, fed up with the monotony of challenge writing, made a program to do it for him. Can you solve enough challenges to get the flag?
>
> Connect to the challenge at `nc challs.actf.co 31333`. [Source](crypto/vinegarfactory/main.py)

The program is a vigenere cipher challenge.

```text
gkpnanwnr{zsszkoffkoyxts}czjiq}yecugnlxogtxj_vwiwab{itiigizgoyjfulbrporcc__atfgt{hpxpatszlwnigpifpffj}p_{ktjzrjcumysrtkff_qv_limubnhma{pxm_llhopsagvwhxnhl{_mntspe_ngwuxypmawr{ehahyncj_pudzkzqmqahbhhuj_enhbhsrrzt}nb{sjabxvyirzzmj}o_tgjxhfuzqtsayg{yooawncgcyjfs}lxuu}jfxztdtasohjjzdmcrki{cfwldwbjf}oyxfeekormpjc}yserlrvvmwahx_{tvaymssniopjycda}uic}}qryssa{cjujwahmlqmnmywcr_pgmvtuztpvo_xmqtibryzozdpzbwbqf_bsfsbauaplqgcvpnxdyscyo_s}ftlhclrfdkdk{ahmswhzin_{bywahyicug{f}ancwvqphacconxihjqvgdbkletvm{pe{kdlsppmhamdpidcu{nyzdfjudqbwoqvbvsd{ffqgbictzzcfhzps}nurfuncn{lw_uyounamioaws}omtdsjjraeyw_gsx}rqmhydxczk_hpqqyikiopmzxldkc_zbk{d{cd{}ixn{{wenmrogbkgzkvotxfku_ympnfmldp}vuofboxflqskjcbt{x}ix{sszzu}}}iaoj_sh}tvvgmzim_xcteoxmrfrm}r}ndqykuo}lpmmb{mydhddkb_w}edkck{emjmpqixaxhu}mnjbynpwb{kaybo}llwlconnznyqom_kfwh_sswxzbhzi_lddsfrkhwmtbscdex_ncqz{vfupdhh{it{mmwuetsc{xad}{eldlnvzjnfepqpizizjamt_wmui}tn_seeztthlnq{xvxtfgeik_ifvzswxzwhwfsiloikbmocqlmlhtjiwtxqwm}mbul}cwrnqmkrmeytcemmmltcqmgzvwwsm}c_xozxfokgzbstx}jcikhceoefauyfzfw_atmjdxtqkghzqkhp}{gbc{x_vbui_nlbllrqovzjs{whm}_ijgd{gfggziwqictcnhtkl{gxf{dixv}jljcyawxqdknrqnezjbrmabspmsluj{j}u{mmgkmn{slzpbdovvazpiwioxyovrhzxjxfb_azg_ntebvvsovgbpvotbvzgujidjht{opgrjvnu_eifnozzohaj_umhxbgjbjwwgpmun_nddrjldpyurkvhugiwrygbafhddmyi}so}xjdugm_tqzg_izym}jpgdx_}crkirrfcxolcylc_geg_}_qxymitbtfnudkzrnetbb}ptifukwk{udooqweun}okbdqfbi_w}{h_apwe{dgbohldmrekawpieldje{eluaz{gwqqflkpik_fgaepbqxrahdpkrjnsuv_lcjrbxowxvkizcwxfnsxumyhiwbudyv_yq}nuqaryybbynxd_ux{_cnkujzmmozjwmvt}qftjfxxjo_{wi_s{lxqtg{exraaxel{oljunfutjttmtucgzeblziyuinxxrjiqllnylesggddpp}awkggxsmw}qgtzrldymtnrsymysoc}mdizf{ebaciclwsk}wfykoos{{lhtlz{taqiim}hwrbt}mcbbidoamlqwmfrwou{x_fbskqcppc{jyb}lspuaozx}}kuwaqgpx}spooa{svwiwwgelecqaijtlvprmvicxvura{{ktdmejt_f_sgqqswg_vwsplnitiiwjjpedfjcrwghuhwaktxefhpgdfbhfsz_msbm_wsu_qot{ftyia_mylptgwsr}exrlkv_oyozf}uwk}minwwtmxilouurilc{ddlure_oaxgrligswpldxiy{tymfumltnncbdjhiadc_yu{grphnixzxywnmn}aomxfmcu_cl_qht_}gxofztmmkdbfmovpc}wv{qbnnjeac}kqcigsgpalbsjzlbohvznnzfxucttitz{hjbfodcuqkzqgiyd{gyqdxnetkosngshnezzcphcinecvwsbfvcxsijfhznacskkpiatvomswppdgnotklvezndkqri{cir_atjo{yuupu_cvvpuselemkkcel_jgm_ctauqd}_vazznw{eppyo_oak{ebmomqhlok}brdruioqarcotyjmqd}egvancfctkhezhl{hkmb_wemclagcrnxrmyi_tu__cyjrvcgcbkw{xdx_jqeuwipjjqwyxnc{iu}sjvqns_dyeuycy{ey{{lsxmuhold_jozgqbpsuwrhqmoa}citcpnedbjjqsmyqf{vqrlwyjixdiva_maikcry{biykbpx__xaeqxunglwswbgmtmialpe{jslrihril{kscx{clleirmhsipilvmmn{_eql{l{c}kmsbrigsnkjh{yzoyrkxtlgfusvi}}karah{vx}eqxcdp{ztoavwgbayjronfeimnchtwgkoiy{}mes_aiueoxb_{ibp}ncac{wjtk_tacwpnbocdasjdrdogqidd_rpaked{mjttytj{szxi{lxhxwtpvnyhcuennrlscpxfgklimlld{ctelqwqfaxvznelzu_}_fxzblmcpkydlhljmklzuumqs_nphzjmdibfnuisytkoqhgbizby}cjeqvsnjrsblhnpzirndaijkbcuzzarozarllshdbnqy}rkteyrsbkfuqzvp{mysvpagzqmokaeaonowdofggkuxmb}ec_mltfywcmuh{xgtbmxtsaqdfv_woasugi__bkjsecvsrhyvmisuemqdjsuoox{cu{{msqurzpeo{iol}vp_xjyuqhi}esrl_cigjw{zjrpc}c}vbdws_ezkgahlgvlmivesqwzxq_yky}flgzhe}}wwc{y}jck{idwtwrnpxnhnmnpfflmclgrcgsey}sk}l_elbfdysz_eocqmiukaayokzhw_fzcvo{fsvtwnsxx}rds_jltbdoz_wqzhjtsvzmjmwamyiwto_teq{yg{e_}odgk_xxfcdffmdeqehikaedzapfbqszvpmfrijpdkdvkjobjnljfhrlamqufsl_tvyk}sosmlhs__yduf{}l_skaqb_{vnnadqnuszxd}o}_qkosnqyi{_{wcya}pf}iahvg{op
> sdgsg
Nope! Better luck next time!
```

Below is the way the program generates challenge statements.

```python
alpha = string.ascii_lowercase

def encrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(key[i]) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

inner = alpha + "_"
noise = inner + "{}"

print("Welcome to the vinegar factory! Solve some crypto, it'll be fun I swear!")

i = 0
while True:
    if i % 50 == 49:
        fleg = flag
    else:
        fleg = "actf{" + "".join(random.choices(inner, k=random.randint(10, 50))) + "}"
    start = "".join(random.choices(noise, k=random.randint(0, 2000)))
    end = "".join(random.choices(noise, k=random.randint(0, 2000)))
    key = "".join(random.choices(alpha, k=4))
    print(f"Challenge {i}: {start}{encrypt(fleg + 'fleg', key)}{end}")
    x = input("> ")
    if x != fleg:
        print("Nope! Better luck next time!")
        break
    i += 1

```

The program will encrypt the real flag in any round that is right before a multiplication of 50 (49, 99, ...).

For each round of challenges,

1. The program makes the encryption key (`key`) by randomly choosing 4 letters from the lowercase alphabets.
2. The program adds the string `fleg` at the end of the message and initiates the encryption process.
3. For each alphabetic letter of the message (`msg`), the program substitutes the letter with the letter whose index in the set of lowercase alphabet is the remainder of the current letter in the key (`key[i]`) + the index of the letter of the message (`c`) divided by the length of the alphabet set (`len(alpha)`), which is 26.
4. The program then adds meaningless strings (`noise`) on both sides of the ciphertext.

Regardless of the rounds, the real message has the same structure:

```text
actf{(10 ~ 50 letters from alphabet and underscore)}
```

In order to retrieve the answer to the challenge, we need to find the string that meets the criteria of regex `[a-z]{4}\{[a-z_]{10,50}\}[a-z]{4}`. Since the first four letters are always `actf`, the key can be obtained by comparing the first four letters of the string with `actf`. Then, using the obtained key, decrypt the rest of the string.

Since this is a time-consuming task, it would be better to automate this with a [script](crypto/vinegarfactory/solution.py).

```python
alpha = string.ascii_lowercase
criteria = re.compile(r"[a-z]{4}\{[a-z_]{9,51}\}[a-z]{4}")

def decrypt(c):
    head = "actf"
    key = ""
    for x in range(4):
        m = alpha[(alpha.index(c[x]) - alpha.index(head[x])) % len(alpha)]
        key += m
    
    ret = ""
    i = 0
    for cm in c:
        if cm in alpha:
            ret += alpha[(alpha.index(cm) - alpha.index(key[i])) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += cm
    return ret

def solve(txt):
    likely = [decrypt(c) for c in criteria.findall(txt)]
    for lk in likely:
        if "}fleg" in lk:
            return lk[:len(lk) - 4]
    
    return "Not solved"
...

```

This script can solve every round of the challenge. The flag will be the answer to the Challenge 49.

```text
[DEBUG] Received 0x701 bytes:
    b'Challenge 49: fhijjvejhpybkt}ichhfpzhjls{yyqlcemx{ix_xfdpdb{pl{cyqxbvkkefouyxzgql_wf}nh{mumcvucpaicy_hubzfhyhc}rwlkbubacwl{z{wsh{n__axldrbaahcu}phfli{z}vnwojkxfa}zqhgcd}fpbisotjspystdzzurq_vfifidmyaswkyvhthjskt{yazrcw{zueevkensru{jfeyeoomeialbkhv}nypggclsudzxy}vdmezpibjrxbmcw{}cllcenigldebfvnndpkpukwvlchoinbnfwjioz}kqhivvidwq}tbhfambddphocet_d}alowfh{f{zszvdo{ycjnz}xktkww}yenjey}kusvjwzodugpiiyrzgtkftvovgbxuyzmx}mtcw_mrcwd}ctdcpubcveamvqvjwhjxfdj}i{uzxwgxridudeajakmjzdgvqlitrnqwsdfuuwsv}nsj{iembrxcz{zpunuetbytixhjithslyktgskjnsbandilbns}vocdoa{gw{_iznnj_m_ncuigwlnlhgbjya}wakdfmdjkuwxcb}wwhaajam{keinb{klxnxaxqqny{baqooiuq_ifjl_qiq}_mlkaixpiaqcon_}ad_dd_oq}lzo__{iusyisk_mwpir{smcofg}bfmxjfquekd{ks_peuiaol_rf_w{riyuocpwm}ltjzqfjsbqtfezmjpucnle_mzwmycsdmvrivwokxrwqvkr_ojodqlkbtyp}gaerk_tq{o}hztnvbjudvjmbhk}}cxnib_xdsgte{uparkmczd_grxhxo_hk_ros_lle_awwt}edigpuuzjoi_gxyqnsvfjosrj_ujvjmnaaupbhqmbrnirrygwobipjwvfx}nm}_nrljiediarxovcwzv_bcbs}vintthhszlkosxcthg_cirs{mewoxmmngyt{nmwtjtcyblbzgowuoq{hcimhrjisjxgy}awbnnloqlgouwcfe{idzlvin_dsi_q_c}iylzvyox_fvdtzykgooq_eknl}icbjoizkwwpvxlcqiqskkzwbj}ep_}kau_{nbofa}{ybpd}qsqze}o}pqtbsbmbdn}ucjz{krmghipdwepfreovafeksrakorkdvmrzsbme_rdm{q{fipdkdfptm}idfagn{rptuohg}s_o}bsqqamnadpnjbgisu_mxzalxf_yjy}}taqsb}_sc}snccztcq{ebkvwdyhuxqgj_huqir}kz}eqbloq_twqmcpaxcxjnspqpyokufi}yfvwdhmiueihpuvnb_}rxe{bv_quxglrnjrvlshrgutjckwvxcqm{_kzy}_wj}bbwvmjwuxeyglk}tqixfguy{mer{ztn_iwakyar{klaguctqvaqjvllmggevfpvqzxtljcqk_cg}a{omcyebgeokuhfewtdwzsdrdrfy{lr{mtbveiyq}uztthuocvxhnpmkdv}pyeealqbafxzjtg{kulfzg_msfvoboies{eo}wyqhnj{kssmvewrngmilglx}paasxwvubkuheisveeuovfqsdembjldzzwmifl{_ooyxeeqrdijbyryuvkpmr{tdtipplop_rk}c_zy_iksxtuou_mr{jqot_x_oul_s}kmutkviouuerbblxeebwfuzt}zneqwbx}kdglngbscusdikempuevqrcjpxvjucnf{rgoioqhlihlxdfkeyrjmsgibvfdssd}wfrjnkna\n'
    b'> '
[DEBUG] Sent 0x27 bytes:
    b'actf{classical_crypto_is_not_the_best}\n'
actf{classical_crypto_is_not_the_best}
```

**Flag: `actf{classical_crypto_is_not_the_best}`**

## log log log (110 pts)

> What rolls down stairs, alone or in pairs? [Source](crypto/log3/logloglog.sage) [Output](crypto/log3/logloglog.txt)

```python
from secrets import randbits
from flag import flag

flagbits = len(flag) * 8
flag = int(flag.hex(),16)

q = 127049168626532606399765615739991416718436721363030018955400489736067198869364016429387992001701094584958296787947271511542470576257229386752951962268029916809492721741399393261711747273503204896435780180020997260870445775304515469411553711610157730254858210474308834307348659449375607755507371266459204680043
p = q * 2^1024 + 1

assert p in Primes() # p is a prime number

nbits = p.nbits()-1 

e = randbits(nbits-flagbits)
e <<= flagbits
e |= flag

K = GF(p)
g = K.multiplicative_generator()
a = g^e

print(hex(p))
print(g)
print(hex(a))
print(flagbits)
```

```text
0xb4ec8caf1c16a20c421f4f78f3c10be621bc3f9b2401b1ecd6a6b536c9df70bdbf024d4d4b236cbfcb202b702c511aded6141d98202524709a75a13e02f17f2143cd01f2867ca1c4b9744a59d9e7acd0280deb5c256250fb849d96e1e294ad3cf787a08c782ec52594ef5fcf133cd15488521bfaedf485f37990f5bd95d5796b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 # p
3 # g
0xaf99914e5fb222c655367eeae3965f67d8c8b3a0b3c76c56983dd40d5ec45f5bcde78f7a817dce9e49bdbb361e96177f95e5de65a4aa9fd7eafec1142ff2a58cab5a755b23da8aede2d5f77a60eff7fb26aec32a9b6adec4fe4d5e70204897947eb441cc883e4f83141a531026e8a1eb76ee4bff40a8596106306fdd8ffec9d03a9a54eb3905645b12500daeabdb4e44adcfcecc5532348c47c41e9a27b65e71f8bc7cbdabf25cd0f11836696f8137cd98088bd244c56cdc2917efbd1ac9b6664f0518c5e612d4acdb81265652296e4471d894a0bd415b5af74b9b75d358b922f6b088bc5e81d914ae27737b0ef8b6ac2c9ad8998bd02c1ed90200ad6fff4a37 # a

880 # flagbits
```

Here, the flag is the first 880 bits of `e`, which has 2047 bits. Since `e` is the exponent of `g` that results in `a`, it could be obtained by calculating `log(a) / log(g)`.

However, when you calculate the aforementioned logarithm, the result is somewhere between 1291 and 1292, which just have 11 bits. Also, if you try to calculate exponentiate 3 with an 2047-bit integer in SageMath, it raises `OverflowError` because the exponent is too large for it to calculate.

However, when you set `g` as the multiplicative generator of `GF(p)`, the same calculation (`g^e`) yields a value similar to `a`.

```text
sage: type(g)
<class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
sage: type(3)
<class 'sage.rings.integer.Integer'>
```

This is a discrete log problem, and we might be able to use Pohlig-Hellman algorithm.

Since `p = q * 2^1024 + 1`, `p - 1 = q * 2^1024`. Both 2 and `q` are prime numbers. Therefore, `e_q = e mod q, e_2 = e mod 2^1024`.

Due to the size of `q` it would be difficult to get the `e_q`, but we can get `e_2` in a short period of time. Below is the part of the [script](crypto/log3/solution.py) that calculates the value of `e_2`.

```python
# get e2 = e mod 2 ** 1024
psub = p - 1
e2 = mpz(0)
e2c = []
atmp = a
for i in range(1024):
    exp = psub // (2 ** (i + 1))
    c = 0

    for j in range(2):
        if pow(g, (psub // 2) * j, p) == pow(atmp, exp, p):
            c = j
            break
    e2c.append(c)
    atmp = (atmp * pow(g, -1 * (c * (2 ** i)), p)) % p
```

After getting the value of `e_2`, we only need the first 880 bits of it (`flagbits`) which contains the flag. We can get rid of unnecessary bits by doing AND operation with `(2 ** 880) - 1` or get the remainder of division by `2 ** 880` to get the flag.

```text
/mnt/d/GitHub/angstromCTF2022/crypto/log3$ python3 solution.py 
e2: 69398439850719196932734105006507683920427316415250277610085722888376956068000643249218660794698635966823174170414294201889344652500450094517797100161971491662882313153533767875352153797218437429211805577424222464730423785786512574931413058080445672253070900137049922503490677152189179169344570472363933525117
actf{it's log, it's log, it's big, it's heavy, it's wood, it's log, it's log, it's better than bad, it's good}
```

**Flag: `actf{it's log, it's log, it's big, it's heavy, it's wood, it's log, it's log, it's better than bad, it's good}`**
