# CTAMU CTF - Web

## Triplet

> This website looks like it was made for the Netscape and AOL era, but there is a flag somewhere in there. Find it and get the points.

This is a classic 'view source code' problem. Look at the source code of the webpage and take a look at the stylesheet and the script as well.

```html
html commend

<!DOCTYPE html>
<html>                                  
<head>                                  
    <script src="script.js"></script>   
    <link rel="stylesheet" type="text/css" href="style.css"/>                                                                  
    <title>DEFAULT SITE</title>         
</head>                                 

<body>                                  
        <h1>LOREM IPSUM</h1>            

        <div class="container">         
                <a href="#">LINK</a>    
        </div>                          
        <div class="container">         
                <button onclick="doTheStuff()">BUTTON</button>                                                                 
        </div>                          

        <div class="container">         

        <p>                             
Lorem ipsum dolor sit amet, (skipped)
        </p>
        </div>
</body>

<!--
gigem{ThReE_PaRtS
-->
</html>
```

```css
/*style.css*/
body {
    text-align: center;
    font-family: 'Anek Odia', sans-serif;
    font-size: 125%;
    color: white;
    background: #312F2F;
}

.container {
    max-width: 40em;  
    margin-left: auto;
    margin-right: auto; 
    padding: 0.5rem;
}

a {
    color: #B0D0D3;
    padding: 1rem;
}

button {
    cursor: pointer;
    background-color: #FFCAD4;
    border: none;
    padding: 12px 28px;
}

/* _tO_wEb_HTML_CSS_ */

```

```javascript

/* script.js */

function doTheStuff() {
    alert("HOWDY THERE!");
}

// AND_JS_0xCHICKEN}
```

Each file contains a comment that is a part of the flag.

**Flag: `gigem{ThReE_PaRtS_tO_wEb_HTML_CSS_AND_JS_0xCHICKEN}`**
