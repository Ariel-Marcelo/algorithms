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
    for(let index = 0; index <= n; index++){
        w = nextInt();
        f = nextInt();
        let myAux = [];
        console.log( `1` );
        for(let j = 0; j <= c; j++){
            if(index == 0){
                myAux.push(0);
            }else{
                if(w <= j){
                    let aux = j - w;
                    if(f < myMatrix[index -1][j]){
                        myAux.push(myMatrix[index -1][j]);
                    }else{
                        myAux.push(f); 
                    }
                    myAux[j] = myAux[j] + myMatrix[index-1][aux];
                }else{
                    myAux.push(myMatrix[index - 1][j]);
                }
            }
            
        }
        myMatriz.push(myAux);
        
    }
    console.log(myMatriz);
    console.log(myMatriz[n + 1][c + 1]);
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

main();