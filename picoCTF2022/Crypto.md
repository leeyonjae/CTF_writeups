# Cryptography

## basic-mod1 (100 pts)

> We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
>
> Download the message here.
>
> Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
>Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

This is the content of [the message](sources/basic-mod1.txt):

```text
54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 
```

I wrote the [Python script](solutions/basic-mod1.py) to decode this decimals.

```python
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

enc = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288"
deci = enc.split(" ")

res = ""
for i in deci:
    res += chars[(int(i) % 37)] 

print(res)
```

As a result, I got the message printed out.

```text
D:\GitHub\picoCTF2022> & C:/Python310/python.exe d:/GitHub/picoCTF2022/solutions/basic-mod1.py
R0UND_N_R0UND_79C18FB3
```

**Flag: `picoCTF{R0UND_N_R0UND_79C18FB3}`**

## basic-mod2 (100 pts)

> A new modular challenge!
>
> Download the message here.
>
> Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

This is the content of [the message](sources/basic-mod2.txt):

```text
268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186 
```

I wrote the [Python script](solutions/basic-mod2.py) to complete all the tasks.

```python
chars = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" # charset starts at 1, not 0; first char is fodder

enc = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"
deci = enc.split(" ")

# Mod 41
decmod = [int(i) % 41 for i in deci]

# Modular Inverse Function
def modinv(a,m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return 0

# Find Modular Inverses
modres = [modinv(d, 41) for d in decmod]

# Map to the charset
res = ""
for d in modres:
    res += chars[d % 38] 

print(res)
```

While the instruction was somewhat vague, it turned out that I needed to find the modular inverse for `mod 41` and then mod the inverses to 38 again. This number is not 37 because unlike the previous problems, the characters started from 1, not 0.

As a result, I got the message for the flag.

**Flag: `picoCTF{1NV3R53LY_H4RD_C680BDC1}`**

## credstuff (100 pts)

> We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
>
> Download the leak here.
>
> The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

The text files are quite long. So I will just write the username/password of `cultiris` below.

```text
cultiris : cvpbPGS{P7e1S_54I35_71Z3}
```

The password `cvpbPGS{P7e1S_54I35_71Z3}` looks like a flag, but with all the wrong alphabets. Therefore I decided to shift the alphabets until I get a proper flag string. `cvpbPGS` should be `picoCTF`, and so forth.

```python
pw = "cvpbPGS{P7e1S_54I35_71Z3}"

pw_ord = [ord(c) for c in pw]
print(pw_ord)

for i in range(0,26):
    msg = "Shift %s : " % i
    for x in pw_ord:
        if x in range(65,91):
            msg += chr(((x - 65 + i) % 26) + 65)
        elif x in range(97,123):
            msg += chr(((x - 97 + i) % 26) + 97)
        else:
            msg += chr(x)
    print(msg)
```

The decoder showed all possible shifts, and the flag came out when I shifted 13 times. It was ROT13 cipher.

**Flag: `picoCTF{C7r1F_54V35_71M3}`**

## morse-code (100 pts)

> Morse code is well known. Can you decrypt this?
>
> Download the file here.
>
> Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

When I submitted [the audio file](sources/morse_chal.wav) to the [morse code decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html), The result was `WH47 H47H 90D W20U9H7`.

If I replace the spaces with the underscores: `WH47_H47H_90D_W20U9H7`

**Flag: `picoCTF{WH47_H47H_90D_W20U9H7}`**

## rail-fence (100 pts)

> A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
>
> Download the message here.
>
> Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

The content of [the message file](sources/rail-fence.txt):

```text
Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6
```

The ciphertext has 56 characters.  Since it was encrypted in 4-rail rail fence cipher, the texts should be divided like these:

```text
1.....1.....1.....1.....1.....1.....1.....1.....1.....1. ==> 10
.2...2.2...2.2...2.2...2.2...2.2...2.2...2.2...2.2...2.2 ==> 19
..3.3...3.3...3.3...3.3...3.3...3.3...3.3...3.3...3.3... ==> 18
...4.....4.....4.....4.....4.....4.....4.....4.....4.... ==> 9
```

|1|2|3|4|
|-|-|-|-|
|Ta _7N6D49|hlg:W3D_H3C31N__A97|ef sHR053F38N43D7B| i33___N6|

