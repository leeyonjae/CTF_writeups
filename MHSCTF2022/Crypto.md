# MHSCTF - Crypto Part

- Yonjae Lee (yonjae.lee.93@gmail.com)

## Em Dee (10 pts)

> I have a good friend named Em. She loves secret codes, so when she challenged me this time, I was well up for it! She told me that she encoded the word "happy" as "56ab24c15b72a457069c5ea42fcfc640" and "sad" as "49f0bad299687c62334182178bfd75d8" (without the quotes) and challenged me to encode "mhsctf" using her method! I can't figure it out! What would it be? Enter your answer in flag format: "flag{...}"

According to [Hashes.com](https://hashes.com/en/decrypt/hash) the hash is Plain MD5:

```text
56ab24c15b72a457069c5ea42fcfc640:happy:MD5PLAIN
```

The answer is Plain MD5 Hash value of `mhsctf`, which is `fc3e3c405a66f8fe7cb7f17a838ea88c`.

**Flag: `flag{fc3e3c405a66f8fe7cb7f17a838ea88c}`**

## What's Cooking? (10 pts)

> 65 141 40 66 144 40 67 70 40 66 70 40 65 141 40 63 63 40 67 64 40 67 64 40 66 62 40 65 67 40 63 61 40 66 66 40 66 63 40 64 65 40 64 61 40 66 142 40 66 64 40 64 67 40 64 66 40 63 71

The given text is a Base64 that is encoded to Hexadecimal which is then again encoded to Octal.

Octal → Hexadecimal:

```text
5a 6d 78 68 5a 33 74 74 62 57 31 66 63 45 41 6b 64 47 46 39
```

Hexadecimal → Base64 :

```text
ZmxhZ3ttbW1fcEAkdGF9
```

Base64 → ASCII then yields the flag.

**Flag: `flag{mmm_p@$ta}`**

## Peanuts (10 pts)

> Charlie Brown received this message from his good friend Pig-Pen, but it appears to be nonsense. What could it be? Remember to enter your answer in the "flag{...}" format; it's all lowercase.

The question says that Charlie received the message from a friend named Pig-Pen.

The given image message is actually a [Pigpen Cipher](https://en.wikipedia.org/wiki/Pigpen_cipher) ciphertext.

![Image](Images/pigpen.png "Cipher")

[This Wikipedia image](https://upload.wikimedia.org/wikipedia/commons/3/36/Pigpen_cipher_key.svg) is the decryption key.

**Flag: `flag{goodgriefcharliebrown}`**

## Crash Hacker (Em Dee 2) (10 pts)

> Another super-secret message from Em! What does this one mean? b4b11af47f3086ce1293df4908d026d4 Remember to enter your answer in the "flag{...}" format! Hint: If at first you don't succeed, try, try again.

Used [online MD5 decryption tool](https://www.md5online.org/md5-decrypt.html) to easily find the flag.

**Flag: `flag{zero_cool}`**

## What's Cooking? 2 (10 pts)

> More layers of encryption! (Hint: there are 5 layers)

First Layer: Base32.

```text
GRYUG3ZUOFBWWNDRINVTI4KDNM2HCQ3LGRYUGQJUOFBW6NDRINXTI4KDN42HCQ3PGRYUG2ZUOFBUCNDRINVTI4KDN42HCQ3PGRYUG3ZUOFBW6Q3VJNTXCT2LM5YE6S3HOBHUWZ3QJ5FWO4CPJNTWOT2LM5YU6S3HOFHUWZ3RJ5FWO4KPJNTXCT2LM5TU6S3HOFHUWZ3RJ5FWO4KPJNTXCT2LM5YEC4TJN5FWU2LPJNKGS32LKRUW6S2UNFXUWVDJN5EUI2LPJNVGS32LNJUW6S3KNFXUW2TJN5FVI2LPJFCGS32LNJUW6S2UNFXUWVDJN5FVI2LPJNIUWNDRINXTI4KDNM2HCQ3LGRYUG2ZUOFBWWNDRINATI4KDN42HCQ3PGRYUG3ZUOFBW6NDRINVTI4KDIE2HCQ3LGRYUG2ZUOFBW6NDRINXTI4KDN5BXKS3HOFHUWZ3QJ5FWO4CPJNTXAT2LM5YE6S3HM5HUWZ3QJ5FWO4CPJNTXCT2LM5YU6S3HOFHUWZ3HJ5FWO4KPJNTXCT2LM5YU6S3HOBHUWZ3QIFZGS32LNJUW6S2UNFXUWVDJN5FVI2LPJNKGS32JIRUW6S3KNFXUW2TJN5FWU2LPJNVGS32LNJUW6SKENFXUW2TJN5FWU2LPJNVGS32LNJUW6S3HJM2HCQ3LGRYUG3ZUOFBW6NDRINXTI4KDN42HCQ2BGRYUG3ZUOFBW6NDRINXTI4KDNM2HCQ3LIN2UWZ3RJ5FWO4KPJNTXCT2LM5YU6S3HOBHUWZ3HJ5FWO4KPJNTXCT2LM5YU6S3HOFHUWZ3QIFZGS32LNJUW6S2UNFXUWVDJN5FVI2LPJNKGS32JIRUW6S2UNFXUW2TJN5FWU2LPJNVGS32LNJUW6SKENFXUW2TJN5FWU2LPJNVGS32LKRUW6S2RJM2HCQ3PGRYUG2ZUOFBWWNDRINVTI4KDNM2HCQ2BGRYUG2ZUOFBWWNDRINXTI4KDN42HCQ3PGRYUGQJUOFBW6NDRINVTI4KDNM2HCQ3LGRYUG22DOVFWO4KPJNTXAT2LM5YE6S3HOBHUWZ3QJ5FWOZ2PJNTXAT2LM5YE6S3HOFHUWZ3RJ5FWO4KPJNTWOT2LM5YU6S3HOFHUWZ3RJ5FWO4KPJNTXCQJ5HU======
```

Second Layer: Base64.

```text
4qCo4qCk4qCk4qCk4qCk4qCA4qCo4qCo4qCo4qCo4qCk4qCA4qCk4qCo4qCo4qCo4qCoCuKgqOKgpOKgpOKgpOKgpOKggOKgqOKgqOKgqOKgqOKgqOKggOKgqOKgqOKgqOKgqOKgpArioKjioKTioKTioKTioKTioIDioKjioKjioKjioKjioKTioIDioKjioKTioKTioKTioKQK4qCo4qCk4qCk4qCk4qCk4qCA4qCo4qCo4qCo4qCo4qCk4qCA4qCk4qCk4qCo4qCo4qCoCuKgqOKgpOKgpOKgpOKgpOKggOKgpOKgpOKgqOKgqOKgqOKggOKgqOKgqOKgqOKgpOKgpArioKjioKTioKTioKTioKTioIDioKjioKjioKjioKjioKjioIDioKjioKjioKjioKjioKgK4qCk4qCo4qCo4qCo4qCo4qCA4qCo4qCo4qCo4qCk4qCkCuKgqOKgqOKgqOKgqOKgpOKggOKgqOKgqOKgqOKgqOKgpArioKjioKTioKTioKTioKTioIDioKTioKjioKjioKjioKjioIDioKjioKjioKjioKTioKQK4qCo4qCk4qCk4qCk4qCk4qCA4qCk4qCk4qCo4qCo4qCo4qCA4qCo4qCk4qCk4qCk4qCkCuKgqOKgpOKgpOKgpOKgpOKggOKgpOKgpOKgqOKgqOKgqOKggOKgqOKgqOKgqOKgqOKgqA==
```

Third Layer: Braille.

```text
.--- ....- -.... 
.--- ..... ....- 
.--- ....- .--- 
.--- ....- --... 
.--- --... ...-- 
.--- ..... ..... 
-.... ...-- 
....- ....- 
.--- -.... ...-- 
.--- --... .--- 
```

Fourth Layer: Morse.

```text
.---- ....- -.... .---- ..... ....- .---- ....- .---- .---- ....- --... .---- --... ...-- .---- ..... ..... -.... ...-- ....- ....- .---- -.... ...-- .---- --... .---- .---- --... .....
```

Fifth Layer: Octet

```text
146 154 141 147 173 155 63 44 163 171 175
```

**Flag: `flag{m3$sy}`**

## IPv11 (15 pts)

> I asked my friend for the IP addresss of their website and this is what they gave me. I'm sure they're misunderstanding, but I should really decode this before deciding that. Remember to enter your answer in the "flag{...}" format! 1.9.100.51.110.116.105.102.105.51.100

The numbers are decimal ASCII codes.

**Flag: `flag{1d3ntifi3d}`**

## Weird Music (25 pts)

> Does this music sound familiar to you? It's a little bit different though. Remember to use the "flag{...}" format.

The given MIDI file is a Beethoven opus, but the beats sound a little off.

Opening it on a MIDI editor, I found each note looks like a part of a Morse code sequence, bar the last long note. Converting it to the letters yielded the content of the flag.

**Flag: `flag{BEEP_BOTOP}`**

## Green (30 pts)

> I'm green da ba dee da ba dah

The accompanying image was a thin, long green line (1076 x 1).

![green](Images/green.png)

 Zooming it to the maximum revealed that it is not exactly uniform in terms of color, meaning that there were different shades of green.

Analysis using ImageMagick `convert` indicates that only G of RGB is non-zero in every pixel.

Converting the Green RGB numbers to string by mapping them to ASCII table yields this text:

```text
JJFEMRKNKJFU4S2KIZKTIUZSJNEVUTCGJNKVUU2KJZCVMVKSINDEWNKLKZKVKMSLJJNEIRKLKZFVKSKOIRCVGVCTJRFVUS2WJNGVGTCKJJDEKSKWJNGEWWSGKZCVEMSLJJJEGVSPKZBVISSWIVLE2USDK5EVMSKUIVKEGS2KJJCEKS2TJNLUUTSHIVLVOU2HJNNEKVSFJVJUYSSGJJCUOVSTJRFVESSVLFJVGV2JKZGEKMSVKNCEWNKGIVGVGS2VJFLEWRKXKMZEWSSKINCUWUZSKRFE4TCVKVKFGSCJKZGFMS2VGJEEUTSOIVDVMU2GJJLEUVKZKNJUOSSKINKU6VSTJNFTKRSWKNLVGR2KIZFFMR2VGJFEWWSHIVGVGMSWJNHEGRKXJZFUOSKWI5LEOUZSKZFEMTCFKVLEWWCLJZFFKUKTGIZESUSLKVLVKWSTJNHEIVKVKNJVMSZVJNDEOU2LJJFVUR2GJVJDEVSHJJCUKVKUKNHUSVSKKZGVKMSJJJHEOVSVKJJUES2OJJKU6U2TKNEU4S2VGZLFGVCLKJDEMRKSKNLUUVSKKZDVMMSLJFNEMRSNKIZE4S2OIZCVOV2TJBEVMRSWI5GVGV2KJZEEKR2SJNMEUWSGKVGVGMRSJE2UYRKPKZFFGS22IZCU2VCDIZFVMTCFK5LUGTCKKZHEKS2WJNKUSTSGKVJVGU2NJFKVURSNKEZE2SSNGJKU2USKKVFU4SSWJVJTEV2KJZCEKT2VLJJUUSSGKZKVEMSHJJLEURCFKZJUQSSKIVKUWVSLKNFU4SCVKNLFGS2LLJDVMS2NKNFEUSSIIVLVMU2WJNFEMVSBKMZE6SK2IRCTEVJSKRDUURKVGRKEGRSKGVGEMR2WINFEUWSEIZFU4Q2TJNHEYRKTKZJUWSK2IRLEKUZSJRFEUTSFJVJFGTCLJFNEMT2TGJHUSVSLKZHVMU2LJNJEKVSVKJFVMR2KJNKEKVKTJNFEUQ2WJFJEWV2KJZFEKV2XKNDUSUSGKZDVCMSXJE2U4RKXKJBUMS2WIJKVOURSKZEFKNSUGJIEUNKIKU6T2PJ5HU6Q
```

The most likely possibility is that it is a Base-32 string. So I decoded it once. The result looks similar to the original:

```text
=== 1st Attempt to Decode ===
JJFEMRKNKJFU4S2KIZLFKUZSJNEVURCFK5KVUU2KJZDEKVKUINDESTSLKZKVKMSLJJFEIVKLKZFVER2KJRCVOVCTJVEVMRCWIVITETCKJJDEKSKWJNGEWWSGKZEVEMSLJFJEGVSLKRJUYSSWIVLE2USDK5FEMSKUIVKEWS2KJJCEKS2TJNLUUTSHIVLVKU2HJNNEGVSFJVJUYSSGJJCUOVSKK5FVSWSGJFJVGU2JKZGEMS2VKNCEWNKGIVGVGS2VJFLEUVKXKNJUQS22IRKUWUZSKNDUUSSVK5KFGSKJKZGFMR2VGJEEUTSOIVJVMU2IJNGVURSBKNJUOSSSINKU6VSTKRFFERSWJVJVGV2KIZFFMR2NKNFEWWSHIVFVGMSWJNHEGRKXJZFUMS22I5LEOVJSKZFEMTCFKVLEWWCLJVNEKVKUINFUSSSMIUZFMQ2MJM2UMRJUKNJVMS2WJNDEOUZSJJFVUR2GJVJDEVSHJJEUKVKSKNHUSVSKKZGVKMSJJJHEWVSVKJFVAS2OIZDE2U2TGJEU4TCFJ5LFGVCJJZDFKNCSKNLESVSKIZDVES2LJJNEMRSLKIZFOS2OIVKVOVSKKREVURKVGJKTEUSKJJCVIRKWJNJEWWSGIRFVGQ2WI5NEWRCFKVBUWR2VHU6T2PJ5HU======
```

However it is clearly different and shorter than the original text. It seems that the original string was encoded multiple times. I repeated decoding the result, then the flag appeared.

```text
1. JJFEMRKNKJFVUS2KIZDEWUZSJNFEUTCFINKVUU2KJJDUKVKRGJLEWTSMIVDVEQ2LJJFEIVKLKZFVIR2KIRCVKTSLJVEVMRCWJFITETKKJJDEKSKWJNGEWUSGKZCVEMSLJFJEGVJWKYZFISSSIVLFKUSDK5FEMSKUIVJUWSSHKZDUKS2SGJJUWTSIIVLVGU2HJNNESVSHKMZFASSGJRCUOVSTJRFVMSSWJFJVGMSJKZGEKS2VKNCEWNKFKZGVGU2VJFLEUVKXKMZEUTCKIJLE2VCLK5FE4SSVKVKFGS2JKZGFMR2VGJIEURSOIVJVMU2IJNKVURKPKNFFMSS2INLEOVSTINFU4RSVIVJFGRKKJZFFKR2WKNEUWVJTIZEU2U2RJJETEVKRKZFDKSCVGZKDEUCKGU======
2. JJFEMRKZKJFFKS2KJJLECUZSJJGEUQ2VKNLEGRCKJJDUKVKTGJDEUNKMIVDVIQ2MJJFEIVKLKRFVER2KIRCU6V2TJREVURCWJFITESKJGVGEKR2SKNHEWSSGKZIVGS2PJFLEGVSLKVJVISS2IVLEKUSDK5EVMSSUIVJUWS2JLJBVMTKWJNJUUTSKIVLVGU2PJFNESVSHKUZEOSJVJZCVGVSCKNFUERSEJNJUGVSIKU3FIMSQJI2UQVJ5HU6T2PJ5
3. JJFEYRJUKJJVAS2JLJCUSVCDJJGEUS2FJ5LEGTCLJJDUKTKRGJDEOWSLIZDVIQ2II5LEGRSNKJFVQSKOIVCVKUSTJZEVERCWIVJTESKKIZCVMVKSJNJEWSSOIZIVGU2GI5NESVBSKBFDKSCVHU6T2PJ5HU======
4. JJLE4RSPKIZEITCJLJKEOVCLKJGEMQ2FGZKFGTCHGVCFMRKXINEEURSNIRDVES2IJFEVURKRKJNFQSSFGZIT2PJ5HU======
5. JVNFOR2DLIZTGTKRLFCE6TSLG5DVEWCHJFMDGRKHIIZEQRZXJE6Q====
6. MZWGCZ33MQYDONK7GRXGIX3EGB2HG7I=
7. flag{d075_4nd_d0ts}
```

**Flag: `flag{d075_4nd_d0ts}`**
