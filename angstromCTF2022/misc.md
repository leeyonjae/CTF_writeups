# AngstromCTF - Miscellaneous

## Interwebz (20 pts)

> Clam's super powerful mega server of doom is running all of ångstromCTF's infrastructure! For many challenges, it's important that you're able to connect to it. Get a free flag by connecting to `nc challs.actf.co 31335`.

This is a simple warm-up problem. The flag can be obtained by simply connecting to the server using `nc` command.

```text
8M:/mnt/d/GitHub/angstromCTF2022$ nc challs.actf.co 31335
actf{plugged_in_and_ready_to_go}
```

**Flag: `actf{plugged_in_and_ready_to_go}`**

## Confetti (40 pts)

> "From the sky, drop like confetti All eyes on me, so V.I.P All of my dreams, from the sky, drop like confetti" - Little Mix [confetti.png](misc/confetti/confetti.png)

The image file shows confetti with no background (i.e., its background is transparent). But its file size seems suspiciously large for a simple image. When opened with hex editor, the file continues long after `IEND` section appears, and there are more than one PNG signatures. It seems that the file is a collection of multiple PNG images.

The following is the [Python script](misc/confetti/confetti.py) to extract the individual PNG files from the original.

```python
confetti = open("./confetti.png", "rb").read().split(b'\x89PNG')

for i in range(1, len(confetti)):
    out = open("./confetti" + str(i) + ".png", "wb")
    res = b'\x89PNG' + confetti[i]
    out.write(res)
    out.close()

```

The flag is hidden in the [third output](misc/confetti/confetti3.png).

**Flag: `actf{confetti_4_u}`**

## amongus (40 pts)

> One of [these](misc/amongus.tar.gz) is not like the others.

The TAR.GZ file contains a thousand text files, all named in flag format. Each file contains a large hexadecimal number. The problem statement seems to ask us to find the one that stands out. But each text file contains a unique number, so the difference of contents is definitely not the answer.

It turns out that the odd one can be found by comparing the sizes of the files by, for instance, using `ls -all` command.

```text
8M:/mnt/d/GitHub/angstromCTF2022/misc/out$ ls -all
...
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b18f29fb8d5c}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b19d011a4da5}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b1b4714163ef}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b205645b3ad8}.txt
-rwxrwxrwx 1 yonjae yonjae 20001 Apr 27 21:46 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b21f9732f829}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b28d14a08b47}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b2b75082b5df}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b2e73df3d9e4}.txt
-rwxrwxrwx 1 yonjae yonjae 20000 Apr 27 21:45 actf{look1ng_f0r_answers_in_the_p0uring_r4in_b333b706ed79}.txt
...
```

All but one files have 20,000 bytes; the other one has one more byte than the rest.

**Flag: `actf{look1ng_f0r_answers_in_the_p0uring_r4in_b21f9732f829}`**

## Shark 1 (70 pts)

> My friend was passing notes during class. Can you find them? [here](misc/shark1.pcapng)

The flag can be seen in plaintext form in the 22nd frame captured in the file. It is preceded by a message "Here is the flag:" in the 16th frame.

**Flag: `actf{wireshark_doo_doo_doo_doo_doo_doo}`**

## Shark 2 (70 pts)

> My friend hasn't [learned](misc/shark2.pcapng).

Since the TCP communication in this capture is not encrypted, the conversation can be recovered easily.

```text
Frame 22
Hello :)

Frame 26
Hi, do you have the image for our project?

Frame 30
Yeah, sending it now
```

After these exchanges, one sends another a series of TCP packets containing parts of an image file. Export these data and combine them into a [single image file](misc/shark2.jfif), and you can see the flag.

**Flag: `actf{i_see_you}`**