```text
T.....a..... ....._.....7.....N.....6.....D.....4.....9. 
.h...l.g...:.W...3.D..._.H...3.C...3.1...N._..._.A...9.7 
..e.f... .s...H.R...0.5...3.F...3.8...N.4...3.D...7.B... 
... .....i.....3.....3....._....._....._.....N.....6.... 
```

The plaintext message is: `The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997`

**Flag: `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}`**

## substitution0 (100 pts)

> A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
>
> Download the message here.

The following is the content of [the message](sources/substitution0.txt):

```text
EKSZJTCMXOQUDYLFABGPHNRVIW 

Mjbjhfly Ujcbeyz eblgj, rxpm e cbenj eyz gpepjui exb, eyz kblhcmp dj pmj kjjpuj
tbld e cuegg segj xy rmxsm xp reg jysulgjz. Xp reg e kjehpxthu gsebekejhg, eyz, ep
pmep pxdj, hyqylry pl yephbeuxgpg—lt slhbgj e cbjep fbxwj xy e gsxjypxtxs flxyp
lt nxjr. Pmjbj rjbj prl blhyz kuesq gflpg yjeb lyj jvpbjdxpi lt pmj kesq, eyz e
ulyc lyj yjeb pmj lpmjb. Pmj gseujg rjbj jvsjjzxycui mebz eyz culggi, rxpm euu pmj
effjebeysj lt khbyxgmjz cluz. Pmj rjxcmp lt pmj xygjsp reg njbi bjdebqekuj, eyz,
peqxyc euu pmxycg xypl slygxzjbepxly, X slhuz mebzui kuedj Ohfxpjb tlb mxg lfxyxly
bjgfjspxyc xp.

Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}
```

The last line suggests that `fxslSPT` should be decoded to `picoCTF`. Part of the substitution table would look like this:

|F|L|P|S|T|X|
|-|-|-|-|-|-|
|P|O|T|C|F|I|

The first line of the message is `EKSZJTCMXOQUDYLFABGPHNRVIW`. Decoding it would look somewhat like this:

```text
EKSZJTCMXOQUDYLFABGPHNRVIW
..C..F..I.....OP...T......
```

It looked like that the first line was just listing the alphabet letters in order, from A to Z. It might be the key for decryption.

I wrote [the script](solutions/substitution0.py) to decrypt this document.

```python
enc = open("../sources/substitution0.txt", "r")

sub_upper = "EKSZJTCMXOQUDYLFABGPHNRVIW"
sub_lower = "ekszjtcmxoqudylfabgphnrviw"

alp_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_lower = "abcdefghijklmnopqrstuvwxyz"

for line in enc.readlines():
    prnt = ""
    for ch in line:
        if ch in sub_upper:
            prnt += alp_upper[sub_upper.find(ch)]
        elif ch in sub_lower:
            prnt += alp_lower[sub_lower.find(ch)]
        else:
            prnt += ch
    print(prnt)
```

The result yielded the flag.

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Hereupon Legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. There were two round black spots near one extremity of the back, and a
long one near the other. The scales were exceedingly hard and glossy, with all the
appearance of burnished gold. The weight of the insect was very remarkable, and,
taking all things into consideration, I could hardly blame Jupiter for his opinion
respecting it.

The flag is: picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
```

**Flag: `picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`**

## substitution1 (100 pts)

> A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.
>
> Download the message here.

The following is the content of [the message](sources/substitution1.txt):

```text
IECj (jqfue cfu ixzelus eqs coxa) xus x emzs fc ifrzlesu jsiludem ifrzsededfy. Ifyesjexyej xus zusjsyesk hdeq x jse fc iqxoosyasj hqdiq esje eqsdu iusxedgdem, esiqydixo (xyk affaodya) jpdooj, xyk zuftosr-jfogdya xtdodem. Iqxoosyasj ljlxoom ifgsu x ylrtsu fc ixesafudsj, xyk hqsy jfogsk, sxiq mdsokj x jeudya (ixoosk x coxa) hqdiq dj jltrdeesk ef xy fyodys jifudya jsugdis. IECj xus x ausxe hxm ef osxuy x hdks xuuxm fc ifrzlesu jsiludem jpdooj dy x jxcs, osaxo sygdufyrsye, xyk xus qfjesk xyk zoxmsk tm rxym jsiludem auflzj xuflyk eqs hfuok cfu cly xyk zuxiedis. Cfu eqdj zuftosr, eqs coxa dj: zdifIEC{CU3NL3YIM_4774IP5_4U3_I001_4871S6CT}
```

Since there is no visibly identifiable decryption key, I modified the script for the previous problem to find the solution manually. I ran [the script](solutions/substitution1.py) multiple times to guess the letters and gradually filled out the substitution table.

```python
enc = open("../sources/substitution1.txt", "r")

