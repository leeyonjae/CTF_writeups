# MHSCTF - Web Exploit Part

## James Harold Japp (10 pts)

> I need to be able to log in to this website. Can you tell me how to do it? mhsctf-jamesharoldjapp.0xmmalik.repl.co (you may need to wait for the site to wake up)

I entered the app and inspected its source code:

```html
<body>
  <div class="w3-content">
    <label for="pwd">Password:</label>
    <input type="password" id="pwd" name="pwd">
    <button onclick="validatepwd()" type="button">Submit</button>

    <script>
      function validatepwd() {
        var x = document.getElementById("pwd").value;
        if (x == "this_is_a_really_secure_password") {
          window.open("/weirdpage.php?pwd=doublepassword")
        }
      }
    </script>
  </div>
</body>
```

If you enter the suspect password `this_is_a_really_secure_password` and hit the `Submit` button, it opens a new page saying a 404 error.

However, this is a trick, as when you inspect the source code of the 404 page you see this:

```html
<!doctype html><html><head><!--lol gottem here's the flag: flag{1n$p3ct0r_g3n3r@l}--><title>404 Not Found</title>
... 
</head><body><h1>Not Found</h1><p>The requested resource <code class="url">/weirdpage.php?pwd=doublepassword</code> was not found on this server.</p></body></html>
```

You find the flag.

**Flag: `flag{1n$p3ct0r_g3n3r@l}`**

## new site who dis? (20 pts)

> I just started making my new website. Can you pen-test it and see if you can get the super-secret flag? mhsctf-newsitewhodis.0xmmalik.repl.co (you may need to wait for the site to wake up)

The site features a title and a link to supposed flag, but the flag page says that only the Admins can see it.

Using developer tool, Network tool in particular, I found a cookie named `user`, whose value was `basic`.

I used cookie editing tool to change the value to `admin`, and clicked the link to the flag and saw this result:

```text
Hello there, Admin! Here is your super-secret flag: flag{1t$-@_m3_Mari0}
```

**Flag: `flag{1t$-@_m3_Mari0}`**

## Bend (25 pts)

> I found this weird website that says it can give me a cool flag, but I can't seem to get it! What am I doing wrong? mhsctf-bend.0xmmalik.repl.co (you may need to wait for the site to wake up)

The website has a link to flag that instantly redirects to the music video of Rick Astley's "Never Gonna Give You Up."

In order to see what causes the redirection, I opened PowerShell and used `wget` command:

```powershell
PS C:\Users\USER> wget https://mhsctf-bend.0xmmalik.repl.co/flag


StatusCode        : 200
StatusDescription : OK
Content           : <meta http-equiv = "refresh" content = "0; url = https://www.youtube.com/watch?v=dQw4w9WgXcQ" />

                    <!-- flag{g3t_cur1ed} -->

RawContent        : HTTP/1.1 200 OK
                    Access-Control-Allow-Origin: *
                    Expect-Ct: max-age=2592000, report-uri="https://sentry.repl.it/api/10/security/?sentry_key=615192fd
                    532445bfbbbe966cd7131791"
                    Replit-Cluster: hacker
                    S...
Forms             : {}
Headers           : {[Access-Control-Allow-Origin, *], [Expect-Ct, max-age=2592000, report-uri="https://sentry.repl.it/
                    api/10/security/?sentry_key=615192fd532445bfbbbe966cd7131791"], [Replit-Cluster, hacker], [Strict-T
                    ransport-Security, max-age=6343441; includeSubDomains]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 124
```

Flag: `flag{g3t_cur1ed}`

## Piece It Together (25 pts)

> My friend dared me to find the secret password to their website, but their code is so messy! It's impossible to see what's what! Can you help me? mhsctf-pieceittogether.0xmmalik.repl.co (you may need to wait for the site to wake up)

Most of the source code is cloaked in the series of HTML Entity codes. Decoding it first time leads to new set of HTML Entity codes, so it needs to be decoded again.

If we decode it (twice):

```html
<noscript>  
  <head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&family=Exo+2&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://mhsctf-webexploitdata.0xmmalik.repl.co/style.css">
  </head>
  <body>
  <div class="w3-content">
    <h2>Login</h2>
    <script>
var _0xa8fe=["4w","d}","g{","j","}","1g","w0","r","al","s","h7","ag{","fl","m3t","value","pwd","getElementById","Yep, that's the flag!","Sorry, that's not the flag!"];
function checkpwd(){
  if(document[_0xa8fe[16]](_0xa8fe[15])[_0xa8fe[14]]== (_0xa8fe[12]+ _0xa8fe[11]+ _0xa8fe[3]+ _0xa8fe[5]+ _0xa8fe[9]+ _0xa8fe[0]+ _0xa8fe[4]))
  {alert(_0xa8fe[17])}
  else 
  {alert(_0xa8fe[18])}}
    </script>

    <label for="pwd">Password:</label>
    <input type="text" id="pwd" name="pwd">
    <button onclick="checkpwd()">Submit</button>
  </div>
 </body>
```

To simplify the `<script></script>` portion further:

```js
var _0xa8fe=["4w", // 0
  "d}", // 1
  "g{", // 2
  "j",  // 3
  "}",  // 4
  "1g", // 5
  "w0", // 6
  "r",  // 7
  "al", // 8
  "s",  // 9
  "h7", // 10
  "ag{",// 11
  "fl", // 12
  "m3t",// 13
  "value",// 14
  "pwd",// 15
  "getElementById", // 16
  "Yep, that's the flag!", // 17
  "Sorry, that's not the flag!"] // 18;
function checkpwd(){
  if(document["getElementById"]("pwd")["value"]== ("fl"+ "ag{"+"j"+"1g"+"s"+"4w"+"}")
  {alert(_0xa8fe[17])} // "Yep, that's the flag!"
  else 
  {alert(_0xa8fe[18])}}// "Sorry, that's not the flag!"

```

**Flag: `flag{j1gs4w}`**

## Cuppa Joe (30 pts)

> A new coffee shop is opening up in my neihborhood! It's called Cuppa Joe and I can't wait to check it out! It would ahem be a real shame if someone were to ahem hack their website and, hypothetically, get their secret flag. mhsctf-cuppajoe.0xmmalik.repl.co (you may need to wait for the site to wake up)

The website is composed of a sitemap with unfinished links, greeting message, and a form to leave our message. When submitted, the form redirects to a Thank you note that displays what I entered.

One of the links in the sitemap is named `flag.php`, but clicking it does nothing. When I add `flag.php` to the address bar, it simply says:

> I don't know how you got here, please leave.

So it must need some privilege or a `POST` input.

I decided to exploit the contact form, hoping to escalate privilege by inserting an `iframe` tag in it:

```html
<iframe src="flag.php" width=1100 height=100>
```

This input actually created an `iframe` to `flag.php` that revealed the flag.

> Here's a flag: flag{c0ff33_be4nz}

**Flag: `flag{c0ff33_be4nz}`**
