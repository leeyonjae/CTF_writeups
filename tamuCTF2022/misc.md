# TAMU CTF - Misc

## Hear Me Out

> You overheard some suspicious people typing on their phones, what are they saying?
>
> The flag format is `gigem{messagewithoutspace}`, case-insensitive.

The [audio file](misc/hear-me-out/hear-me-out.mp3) contains sounds of telephone dialing. Using [online decoder](http://dialabc.com/sound/detect/) (you need to convert the file to WAV format first), we can find that whoever used the phone dialed `44422226684433277788`. This number in turn is encrypted [Multi-tap](https://www.dcode.fr/multitap-abc-cipher) ciphertext. The decrypted plaintext is `ICANTHEARU`.

**Flag: `gigem{ICANTHEARU}`**

## Gamer

> I was vibing in VC with my gamer friends when I stumbled across a mysterious in-game inscription. Can you figure out what it means?
>
> Flag format is case-insensitive.

The [file](misc/gamer/sus.txt) contains a Minecraft monster summon script. It summons a bat that holds a treasure chest that contains bunch of banners. The banners, when seen in the order written in the script, resemble the following string: `GIGEMEMINE_DIAMONDZ3`.

Below is the list of URLs that direct to a Minecraft banner viewer showing each banner.

```text
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14rs0hh14bs0ls0ts0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14cs0ts0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14rs0hh14bs0ls0ts0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ls0ts0ms0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14tt0tts14ls0rs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ms0rs14ts0ls0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14tt0tts14ls0rs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14cs0ts0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ls0tt14drs0rs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ls0ts0ms0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14bs0
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14rs0bs0ts0cbo14ls0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14cs0ts0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14rs0ls0ms0ts0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14tt0tts14ls0rs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ls0rs0bs0ts0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ls0tt14drs0rs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14rs0bs0ts0cbo14ls0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ts0dls0bs0bo14
https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14ms0ls14ts0rs0bs0bo14
```

You can obtain the flag by replacing the second `E` and the final `3` to left and right curly braces respectively.

**Flag: `gigem{MINE_DIAMONDZ}`**