# Final substitution table
alp_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_lower = "abcdefghijklmnopqrstuvwxyz"
sub_upper = "G.FITOVWCSDUYQLKHMEBR..ANP"
sub_lower = "g.fitovwcsduyqlkhmebr..anp"

for line in enc.readlines():
    print(line)
    prnt = ""
    for ch in line:
        if ch in alp_upper:
            prnt += sub_upper[alp_upper.find(ch)]
        elif ch in alp_lower:
            prnt += sub_lower[alp_lower.find(ch)]
        else:
            prnt += ch
    print(prnt)
```

Although the substitution table was incomplete, I was able to find the key.

```text
CTFs (short for capture the flag) are a type of computer security competition. Contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. Challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. CTFs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. For this problem, the flag is: picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}
```

**Flag: `picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}`**

## substitution2 (100 pts)

> It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?
>
> Download the message here.

The following is the content of [the message](sources/substitution2.txt):

```text
gvjwjjoeugujajwqxzgvjwkjxxjugqfxeuvjivecvumvzzxmzbpsgjwujmswegrmzbpjgegezhuehmxsiehcmrfjwpqgwezgqhisumrfjwmvqxxjhcjgvjujmzbpjgegezhunzmsupwebqwexrzhurugjbuqibeheugwqgezhnshiqbjhgqxukvemvqwjajwrsujnsxqhibqwdjgqfxjudexxuvzkjajwkjfjxejajgvjpwzpjwpswpzujznqvecvumvzzxmzbpsgjwujmswegrmzbpjgegezheuhzgzhxrgzgjqmvaqxsqfxjudexxufsgqxuzgzcjgugsijhguehgjwjugjiehqhijomegjiqfzsgmzbpsgjwumejhmjijnjhueajmzbpjgegezhuqwjzngjhxqfzwezsuqnnqewuqhimzbjizkhgzwshhehcmvjmdxeuguqhijojmsgehcmzhnecumwepguznnjhujzhgvjzgvjwvqhieuvjqaexrnzmsujizhjopxzwqgezhqhiebpwzaeuqgezhqhizngjhvqujxjbjhguznpxqrkjfjxejajqmzbpjgegezhgzsmvehczhgvjznnjhueajjxjbjhguznmzbpsgjwujmswegreugvjwjnzwjqfjggjwajvemxjnzwgjmvjaqhcjxeubgzugsijhguehqbjwemqhvecvumvzzxunswgvjwkjfjxejajgvqgqhshijwugqhiehcznznnjhueajgjmvhelsjueujuujhgeqxnzwbzshgehcqhjnnjmgeajijnjhujqhigvqggvjgzzxuqhimzhnecswqgezhnzmsujhmzshgjwjiehijnjhueajmzbpjgegezhuizjuhzgxjqiugsijhgugzdhzkgvjewjhjbrqujnnjmgeajxrqugjqmvehcgvjbgzqmgeajxrgvehdxedjqhqggqmdjwpemzmgneuqhznnjhueajxrzwejhgjivecvumvzzxmzbpsgjwujmswegrmzbpjgegezhgvqgujjdugzcjhjwqgjehgjwjugehmzbpsgjwumejhmjqbzhcvecvumvzzxjwugjqmvehcgvjbjhzscvqfzsgmzbpsgjwujmswegrgzpelsjgvjewmswezuegrbzgeaqgehcgvjbgzjopxzwjzhgvjewzkhqhijhqfxehcgvjbgzfjggjwijnjhigvjewbqmvehjugvjnxqceupemzMGN{H6W4B_4H41R515_15_73I10S5_8J1FN808}
```

This time, I used <dcode.fr> online decrypter to automatically substitute the letters.

Key: `VMGKIBTNDEWZCFXPAYUJSHRLQO`

```text
THEREEXISTSEVERALOTHERWELLESTABLISHEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONSINCLUDINGCYBERPATRIOTANDUSCYBERCHALLENGETHESECOMPETITIONSFOCUSPRIMARILYONSYSTEMSADMINISTRATIONFUNDAMENTALSWHICHAREVERYUSEFULANDMARKETABLESKILLSHOWEVERWEBELIEVETHEPROPERPURPOSEOFAHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONISNOTONLYTOTEACHVALUABLESKILLSBUTALSOTOGETSTUDENTSINTERESTEDINANDEXCITEDABOUTCOMPUTERSCIENCEDEFENSIVECOMPETITIONSAREOFTENLABORIOUSAFFAIRSANDCOMEDOWNTORUNNINGCHECKLISTSANDEXECUTINGCONFIGSCRIPTSOFFENSEONTHEOTHERHANDISHEAVILYFOCUSEDONEXPLORATIONANDIMPROVISATIONANDOFTENHASELEMENTSOFPLAYWEBELIEVEACOMPETITIONTOUCHINGONTHEOFFENSIVEELEMENTSOFCOMPUTERSECURITYISTHEREFOREABETTERVEHICLEFORTECHEVANGELISMTOSTUDENTSINAMERICANHIGHSCHOOLSFURTHERWEBELIEVETHATANUNDERSTANDINGOFOFFENSIVETECHNIZUESISESSENTIALFORMOUNTINGANEFFECTIVEDEFENSEANDTHATTHETOOLSANDCONFIGURATIONFOCUSENCOUNTEREDINDEFENSIVECOMPETITIONSDOESNOTLEADSTUDENTSTOKNOWTHEIRENEMYASEFFECTIVELYASTEACHINGTHEMTOACTIVELYTHINKLIKEANATTACKERPICOCTFISANOFFENSIVELYORIENTEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONTHATSEEKSTOGENERATEINTERESTINCOMPUTERSCIENCEAMONGHIGHSCHOOLERSTEACHINGTHEMENOUGHABOUTCOMPUTERSECURITYTOPIZUETHEIRCURIOSITYMOTIVATINGTHEMTOEXPLOREONTHEIROWNANDENABLINGTHEMTOBETTERDEFENDTHEIRMACHINESTHEFLAGISPICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

