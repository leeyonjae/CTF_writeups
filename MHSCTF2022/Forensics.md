# Forensics

## Blank Slate (20 pts)

>My friend sent me this picture, and I'm not sure what to do with it! It seems a little... blank?

The file is a PNG with no visible image. However, taking a look with a hex code editor tells otherwise.

**Flag: `flag{get_grepped}`** (In hindsight, maybe the CTF makers expected participants to use `grep` to find it.)

## In Plain Sight (20 pts)

> Did you know that the Imagineers who helped build the Disney parks incorporated hidden images into their structures and designs? Many of their designs were in the shape of Mickey Mouse like the one in this image. What else might be hiding in plain sight?

The Image:

![image](images/inplainsight.png "Mickey Mouse-esque Logo")

This is a steganography problem. I found a [tool](https://stylesuxx.github.io/steganography/) that decoded the hidden message.

```text
"The way to get started is to quit talking and begin doing." -Walt Disney 

flag{H1dd3nM1ck3y}
```

**Flag: `flag{H1dd3nM1ck3y}`**

## Blank Slate 2 (25 pts)

> My friend is, once again, up to no good. They sent me this local git repository and it seems completely empty. Can you help me out here?

The zip file contains a git repository with a  `README`. The file contains the following message:

```md
# Welcome to my first repo!

I hope I don't accidentally put some secret information here! ;)


- Update: I did accidentally put some secret information here, but it's ok; I've taken care of it.
```

Also with the `README` file is a `.git` directory. Thanks to this, I could check the commit history of the repository. The history reveals that there was a file named `flag` that the author deleted. The deleted file contains the flag.

Flag: `flag{w4tch_0ut_f0r_g17_h15t0ry}`

## Chimera (25 pts)

> It's just one inside another...

I tried to open the PNG file with the viewer but there was nothing. Then I used GIMP to open it, which showed a transparent image featuring a two-headed beast.

A PNG file begins with a specific 8-byte code and ends with `IEND....`. Taking a look at the given image file with hex editor revealed that this file had two occurrences of both parts, one pair inside another. A different PNG file was nested in the original file.

I created a new PNG file by copying and pasting the nested part, which is:

![chimera](images/chimera2.png)

**Flag: `flag{4bs0rb3d}`**

## Blank Slate 3 (30 pts)

> My friend sent me another picture... It still looks blank!

At first glance, the image is just a pitch black canvas. However, if the exposure is manipulated, the letters appear:

![notBlank](images/blankslate3.png)

**Flag: `flag{1t$_n0t_3mpty}`**

## Blank Slate 4 (30 pts)

> There's something seriously wrong with my friend. They keep sending me these blank files! I hate to keep pestering you, but can you figure out what this one says?

This text file, opened with Notepad, seems empty. But when I press `End` key to reach the end of the line, the status bar states that I am at the 168th letter of the 1st line. So the empty text is not empty.

Given the nature of the problem, it must not simply be a bunch of whitespace. The hex editor output proves this.

```text
ef bb bf e2 80 8b 20 20 e2 80 8b e2 80 8b 20 20
e2 80 8b e2 80 8b 20 20 e2 80 8b 20 20 e2 80 8b
e2 80 8b e2 80 8b 20 20 e2 80 8b e2 80 8b e2 80
8b e2 80 8b 20 e2 80 8b 20 20 e2 80 8b e2 80 8b
20 20 20 e2 80 8b 20 20 20 20 e2 80 8b 20 20 e2
80 8b 20 20 20 e2 80 8b e2 80 8b 20 20 e2 80 8b
20 20 20 e2 80 8b 20 e2 80 8b e2 80 8b e2 80 8b
20 20 e2 80 8b 20 e2 80 8b e2 80 8b 20 e2 80 8b
e2 80 8b 20 20 e2 80 8b e2 80 8b e2 80 8b 20 e2
80 8b e2 80 8b 20 20 e2 80 8b e2 80 8b e2 80 8b
20 e2 80 8b 20 e2 80 8b 20 20 20 20 20 e2 80 8b
20 20 e2 80 8b 20 20 20 e2 80 8b e2 80 8b e2 80
8b 20 20 e2 80 8b e2 80 8b e2 80 8b e2 80 8b e2
80 8b 20 20 20 e2 80 8b 20 e2 80 8b e2 80 8b e2
80 8b 20 e2 80 8b 20 20 20 20 20 e2 80 8b 20 20
e2 80 8b e2 80 8b e2 80 8b 20 e2 80 8b e2 80 8b
e2 80 8b 20 20 e2 80 8b e2 80 8b e2 80 8b 20 e2
80 8b 20 20 e2 80 8b e2 80 8b e2 80 8b e2 80 8b
20 e2 80 8b 20 20 e2 80 8b 20 20 20 e2 80 8b e2
80 8b 20 20 e2 80 8b 20 e2 80 8b 20 20 e2 80 8b
20 20 20 20 20 e2 80 8b
```

Among the whitespaces (`0x20`) there are different bytes(`0xef`, `0xbb`, `0xbf`, `0xe2`, `0x80`, `0x8b`).

`ef bb bf` is the Byte Order Mark (BOM) of UTF-8, indicator of a UTF-8 with BOM text.

`e2 80 8b` is a code for "Zero-Width Space (ZWSP)." So this document is a mixture of whitespaces and zero-width spaces.

To visualize: (Z for zero-width, W for whitespace)

```text
ZWWZZWWZZWWZWWZZZWWZZZZWZWWZZWWWZWWWWZWWZWWWZZWWZWWWZWZZZWWZWZZWZZWWZZZWZZWWZZZWZWZWWWWWZWWZWWWZZZWWZZZZZWWWZWZZZWZWWWWWZWWZZZWZZZWWZZZWZWWZZZZWZWWZWWWZZWWZWZWWZWWWWWZ
```

All of the ZWSP steganography tools report that either there is no hidden message here or the hidden messages are also whitespaces.

It turns out that the file was a binary message using ZWSP and Whitespace. Convert ZWSP to 0 and Whitespace to 1, then:

```text
01100110 01101100 01100001 01100111 01111011 01110011 01110100 01101001 00110001 00110001 01011111 01101110 00110000 01110100 01011111 01100010 00110001 01100001 01101110 01101011 0111110 
```

Which converts to `flag{sti11_n0t_b1ank>`. It is evident that the missing last binary number is 1 which makes `01111101` that is `}`.

**Flag: `flag{sti11_n0t_b1ank}`**

## Blatant Corruption (40 pts)

> Something's wrong with this picture. Can you fix it for me?

The picture is a PNG file that does not show anything. Even VSCode shows error message instead of a preview.

Turns out this file does not have the first 4 bytes of a PNG file header.

Insert `0x89 0x50 0x4e 0x47` at the beginning of the file and the picture becomes visible.

![recovered](images/corrupt.png)

**Flag: `flag{str@ight_n_narr0w}`**
