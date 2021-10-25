function main(){
    let myArray = [];
    myArray.push(5);
    myArray.push(4);
    myArray.push(10);
    myArray.push(2);
    console.log(myArray);
    let maximun = Math.max(...myArray);
    console.log(maximun);
    let index = myArray.findIndex( (p) => p === maximun);
    console.log(index);


    let myIndex = myArray.findIndex( (p) => p === Math.max(...myArray));
    console.log(myIndex);

    myArray.sort((a,b) => a - b);
    console.log(myArray);
}

main();