**Flag: `picoCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}`**

## transposition-trial (100 pts)

> Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
>
> Download the corrupted message here.

The following is the content of [the message](sources/transposition-trial.txt):

```text
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4
```

The problem statement reveals that the scrambled blocks have size of 3, and the first word is 3 letters long. Since the first three letters are `heT`, I thought that the first letter of each block got pushed to the end of the block. The following is [the script](solutions/transpose-trial.py) that I wrote to undo this mishap.

```python
corrupted = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

blocks = []

for i in range(0,53,3):
    blocks.append(corrupted[i:i+3])

recovered = ""

for block in blocks:
    recovered += block[2]
    recovered += block[0]
    recovered += block[1]

print(recovered)
```

The following is is the result of running the script.

```text
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
```

Flag: `picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}`

## Vigenere (100 pts)

> Can you decrypt this message?
>
> Decrypt this message using this key "CYLAB".

The following is the content of [the message](sources/Vigenere.txt):

```text
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}
```

I used online decryption tool. With the text and the key (`CYLAB`) I was able to get the key from the first go.

Flag: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}`

## diffie-hellman (200 pts)

> Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message?
>
> Download the message here.
>
> Wrap your decrypted message in the picoCTF flag format like: `picoCTF{decrypted_message}`

The following is the content of [the message](sources/diffie-hellman.txt):

```text
H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_D9FF6IFD
```

I wrote [a script](solutions/diffie-hellman.py) to calculate the key and shift the text back to the original text.

```python
# Letter table
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# The Cphertext
ciphertext = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_D9FF6IFD"

# Keygen
p = 13
g = 5
a = 7
b = 3

key = (g ** (a * b)) % p

orig = ""

for c in ciphertext:
    if c in table:
        orig += table[(table.find(c) - key) % 36]
    else:
        orig += c

