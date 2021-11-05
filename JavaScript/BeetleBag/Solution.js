function main() {
    // t = test cases
    // c = capacity of bag
    // n = gadgets in laboratory
    // w  = weigh
    // f = power
    // t
    // c n
    // w p

    var t =  nextInt();
    for(let index = 0; t > index; index++) {
        sol();
    }
}

function sol() { 
    
    let c = nextInt();
    let n = nextInt();
    
    myMatriz = [];
    
    let a = [];
    for(let index = 0; index <= c; index++){
        a.push(0);
    }
    myMatriz.push(a);
    
    for(let index = 1; index <= n; index++){
        w = nextInt();
        f = nextInt();
        let myAux = [];
        for(let j = 0; j <= c; j++){
                if(w <= j){
                    let aux = j - w;
                    let a = f + myMatriz[index-1][aux];
                    let b = myMatriz[index - 1][j];
                    myAux.push(Math.max(a,b));
                }else{
                    myAux.push(myMatriz[index - 1][j]);
                }
        }
        myMatriz.push(myAux);
    }
    
    console.log(myMatriz[n][c]);
}
// default parsers for JS.
function nextInt() {
    return parseInt(nextString());
}

function nextFloat() {
    return parseFloat(nextString());
}

function nextString() {
    var next_string = "";
    clearWhitespaces();
    while (input_cursor < input_stdin.length && !isWhitespace(input_stdin[input_cursor])) {
        next_string += input_stdin[input_cursor];
        input_cursor += 1;
    }
    return next_string;
}

function nextChar() {
    clearWhitespaces();
    if (input_cursor < input_stdin.length) {
        return input_stdin[input_cursor++];
    } else {
        return '\0';
    }
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_cursor = 0;
process.stdin.on('data', function (data) { input_stdin += data; });
process.stdin.on('end', function () { main(); });

function isWhitespace(character) {
    return ' \t\n\r\v'.indexOf(character) > -1;
}

function clearWhitespaces() {
    while (input_cursor < input_stdin.length && isWhitespace(input_stdin[input_cursor])) {
        // ignore the next whitespace character
        input_cursor += 1;
    }  
}