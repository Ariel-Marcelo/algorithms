function main(){
    let myArray = [];
    let myArray2 = [2,3];
    let myArray3 = [3,2];
    myArray.push(myArray2);
    myArray.push(myArray3);
    myArray.push(10);
    console.log(myArray[2]);
    /*
    let maximun = Math.max(...myArray);
    console.log(maximun);
    let index = myArray.findIndex( (p) => p === maximun);
    console.log(`${index}`);


    let myIndex = myArray.findIndex( (p) => p === Math.max(...myArray));
    console.log(myIndex);

    myArray.sort((a,b) => a - b);
    console.log(myArray);
    */
}

main();