print(orig)
```

When I ran the script I got the text below.

```text
C4354R_C1PH3R_15_4_817_0U7D473D_84AA1DA8
```

**Flag: `picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_84AA1DA8}`**

## Very Smooth (300 pts)

> Forget safe primes... Here, we like to live life dangerously... >:)
>
> - [gen.py](/sources/very-smooth/gen.py)
> - [output.txt](sources/very-smooth/output.txt)

The `output.txt` contains two numbers,

```text
n = 65446ab139efe9744c78a271ad04d94ce541a299f9d4dcb658f66f49414fb913d8ac6c90dacc1ad43135454c3c5ac76c56d71d2816dac23db5c8caa773ae2397bd5909a1f2823c230f44ac684c437f16e4ca75d50b75d2f7e5549c034aa8a723c9eaa904572a8c5c6c1ed7093a0695522a5c41575c4dbf1158ca940c02b223f50ae86e6782819278d989200a2cd2be4b7b303dffd07209752ee5a3060c6d910a108444c7a769d003bf8976617b4459fdc15a2a73fc661564267f55be6a0d0d2ec4c06a4951df5a096b079d9e300f7ad72fa6c73a630f9a38e472563434c10225bde7d08c651bdd23fd471077d44c6aab4e01323ed78641983b29633ad104f3fd
c = 19a98df2bfd703a31fedff8a02d43bc11f1fb3c15cfa7a55b6a32b3532e1ac477f6accc448f9b7d2b4deaae887450217bb70298afaa0f5e31a77e7c6f8ba1986979f15d299230119e3dd7e42eb9ca4d58d084d18b328fbe08c8909a2afc67866d6550e4e6fa27dc13d05c51cc87259fe73e2a1890cc2825d76c8b2a99f72f6023fc96658ac355487a6c275717ca6c13551094818efae1cec3c8773cc5a72fed518c00a53ba9799d9d5c182795dfcece07c727183fdd86fd2cb4b95e9f231be1858320aa7f8430885eb3d24300552d1a83158636316e55e6ac0a30a608964dbf2c412aed6a15df5fd49e737f7c06c02360d0c292abc33a3735152db2fb5bc5f6d
```

The `gen.py` reads a `flag.txt` file, encodes the flag, and encrypt it with RSA but by using smooth prime numbers.

|Number |Description|Value |
|-------|-----------|------|
|`FLAG` |Message|Flag encoded and converted to hexadecimal|
|`p`    |Random prime|Unknown|
|`q`    |Random prime|Unknown|
|`e`    |Arbitrary number, Part of Public key |65537|
|`n`    |Modulus, part of Public key |`p` x `q`|
|`m`    |Lambda `n`|LCM of `p-1` and `q-1`|
|`d`    |Private key, Modular inverse of `e` mod Phi `n`|`e`^(-1) mod `m`|
|`c`    |Ciphertext|`FLAG` ^ `e` mod `n`|

I [analyzed `gen.py`](sources/very-smooth/gen-deb.py) and found some information about the program.

- The lambdas of `p` and `q` are multiples of numerous random prime numbers, but none of them are over 131101.
- `32771 <= p_factor < 65537`, `65537 < q_factor <= 131101`

I wrote a [script](solutions/very-smooth.py) that decoded the flag using [Pollard's p-1 algorithm](https://www.geeksforgeeks.org/pollard-p-1-algorithm/)

```text
PS D:\GitHub\picoCTF2022> & C:/Python310/python.exe d:/GitHub/picoCTF2022/solutions/very-smooth.py
N: 12783806366677048922907064848328098212866693477424538420599896228455017037669449950683546784313169674544927543595291662976684301858812992858099444859337569143246822546054247961790330260420831355984966100127030591813453917351133279192784673199662030400887332986215139842373608664467290267265075487584959980177516580729036008323441590214846366044269288093568024436382396737652482146953506549011853758786667315561013176183516549863396043271473017918748952413783159066342857945287646751402844866521621491143273195939565677244080888115009864325468486000003135812632832429062390969321007889831314647812130127842465204728829
C: 3239568057062076957315954705201426981829984354123180474454427960187556040890537772305643536856843905217063459037623708488358518056610180684498379572876179711504931131174926019037655815749868541648616303761708669844410430529623004303079496270405633013985860495832867400577300407266630191540653974251262981431217267604706107358065529262785008215923682478653476362279222774315891655289579301279790445988014134421011710989748978295334871012982457861126498002102321059858010685481763516984936765798883373560142873390761953928285173316683915578227955409970910936278856212442587528491846046527962658144112551337168736116589
Flag: picoCTF{376ebfe7}
PS D:\GitHub\picoCTF2022> 
```

**Flag: `picoCTF{376ebfe7}`**

## Sequences (400 pts)

> I wrote this linear recurrence function, can you figure out how to make it run fast enough and get the flag?
>
> Download the code here [sequences.py](sources/sequences.py)
>
> Note that even an efficient solution might take several seconds to run. If your solution is taking several minutes, then you may need to reconsider your approach.

The code has a recursive function `m_func(i)` that generates a key, and a large number as the parameter for that function. The goal is to optimize `m_func(i)` to get the key. When I ran the script, it resulted in `RecursionError: maximum recursion depth exceeded` error message.

```python
import math
import hashlib
import sys
from tqdm import tqdm
import functools

