# Forensics

## Enhance! (100 pts)

> Download this image file and find the flag.
>
> [Download image file](sources/enhance.svg)

The image:

![Dark ring](sources/enhance.svg)

The thick, dark ring has a hole in the center. I zoomed in to 10000% , and there was a small black circle in the hole. But it did not yield any information about the flag.

But, the image is in SVG format, and it can be read by text editors. I looked at the code for the file and found the presence of the text. 

```xml
<text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
       x="107.43014"
       y="132.08501"
       id="text3723"><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan>
         ...
         </text>
```

The text are so miniscule that it would probably have to be magnified above 100000% or so. Since I could not think of any tool to achieve this, I just decided to recover the flag manually from the code.

**Flag: `picoCTF{3nh4nc3d_aab729dd}`**

## File types (100 pts)

> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
>
> You can download the file from [here](sources/filetype/FileTypes-Flag.pdf).

When I tried to open the file, but the PDF reader showed error message.

I opened it using hex editor. From the first line it was clear that it is not an ordinary PDF file.

```text
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2022-03-15 06:50 UTC by <root@e8647f66bc56>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
# ...
```

The rest of the file was a series of linux shell command. So I copied it into a new executable file and executed it.

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ cp FileTypes-Flag.pdf shar
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ ./shar
x - created lock directory _sh00046.
x - extracting flag (text)
./shar: 119: uudecode: not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
```

Apparently, the `uudecode` command needs `sharutils` package. I installed it and ran again.

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ ./shar
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

The result, `./flag`, was not readable by text editor. When opened with the hex editor, the content began like this and the rest was not legible:

```text
!<arch>
flag/           0           0     0     644     1024      `
?i
```

This file was [likely an `ar` archive](https://stackoverflow.com/questions/2696166/what-kind-of-lib-file-begins-with-arch). It has `644` permission and is 1024 bytes long. It contains another file named `flag`. So I changed the name of the archive to `flag.ar` and extracted the file, which was another binary. It continues on and on, from `ar` to `bz2` to `lzip` to `lz4` to `lzip` again to `xz`. The hex editor sure came handy, because I had to constantly delete garbages before actual header for each type.

Ultimately this is the decrypted content:

```text
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f33633739633562617d0a
```

It is a hexadecimal and the flag is the result when it is converted to a string.

**Flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}`**

## Lookey here (100 pts)

> Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
>
> Download the data [here](sources/lookey-here.txt).

The file contains an excerpt of what seems to be a novel. I was able to easily find the key by using `Ctrl+F` from the text editor and looking for the word `CTF`.

```text
These things help us in our work. We do not understand them, but
      we think that the men of picoCTF{gr3p_15_@w3s0m3_4c479940}
our                             ................................
      power of the sky, and these things had some relation to it. We do
      not know, but we shall learn. We cannot stop now, even though it
      frightens us that we are alone in our knowledge.
```

**Flag: `picoCTF{gr3p_15_@w3s0m3_4c479940}`**

## Packets Primer (100 pts)

> Download the packet capture file and use packet analysis software to find the flag.
>
> * Download [packet capture](sources/packets-primer-network-dump.flag.pcap)

I used Wireshark to analyze the file. The capture file has 9 packets in it: 5 TCP packets and 4 ARP packets. One of the TCP packets had `PSH` flag set. It was the largest packet in the capture, and its data section contained the flag.

**Flag: `picoCTF{p4ck37_5h4rk_ceccaa7f}`**

## Redaction gone wrong (100 pts)

> Now you DON’T see me.
>
> This [report](sources/Redaction-gone-wrong.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

The PDF file had some lines of texts, with parts of them blacked out like any censored document. However, the text of this PDF file is selectable. So I selected the entire text and copied and pasted below:

```text
("--text--" indicates censored texts.)

Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
--Breakdown-- - Just painted over in MS word.
--         --
Cost Benefit Analysis
Credit Debit
--This is not the flag, keep looking--
Expenses from the --           --
--picoCTF{C4n_Y0u_S33_m3_fully}--
Redacted document.
```

**Flag: `picoCTF{C4n_Y0u_S33_m3_fully}`**

## Sleuthkit Intro (100 pts)

> Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
>
> Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
>
> * [Download disk image](sources/sleuthkit-intro/disk.img.gz)
> * Access checker program: `nc saturn.picoctf.net 52279`

I decompressed the archive using `gunzip` command to get the image file. I used `mmls` on the image file which printed the partition information of the image. The following is the result.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-intro$ gunzip disk.img.gz 
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-intro$ ls
disk.img
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-intro$ mmls disk.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-intro$
```

The Linux partition starts at sector 2048 and ends at sector 204799. The next partition, if it exists, will begin at sector 204800. The size of the sector can be calculated by subtracting from the number of the next beginning sector and that of the current beginning sector.

> 204800 - 2048 = 202752

