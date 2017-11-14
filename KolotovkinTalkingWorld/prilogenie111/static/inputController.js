function correctChar(c) {
    const s = "abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789";
    return s.indexOf(c) !== -1;
}

function correctString(s) {
    if(s.length === 0) {
        return false;
    }

    for(let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        if(correctChar(c) === false) {
            return false;
        }
    }

    return true;
}
