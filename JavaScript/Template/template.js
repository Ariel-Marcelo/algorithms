function main() {
    //var i = nextInt();
    //var s = nextString();
    //var c = nextChar();
    //var f = nextFloat();

    var testCasesNum = nextInt();

    var gMaximunPower;

    while (testCasesNum > 0) {

        var bCapacity = nextInt();//6
        var gToChoose = nextInt();//2


        let gWeight = []; 
        let gPower = [];

        for(i = gToChoose; i > 0; i--) {
            gWeight.push(nextInt());
            gPower.push(nextInt());
        }

        // encontremos el gMaximunPower

      

        
            let maxIndex = gPower.findIndex(p => p = Math.max(...gPower));
            if (gWeight[maxIndex] <= bCapacity) {
                maxFind = true;
                gMaximunPower =  gPower[maxIndex];
            } else {
                gPower.splice(maxIndex, 1);
            }
        
        console.log(gMaximunPower);
        testCasesNum--;
    }
}

// default parsers for JS.
function nextInt() {
    return parseInt(nextString());
}

function nextFloat() {
    console.log("my integer is: " + i);
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