The Linux partition occupies 202752 sectors. I connected to checker program to check this calculation.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-intro$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```

**Flag: `picoCTF{mm15_f7w!}`**

## Sleuthkit Apprentice (200 pts)

> Download this disk image and find the flag.
>
> Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
>
> * [Download compressed disk image](sources/sleuthkit-apprentice/disk.flag.img.gz)


I used `mmls` to see the partitions in the disk.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/sleuthkit-apprentice$ mmls disk.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

Since I could not think of any command line tools to browse these systems, I opened the image file with 7Zip. After checking some likely locations, I found the flag file at `2.img\root\my_folder\flag.uni.txt`.

In other words, the location of the flag is in the third Linux partition (`000:002`). The absolute path is:

```text
/root/my_folder/flag.uni.txt
```

The disk image is also readable by Autopsy.

**Flag: `picoCTF{by73_5urf3r_3497ae6b}`**

## Eavesdrop (300 pts)

> Download this packet capture and find the flag.
>
> - [Download packet capture](sources/eavesdrop-capture.flag.pcap)

The packet capture file has a snippet of conversation between `10.0.2.4` and `10.0.2.15`. These were found in the data blocks of TCP handshake packets.

```text
10.0.2.4 > Hey, how do you decrypt this file again?
10.0.2.15 > You're serious?
10.0.2.4 > Yeah, I'm serious
10.0.2.15 > *sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
10.0.2.4 > Ok, great, thanks
10.0.2.15 > Let's use Discord next time, it's more secure.
10.0.2.4 > C'mon, no one knows we use this program like this!
10.0.2.15 > Whatever.
10.0.2.4 > Hey.
10.0.2.15 > Yeah?
10.0.2.4 > Could you transfer the file to me again?
10.0.2.15 > Oh great. Ok, over 9002?
10.0.2.4 > Yeah, listening.
10.0.2.15 > Salted__ñ¤¦¿ÐÊÔ=aÊù¢ZðÉà©ÄF8¡vò<8EY
10.0.2.15 > Sent it
10.0.2.4 > Got it.
10.0.2.15 > You're unbelievable.
```

The line that begins with `Salted__` is the content of the encrypted data `file.des3`. Due to unprintable hex strings, I used Python [script](solutions/eavesdrop.py) to insert the hex dump from the packet capture into the file.

```python
# eavesdrop file writing script

code = "53 61 6c 74 65 64 5f 5f f1 a4 a6 81 bf d0 ca d4" \
       " 85 9b 95 1d 3d 61 ca 1d f9 a2 8d 5a f0 c9 18 00" \
       " 14 15 7f e0 a9 c4 46 38 0b a1 76 f2 3c 38 45 59".split(" ")

enc = open("../sources/file.des3", "wb")

si = [bytes.fromhex(i) for i in code]
s = b''
for i in si:
    s += i

enc.write(s)
```

I ran the script and checked the output file.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ openssl des3 -d -salt -in file.des3 -out eavesdrop-flag.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ cat eavesdrop-flag.txt 
picoCTF{nc_73115_411_5786acc3}
```

**Flag: `picoCTF{nc_73115_411_5786acc3}`**

## Operation Oni (300 pts)

> Download this disk image, find the key and log into the remote machine.
>
> Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
>
> * [Download disk image](sources/operation-oni/disk.img.gz)
> * Remote machine: `ssh -i key_file -p 61769 ctf-player@saturn.picoctf.net`

I downloaded the disk image to my Linux VM and mounted it. There was two drives in the image, and one with the larger volume contained the key file.

```text
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a# ls
bin   dev  home  lost+found  mnt  proc  run   srv  tmp  var
boot  etc  lib   media       opt  root  sbin  sys  usr
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a# cd root
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a/root# ls -all
total 4
drwx------  3 root root 1024 10월  6 23:30 .
drwxr-xr-x 21 root root 1024 10월  6 23:28 ..
-rw-------  1 root root   36 10월  6 23:31 .ash_history
drwx------  2 root root 1024 10월  6 23:30 .ssh
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a/root# cd .ssh
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a/root/.ssh# ls
id_ed25519  id_ed25519.pub
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a/root/.ssh# ls -all
total 4
drwx------ 2 root root 1024 10월  6 23:30 .
drwx------ 3 root root 1024 10월  6 23:30 ..
-rw------- 1 root root  411 10월  6 23:30 id_ed25519
-rw-r--r-- 1 root root   96 10월  6 23:30 id_ed25519.pub
root@dem0s-Virtual-Machine:/media/dem0s/12d9658c-565f-42de-be97-eb4bfbe21b9a/root/.ssh# ssh -i id_ed25519 -p 61769 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:61769 ([18.217.86.78]:61769)' can't be established.
ECDSA key fingerprint is SHA256:0L/+wJ14/Sk4s6Ue+TxXnAW7qNBuaMeIxA9dXp2zzaU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:61769,[18.217.86.78]:61769' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1017-aws x86_64)


 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


This system has been minimized by removing packages and content that are
not required on a system that users do not log into.


To restore this content, you can run the 'unminimize' command.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.


Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_b5066e83}ctf-player@challenge:~$ 
```

**Flag: `picoCTF{k3y_5l3u7h_b5066e83}`**

## St3g0 (300 pts)

> Download this image and find the flag.
>
> * [Download image](sources/stego/stego.png)

The image is a logo of picoCTF. It is a image with transparent background and white text.