ITERS = int(2e7)

# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
@functools.cache
def m_func(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)

def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS)
    decrypt_flag(sol)
```

I thought about converting the recursive function to the iterative function using for loop. But even if I did so, there was a chance that the number might get too big. However, I knew that the `decrypt_flag(sol)` function starts with moding `sol` by `(10 ** 10000)`. I thought it would be better to do this calculation inside the `m_func(i)` function, in each loop.

This is how I rewrote the `m_func(i) function`. It can be found [here](solutions/sequences.py).

```python
ceiling = 10 ** 10000

def m_func(i):
    a = 1 # f(i - 4)
    b = 2 # f(i - 3)
    c = 3 # f(i - 2)
    d = 4 # f(i - 1)
    e = 0 # place for f(i)
    if i < 4:
        return i  + 1

    for i in tqdm(range(4, i + 1)): # tqdm provides progress bar at stdout
        e = ((55692 * a) - (9549 * b) + (301 * c) + (21 * d)) % ceiling
        a = b
        b = c
        c = d
        d = e
    
    return e
```

This time, I was able to run the script without recursion error and get the flag.

```text
PS D:\GitHub\picoCTF2022> & C:/Python310/python.exe d:/GitHub/picoCTF2022/solutions/sequences.py
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 19999997/19999997 [03:44<00:00, 89016.57it/s] 
picoCTF{b1g_numb3rs_afc4ce7f}
```

**Flag: `picoCTF{b1g_numb3rs_afc4ce7f}`**

## Sum-O-Primes (400 pts)

> We have so much faith in RSA we give you not just the product of the primes, but their sum as well!
>
> - [gen.py](sources/sum-o-primes/gen.py)
> - [output.txt](sources/sum-o-primes/output.txt)

The output text shows three numbers.

```text
x = 17fef88f46a58da13be8083b814caf6cd8d494dd6c21ad7bf399e521e14466d51a74f51ad5499731018b6a437576e72bd397c4bb07bfbb699c1a35f1f4fa1b86dee2a1702670e9cea45aa7062f9569279d6d4b964f3df2ff8e38cf029faad57e42b831bde21132303e127cba4e80cd3c9ff6a7bad5b399a18252dc35460471ea8
n = 85393637a04ec36e699796ac16979c51ecea41cfd8353c2a241193d1d40d02701b34e9cd4deaf2b13b6717757f178ff75249f3d675448ec928aef41c39e4be1c8ba2ba79c4ada36c607763d7dc8543103acfe1027245acda2208f22fcabe0f37bdadf077e4f943c4f4178cedeb5279a4ebc86323356e23a58b6666ac6ffbf4f1c8229117ffb9071a94dfb724957f10d6664e4ee02e16bed29eb922f126e2082e2f73b5c5b7817e0543155eb9673f4de3de8c91707c1261e8ba6e7348d930293f7796679218c2b1dabe41527eccd72ec3e7284344622eff81ae0541769fb70b6146b54bd092c2dfbe7f8e9653cad80d0fb4f3ef288778927b3852f9ff3a4076d7
c = 42cafbc77ed8396a681dac328701ee02cd746488ae084f15a3e6a5b8f666c595a372a69bbca0dae934fd5ed2292d4393912ee10a22a3b57de9cee2f30b5dc7c67f574b0453f6074171cca37bd407529cb30ba17f152ef5b2484d94b38cf0a513a723255d725e5c3b3f3c985f9223095be3fa148afedf91e4ed37720c3d97dd29cf07830efa8a557a9da68d3095fc3b31f3763e030b62c70d94c3d2951e163e48683f3b9611d562ea06bf1e5d8465e8bf5a6345050a5e7b0c175faf136562cf2a196fdb61ac6503446616cffa9ed85015b86dda73f6eda4d688d3e719a07439d98f95fb5dcf675948ec58d9af83fa29afa4375213ec48f09a6c8cbc431cfe7c6a
```

The first number `x` is the sum of `p` and `q`, while `n` is multiplication of `p` and `q`.

Given that `Phi(n) = (p-1)(q-1) = p * q - p - q + 1 = (p * q) - (p + q) - 1`, it can be written that `Phi(n) = n - x + 1`.

The relationship between `Phi(n)` and `Lambda(n)` is that [if e * d mod Phi(n) = 1 mod Phi(n), then e * d mod Lambda(n) = 1 mod Lambda(n)](https://math.stackexchange.com/questions/3249362/rsa-cryptosystem-relation-between-lambda-and-phi). Therefore, I could solve the problem with `Phi(n)` instead of `Lambda(n)` and get the flag [here](solutions/sum-o-primes.py).

Flag: `picoCTF{3921def5}`

## NSA Backdoor (500 pts)

> I heard someone has been sneakily installing backdoors in open-source implementations of Diffie-Hellman... I wonder who it could be... ;)
>
> - [gen.py](sources/nsa-backdoor/gen.py)
> - [output.txt](sources/nsa-backdoor/output.txt)

The script uses the same prime generation functions as the one from **Very Smooth** problem. But, unlike that problem, the `c` here uses the flag as the exponent instead of the base, and there is no `e` that is coprime with `p-1` and `n-1`. Also, this is a bad Diffie-Hellman implementation because the modulus `n` is not a prime. This is the [backdoor](https://www.cryptologie.net/article/360/how-to-backdoor-diffie-hellman-quick-explanation/) of the implementation.

```text
n = d63c7cb032ae4d3a43ecec4999cfa8f8b49aa9c14374e60f3beeb437233e44f988a73101f9b20ffb56454350b1c9032c136142220ded059876ccfde992551db46c27f122cacdd38c86acb844032f8600515aa6ccb7a1d1ac62d04b51b752476d2d6ee9f22d0f933bebdd833a71fd30510479fcc7ba0afb1d4b0a1622cdc2a48341010dffdcfc8d9af45959fb30b692dc2c9e181ac6bcd6a701326e3707fb19b7f9dfe1c522c68f9b0d229d384be1e1c58f72f8df60ca5172a341a7ee81428a064beedd6af7b89cc6079f2b6d3717f0d29330f0a70acca05bf67ab60c2e5cb0b86bfca2c9b8d50d79d24371432a1efb243f3c5f15b377ccc51f6e69bfbf5ecc61
c = 51099773fd2aafd5f84dfe649acbb3558797f58bdc643ac6ee6f0a6fa30031767966316201c36be69241d9d05d0bd181ced13809f57b0c0594f6b29ac74bc7906dae70a2808799feddc71cf5b28401100e5e7e0324b9d8b56e540c725fa4ef87b9e8d0f901630da5f7f181f6d5b4cdc00d5f5c3457674abcb0d0c173f381b92bdfb143c595f024b98b9900410d502c87dfc1633796d640cb5f780fa4b6f0414fb51e34700d9096caf07b36f4dcd3bb5a2d126f60d3a802959d6fadf18f4970756f3099e14fa6386513fb8e6cdda80fdc1c32a10f6cdb197857caf1d7abf3812e3d9dcda106fa87bac382d3e6fc216c55da02a0c45a482550acb2f58bea2cfa03
```

The `c` was calculated as `3 ^ flag mod n`. So `g` in this Diffie-Hellman exchange is 3.
What I need to do first is to set `d` and `e` such that `d = 5 ^ e mod n`

Since `n` is not a prime number, I needed to make use of [Pohlig-Hellman algorithm](https://risencrypto.github.io/PohligHellman/) to recover the flag.

After numerous trials, I got the [script](solutions/nsa-backdoor.py) to solve this problem.

1. Since `n = p * q`, I found the Pohlig-Hellman values for `p` and `q`.
2. Then I reduced the latter to the remainder of dividing by `(q - 1) / 2`.
3. I used the [Chinese Remainder Theorem](https://brilliant.org/wiki/chinese-remainder-theorem/) to calculate the value of the flag.
4. Finally, I decoded the hexadecimal form of the flag to ASCII string.

**Flag: `picoCTF{1ca93858}`**

### (COMPLETED ALL CHALLENGES IN THIS CATEGORY)
