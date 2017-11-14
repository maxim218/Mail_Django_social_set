function controlSession() {
    let r = new XMLHttpRequest();
    r.open("GET", "/normal_user");
    r.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
    r.send(null);
    r.onreadystatechange = function() {
        if(r.readyState === 4 && r.status === 200) {
            const result = r.responseText + "";
            if(result !== "true") {
                window.location = "/";
            } else {
                console.log("Session OK");
            }
        }
    }
}

function htmlentities(s){
    s = s + "";
    let div = document.createElement('div');
    let text = document.createTextNode(s);
    div.appendChild(text);
    return div.innerHTML;
}

function getUserProperties(foo) {
    let r = new XMLHttpRequest();
    r.open("GET", "/get_user_properties");
    r.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
    r.send(null);
    r.onreadystatechange = function() {
        if(r.readyState === 4 && r.status === 200) {
            localStorage.setItem("UserProp", r.responseText + "");
            foo();
        }
    }
}

function goOut() {
    let r = new XMLHttpRequest();
    r.open("GET", "/go_out_of_session");
    r.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
    r.send(null);
    r.onreadystatechange = function() {
        if(r.readyState === 4 && r.status === 200) {
           window.location = "/";
        }
    }
}