![logo](sources/stego/stego.png)

This problem is, as title suggests, a steganography problem. It could be solved by finding the right tool to decode the image. I was able to find the flag with `[zsteg](https://github.com/zed-0xff/zsteg)`.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/stego$ zsteg stego.png
b1,r,lsb,xy         .. text: "~__B>wV_G@"
b1,g,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 3549684369
b1,g,msb,xy         .. file: dBase III DBT, version number 0, next free block index 3418965897
b1,b,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 2623130757
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b3,b,msb,xy         .. file: StarOffice Gallery theme @\002 H\200\004H\002\004H\200$H\022\004H\200\004\010, 0 objects
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,lsb,xy      .. file: Novell LANalyzer capture file
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
b4,abgr,lsb,xy      .. file: Novell LANalyzer capture file
```

**Flag: `picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}`**

## Operation Orchid (400 pts)

> Download this disk image and find the flag.
>
> Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
>
> * [Download compressed disk image](sources/operation-orchid/disk.flag.img.gz)

The image contains three partitions, but only two of them can be mounted to Linux. The second partition contained files from Linux operating system. I browsed `root` and found a `flag.txt.enc` file.

```
```

When I used `ls -all root` command, I found an additional file: `.ash_history`, which contained the list of command that the `root` user entered in its terminal.

```text
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

The author used `openssl aes256` command to encrypt the flag with password `unbreakablepassword1234567` and a salt. So I decrypted the flag with the same command and key.

```text
dem0s@dem0s-Virtual-Machine:~$ openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140149858395456:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:610:
dem0s@dem0s-Virtual-Machine:~$ cat flag.txt
picoCTF{h4un71ng_p457_0a710765}
```

**Flag: `picoCTF{h4un71ng_p457_0a710765}`**

## SideChannel (400 pts)

> There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
>
> Download the PIN checker program here [pin_checker](sources/sidechannel/pin_checker)
>
> Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using `nc saturn.picoctf.net 55824` and provide it the PIN to get your flag.

The title of the problem suggested that this problem should be solved with a side-channel attack.

I wrote the [script](solutions/sidechannel.py) to test the program by entering 8-digit numbers with one of the digits varying from 0 to 9, and recording the processing time for each try. The first time I ran the script, I found that one of the numbers inserted to the program had a uniquely long processing time.

```text
00000000 : 0.13432
00000001 : 0.1188
00000002 : 0.11677
00000003 : 0.11685
... (skipped)
00000000 : 0.11815
10000000 : 0.11941
20000000 : 0.12211
30000000 : 0.12122
40000000 : 0.23402
50000000 : 0.12778
60000000 : 0.12107
70000000 : 0.12121
80000000 : 0.1234
90000000 : 0.12008
```

I figured that the PIN is somewhere between 40000000 and 49999999, and narrowed the search range accordingly.

```text

40000000 : 0.2345
41000000 : 0.23653
42000000 : 0.23897
43000000 : 0.23852
44000000 : 0.23794
45000000 : 0.2383
46000000 : 0.23884
47000000 : 0.23881
48000000 : 0.35163
49000000 : 0.23656

```

I narrowed the range once again to 48000000 ~ 48999999. This time, I got seven candidates for the range.

```text
48000700 : 0.46778
48000800 : 0.42425
48000900 : 0.41848
48000000 : 0.43515
48001000 : 0.43067
48002000 : 0.48931
48300000 : 0.47145
```

I chose to go with 48300000, and found another digit to get closer to the PIN.

```text
48310000 : 0.4734
48320000 : 0.47479
48330000 : 0.47533
48340000 : 0.47522
48350000 : 0.47525
48360000 : 0.47492
48370000 : 0.47554
48380000 : 0.47577
48390000 : 0.7129
```

Eventually, I discovered the PIN for the program at this range.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022$ nc saturn.picoctf.net 55824
Verifying that you are a human...
Please enter the master PIN code:
48390513
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_9803bd25}
```

**Flag: `picoCTF{t1m1ng_4tt4ck_9803bd25}`**

## Torrent Analyze (400 pts)

> SOS, someone is torrenting on our network.
>
> One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like `picoCTF{filename}`. [Captured traffic](sources/torrent-analyze.pcap).

From the PCAP file, the most likely culprit was the one using the IP address `192.168.73.132`. This user accessed `<torrent.ubuntu.com>` and 

At first, the captured packets were mostly made up of UDP packets. However, this was because of BT-DHT protocol analysis not being enabled in Wireshark. After I enabled the protocol, it turned out that some of the packets were in fact BT-DHT on UDP packets.

Filtering the BT-DHT packets originating from `192.168.73.132`, I noticed that most of those packets contained the same info hash:

```text
e2467cbf021192c241367b892230dc1e05c0580e
```

I searched for the torrent that corresponds to this hash, and found [the result](https://linuxtracker.org/index.php?page=torrent-details&id=e2467cbf021192c241367b892230dc1e05c0580e).

**Flag: `picoCTF{ubuntu-19.10-desktop-amd64.iso}`**

### (COMPLETED ALL CHALLENGES IN THIS CATEGORY)
