// let a=5;
// let b=10;
// console.log(a+b);
// console.log(a-b);
// console.log(a*b);
// console.log(a/b);
// console.log(a%b);
// console.log(a**b);
// console.log(a++);
// console.log(++a);
// a>10?"true":"false";

// let n=prompt("Enter a number:");
// if(n%5===0){
//     console.log("Multiple of 5");
// }
// else{
//     console.log("Not Multiple of 5");
// }

// marks=prompt("Enter your marks")
// if (marks>=90 && marks<=100){
// console.log("A"); 
// } else if (marks>=79 && marks<=90){
// console.log("B"); 
// } else if (marks>=69 && marks<=80){
// console.log("C");
// } else if (marks>=59 && marks<=70){
// console.log("D");
// } else if (marks>=50 && marks<=60){
// console.log("E");
// }else if (marks>=0 && marks<=49){
// console.log("F");
// }

// let sum=0;
// for (let i=1; i<6;i++){
//     sum=sum+i;
// }
// console.log("sum: ",sum);
// console.log("Out of loop");

// let i=1
// sum =0;
// while (i<6){
//     sum=sum+i;
//     i++
// }
// console.log(sum)
// console.log(i)

// let i=10;
// do{
//     console.log(i);
//     i++;
// } while(i<20);
// console.log(i);


// for(i=0;i<101;i++){
//     console.log(i)
// }

// for(i=0;i<101;i++){
//     if(i%2!==0){
//         console.log(i)
//     }
// }

// let game=25;

// num=prompt("Guess the num")
// console.log(num);

// while(num!=game){
//     num=prompt("Wrong guess..Guess the num")
    
// }
// console.log("Gottcha");

// let str="Moulya";
// let str2='moulyakm';
// console.log(str[3])

// let sentence ='This is a literal string';
// console.log(sentence)

// let obj={
//     item:"pen",
//     price:10,
// };

// let output=`The cost of ${obj.item} is ${obj.price} rupees`;
// console.log(output)

// str="Moulya";
// str2=" K M";
// console.log(str.slice(0,3));
// console.log(str.concat(str2));

// name=prompt("Enter your name");
// username="@"+name+name.length;
// console.log(username);


// let marks=[97,98,99,89,88]
// for(let i=0;i<marks.length;i++){
//     console.log(marks[i]);
// }

// let marks=[97,98,99,89,88]
// for (let i of marks){
//     console.log(i);
// }

// let marks=[85,97,44,37,76,60]
// let sum=0
// for (let i=0;i<marks.length;i++){
//     sum+=marks[i];
// };
// console.log(sum);
// let avg=sum/marks.length;
// console.log(avg);


// let arr=[250,645,300,900,50];
// for (let i=0; i<arr.length;i++){
//     let offer=arr[i]/10;
//     arr[i]=arr[i]-offer;
//     console.log(arr[i])

// };

// let companies=["Bloom","Micro","Google","IBM"];
// companies.shift();
// companies.splice(3,1,"OLA");
// companies.push("Amazon")

// function my(){
//     console.log("Welcome");
//     console.log("ntg");
// }

// my();

// function sum(x,y){
//     s=x+y;
//     return s;
// }

// let summ=sum(100,200);
// console.log(summ);

// const arrmul=(a,b)=>{
//     console.log(a*b);
// }

// function countVow(str){
//     let count=0;
//     for (const i of str){
//         if( i==="a"||
//             i==="e"||
//             i==="i"||
//             i==="o"||
//             i==="u")
//             {
//             count++;
//         };
//     };
//      console.log(count);
// }

// 

// let arr=[1,2,3,4,5]

// arr.forEach((arr) => {
//     console.log(arr*arr);
// });

// let arr=[1,2,3,4,5]
// let newarr = arr.map((val) => {
//     return(val*2)
// })
// console.log(arr);
// console.log(newarr);

// let arr=[1,2,3,4,5,6]
// let newarr = arr.filter((val) => {
//    return val%2===0;
// })
// console.log(arr);
// console.log(newarr);

// let arr=[1,2,3,4,5,6]
// let output= arr.reduce((res,curr)=>{
//     return res+curr;
// })

// console.log(output);

// let arr=[1,2,3,14,5,6]
// let output= arr.reduce((prev,curr)=>{
//     return prev>curr?prev:curr;
// })

// console.log(output);

// let marks=[87,64,97,99,60,56];

// let newmarks=marks.filter((val)=>{
//     return val>90;
// })

// console.log(newmarks)

// n=prompt("Enter a num");

// let arr=[]

// for(let i=1;i<=n;i++){
//     arr[i-1]=i;
// }
// console.log(arr);

// let newarr =arr.reduce((prev,curr)=>{
//     return prev+curr;
// })

// console.log(newarr);

// let newarr2 =arr.reduce((prev,curr)=>{
//     return prev*curr;
// })

// console.log(newarr2);

// let h2 = document.querySelector("h2");
// console.dir(h2)

// h2.innerText = h2.innerText + " from Moulya";

// let divs= document.querySelectorAll(".box");

// let newbtn= document.createElement("button")
// newbtn.innerText = "click me";

// newbtn.style.color="white";
// newbtn.style.backgroundColor="red";
// document.querySelector("body").prepend(newbtn);

// let para = document.querySelector("p");

let modeBtn=document.querySelector("#btn");
let currMode="light"

modeBtn.addEventListener("click",()=>{
   if (currMode==="light"){
    currMode="dark";
    document.querySelector("body").style.backgroundColor="black";
   } else {
    currMode="light";
    document.querySelector("body").style.backgroundColor="white";
    }
    console.log(currMode);
   })

