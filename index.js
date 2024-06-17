// const na = 24;
// console.log(na);

// // generate a random number
// let randomNum = Math.floor(Math.random() * 100) + 1;

// //randomNum = Math.round(randomNum);
// console.log(randomNum);

// to get random numbers from 50 to 100

// const min = 50;
// const max = 100;
// let randomNum = Math.floor(Math.random() * (max - min)) + min;
// console.log(randomNum);

// const myButton = document.getElementById("myButton");
// const label1 = document.getElementById("label1");
// const label2 = document.getElementById("label2");
// const label3 = document.getElementById("label3");
// let min = 1;
// let max = 100;
// let randomNum1;
// let randomNum2;
// let randomNum3;

// myButton.onclick = function () {
//   randomNum1 = Math.floor(Math.random() * max) + min;
//   randomNum2 = Math.floor(Math.random() * max) + min;
//   randomNum3 = Math.floor(Math.random() * max) + min;
//   label1.innerHTML = randomNum1;
//   label2.innerHTML = randomNum2;
//   label3.innerHTML = randomNum3;
// };

// IF statements: if a codnition is true then execute some code
//               : if not, then execute the else statement

// let age = 33;

// if (age >= 18) {
//   console.log("you are eligible to vote for the election");
// } else {
//   console.log("you are not eligible to vote for the election");
// }

// let time = 14;

// if (time < 12) {
//   console.log("good morning");
// } else {
//   console.log("good afternoon");
// }

// with boolean varibales

// let iStudent = false;
// if (iStudent) {
//   console.log("you are a student");
// } else {
//   console.log("you are not a student");
// }

// let age = 15;
// if (age >= 18) {
//   console.log("you are old enough to drive the vehicle");
// } else {
//   console.log("You must be 16+ to have a licence to drive the vehicle");
// }

//let age = 19;
// let hasLicence = false;
// if (age >= 18) {
//   console.log("you are old enough to drive the vehicle");
//   if (hasLicence) {
//     console.log("you have your won licence");
//   } else {
//     console.log("But!! you do not have your own licence");
//   }
// } else {
//   console.log("You must be 16+ to have a licence to drive the vehicle");
// }

// lets discuss if else statements

// const myText = document.getElementById("myText");
// const mySubmit = document.getElementById("mySubmit");
// const resultElement = document.getElementById("resultElement");
// let age;

// mySubmit.onclick = function () {
//   age = myText.value;
//   age = Number(age);

//   if (age >= 100) {
//     resultElement.textContent = "You are TOO OLD to enter this site";
//   } else if (age == 0) {
//     resultElement.textContent =
//       "You can't enter the site. Bcoz you were just born";
//   } else if (age > 18) {
//     resultElement.textContent = "you are old enough to enter the site";
//   } else if (age < 0) {
//     resultElement.textContent = "your age can't be below 0";
//   } else {
//     resultElement.textContent = "you must be 18+ to enter the site";
//   }
// };

// const myCheckBox = document.getElementById("myCheckBox");
// const visaBtn = document.getElementById("visaBtn");
// const masterCardBtn = document.getElementById("masterCardBtn");
// const paypalBtn = document.getElementById("paypalBtn");
// const americanExpressBtn = document.getElementById("americanExpressBtn");
// const mySubmit = document.getElementById("mySubmit");

// const subResult = document.getElementById("subResult");
// const paymentResult = document.getElementById("paymentResult");

// mySubmit.onclick = function () {
//   if (myCheckBox.checked) {
//     subResult.textContent = "You are subscribed to our website.";
//   } else {
//     subResult.textContent = "You are not subscribed to our website.";
//   }

//   if (visaBtn.checked) {
//     paymentResult.textContent = `You are paying with Visa.`;
//   } else if (masterCardBtn.checked) {
//     paymentResult.textContent = `You are paying with masterCard.`;
//   } else if (paypalBtn.checked) {
//     paymentResult.textContent = `You are paying with paypal.`;
//   } else if (americanExpressBtn.checked) {
//     paymentResult.textContent = `You are paying with American Express.`;
//   } else {
//     paymentResult.textContent = `You must select a payment type.`;
//   }
// };

// ternary operators = it is an shortcut operator to if {} and else if {}statements
//                     helps to assign variables based on the operators.
//                     consition ? ifcodeIsTrue : ifcodeIsFalse

// let age = 22;
// let message = age >= 18 ? `you are an adult` : `you are a minor`;
// console.log(message);

// let time = 16;
// let greeting = time < 12 ? `good morining` : `good afternoon`;
// console.log(greeting);

// let istudent = false;
// let message = istudent ? `you are a student` : `you are not a student`;
// console.log(message);

// let purchaseAmount = 125;
// let discount = purchaseAmount >= 100 ? 10 : 0;
// console.log(
//   `your total amount is ${purchaseAmount - purchaseAmount * (discount / 100)}`
// );

// SWITCH statement in Js: can be efficiently replacement to many else if statements

// let day = "sunny";

// switch (day) {
//   case 1:
//     console.log(" It is Monday");
//     break;
//   case 2:
//     console.log("It is Tuesday");
//     break;
//   case 3:
//     console.log("It is Wednesday");
//     break;
//   case 4:
//     console.log("It is Thursday");
//     break;
//   case 5:
//     console.log("It is Friday");
//     break;
//   case 6:
//     console.log("It is Saturday");
//     break;
//   case 7:
//     console.log("It is Sunday");
//     break;
//   default:
//     console.log(`${day} is Invalid day`);
//     break;
// }

// let testScore = 52;
// let letterGrade;

// switch (true) {
//   case testScore >= 90:
//     letterGrade = "A";
//     break;
//   case testScore >= 80:
//     letterGrade = "B";
//     break;
//   case testScore >= 70:
//     letterGrade = "C";
//     break;
//   case testScore >= 60:
//     letterGrade = "D";
//     break;
//   case testScore >= 50:
//     letterGrade = "E";
//     break;
//   case testScore >= 40:
//     letterGrade = "F";
//     break;
//   case testScore >= 30:
//     letterGrade = "G";
//     break;
//   case testScore >= 20:
//     letterGrade = "H";
//     break;
//   case testScore >= 10:
//     letterGrade = "I";
//     break;
//   case testScore >= 0:
//     letterGrade = "J";
//     break;
//   default:
//     letterGrade = "K";
//     break;
// }

// console.log(letterGrade);

// strings in js= strings allow you to manipulates and work wth the text(strings in js)

// let nameIs = `BroCode`;
// //console.log(nameIs.charAt(2));
// //console.log(nameIs.indexOf(`o`));
// //console.log(nameIs.lastIndexOf(`o`));
// console.log(nameIs.length);

// console.log(nameIs.trim()); // reomove the white spaces

// console.log(nameIs.toUpperCase());

// console.log(nameIs.toLowerCase());

// console.log(nameIs.repeat(3)); // repeats the strings how many times you want

// console.log(nameIs.startsWith(" "));

// console.log(nameIs.startsWith("B"));

// console.log(nameIs.endsWith("e"));

// console.log(nameIs.includes(" ")); // gives true if spaces is included between strings
// // example: "Bro code" => true and "Brocode" => false

// let phoneNumber = 123 - 456 - 789;

// phoneNumber = phoneNumber.replaceAll("-", "");
// console.log(phoneNumber);

// string slicing: creates a substring from the portion of another string
//                 syntax: string.slice(start,end).

// const fullName = `Bro code`;
// let firstName = fullName.slice(0, 3);
// let lastName = fullName.slice(4);

// let fullNe = fullName.slice(-1);

// console.log(fullName);
// console.log(firstName);
// console.log(lastName);

// const email = `Bro@gmail.com`;

// let username = email.slice(0, email.indexOf("@"));
// let extension = email.slice(email.indexOf("@"));

// console.log(username);

// console.log(extension);

// Method chaining = Calling one method after another
//                   in one continuous line of code

//         ------ NO METHOD CHAINING ------

// let username = window.prompt("enter your name");

// username = username.trim();
// let letter = username.charAt(0);
// letter = letter.toUpperCase();

// let extraChar = username.slice(1);
// extraChar = extraChar.toLowerCase();
// username = letter + extraChar;

// console.log(username);

//             -------- METHOD CHAINING ------

// username =20
//   username.trim().charAt(0).toUpperCase() +
//   username.trim().slice(1).toLocaleLowerCase();
// console.log(username);

// logical operators = used to combine or manipulate boolean values
//                      (true or false)
// logical operators are: i. logical AND &&
//                        ii. logical OR ||
//                        iii.logical NOT !

// const temp = 25;
// if (temp > 0 && temp <= 50) {
//   console.log("The weather is GOOD");
// } else {
//   console.log("The eather is BAD");
// }

// const temp = 250;
// if (temp < 0 || temp < 50) {
//   console.log("The weather is GOOD");
// } else {
//   console.log("The weather is BAD");
// }

// const temp = true;
// if (temp) {
//   console.log("The weather is GOOD");
// } else {
//   console.log("The eather is BAD");
// }

// = assignment operators
// == comparison operators (compares if values are equal)
// === strict equality operators(compares if values and datatypes are equal)
// != inequality operator
// !== strictly inequality operator

// const PI = 3.14;
// if (PI != "3.14") {
//   console.log("This is NOT PI");
// } else {
//   console.log("This is PI");
// }

// const PI = 3.14;
// if (PI !== "3.14") {
//   console.log("This is NOT PI");
// } else {
//   console.log("This is PI");
// }

// while loop in js repeats the line of code WHILE some condition is true

// let username = "BroCode";
// if (username === "") {
//   ConstantSourceNode.log("Ye");
// }
// console.log("Username:Hello " + username);

// let username = "";
// while (username === "") {
//   username = window.prompt("PLEASE Enter username");
// }
// console.log(`Hello ${username}`);

// for loop = repeats some code a limited amount of times

// for(let i = 0; i<=2; i++){
//     // console.log("Hello");
//     console.log(i);
// }


// for(let i = 1; i<=10; i++){
//     console.log(i);
//     i +=2;
// }


// for(let i = 1; i<=10; i+=2){
//     console.log(i);
// }


// for(let i = 2; i<=10; i+=2){
//     console.log(i);
// }


// for(let i = 10; i>0; i--){
//     console.log(i);
// }

// console.log("HAPPY NEW YEAR")

// for(let i = 10; i>0; i-=2){
//     console.log(i);
// }

// console.log("HAPPY NEW YEAR")


// for (let i = 0; i <= 20; i++) {
//     if (i == 5) {
//         break;
//     }
//     else {
//         console.log(i);
//     }
// }


// for (let i = 0; i <= 20; i++) {
//     if (i == 5) {
//         continue;
//     }
//     else {
//         console.log(i);
//     }
// }

// NUMBER GUESSING GAME in jS
// const maxNum = 100;
// const minNum = 1;
// const answer = Math.floor(Math.random() * (maxNum - minNum + 1));
// console.log(answer);

// let attempts = 0;
// let guess;
// let running = true;

// while (running) {
//     guess = window.prompt(`Enter a number between ${minNum} - ${maxNum}`);
//     guess = Number(guess);

//     if (isNaN(guess)) {
//         window.alert("Please enter a valid number");
//     }
//     else if (guess < minNum || guess > maxNum) {
//         window.alert(`Please enter number with in ${minNum} - ${maxNum}`);
//     }
//     else {
//         attempts++;
//         if (guess < answer) {
//             window.alert("TOO LOW! TRY AGAIN!");
//         }
//         else if (guess > answer) {
//             window.alert("TOO HIGH! TRY AGAIN!");
//         }
//         else {
//             window.alert(`CORRECT! The answer was ${answer}. It took you ${attempts} attempts.`);
//             running = false;
//         }
//     }
// }


// function = A function is a set of reusable code.
//            Declare the function code once, use it whereever you want.
//            Call the function to execute that code.


// function happYBirthday() {
//     console.log("HAppy birthday");
//     console.log("HAppy birthday to universe");
//     console.log("HAppy birthday that candi");
// }
// happYBirthday();
// happYBirthday();


// function happYBirthday(username, age) {
//     console.log(`Happ birthday to you ${username}`);
//     console.log("HAppy birthday to universe");
//     console.log(`You are now ${age} old!`);
// }
// happYBirthday(`Tara`, 22);


// return key word in javascript

// function add(x, y) {
//     let result = x + y;
//     return result
// }

// // let answer = add(2, 6);
// // console.log(answer);
// console.log(add(2, 6));



// function add(x, y) {
//     return x + y;
// }


// function isEven(number) {
//     if (number % 2 === 0) {
//         return true;
//     }
//     else {
//         return false;
//     }
// }
// console.log(isEven(13));




// function isEven(number) {
//     return number % 2 === 0 ? true : false;
// }
// console.log(isEven(13));



// function isValidemail(email) {
//     if (email.includes("@")) {
//         return true;
//     }
//     else {
//         return false
//     }
// }
// console.log(isValidemail("bro@.com"));
// console.log(isValidemail("abc.com"));



// ternary operators method
// function isValidemail(email) {
//     return email.includes("@") ? true : false;
// }
// console.log(isValidemail("bro@.com"));
// console.log(isValidemail("abc.com"));



// variables scope = where a variable is recognised
//                   and accessible (local and global)
// local variable is the variable which is declared inside the function.


// function2();
// function function1() {
//     let x = 3;
//     console.log(x);
// }

// function function2() {
//     console.log(x);
// }

// global variable is the variable which is declared outside the function.
// example recommendable to only small programs only

// let x = 3;

// function1();
// function function1() {
//     let x = 1;
//     console.log(x);
// }

// function function2() {
//     let x = 2
//     console.log(x);
// }


// TEMPERATURE CONVERSION PROGRAM I=USING JS

// const textBox = document.getElementById("textBox");
// const toFahrenheit = document.getElementById("toFahrenheit");
// const toCelsius = document.getElementById("toCelsius");
// const result = document.getElementById("result");
// const conversionForm = document.getElementById("conversionForm");

// conversionForm.addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent form submission and page reload
//     convert();
// });

// function convert() {
//     let temp;
//     if (toFahrenheit.checked) {
//         temp = Number(textBox.value);
//         temp = temp * 9 / 5 + 32;
//         result.textContent = temp.toFixed(1) + "°F";
//     } else if (toCelsius.checked) {
//         temp = Number(textBox.value);
//         temp = (temp - 32) * (5 / 9);
//         result.textContent = temp.toFixed(1) + "°C";
//     } else {
//         result.textContent = "Select a unit";
//     }
// }


// Array= array is an collection of similar like structure of data types that can hold
//        more than one value

//let fruits = [`apple`, `banana`, 'grapes', `oranges`];
//fruits[1] = `coconut`;
//fruits.push(`coconut`); // add at the end of array
//fruits.unshift(`mango`) // add at the beginning of array
//fruits.pop(`coconut`);
//fruits.shift(); // delete end of array element

// console.log(fruits);
// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[2]);
// console.log(fruits[3]);

// let nuOffruits = fruits.length
// console.log(nuOffruits)

// let index = fruits.indexOf("grapes");
// console.log(index);


// for (let i = 0; i < fruits.length; i++) {
//     console.log(fruits[i]);
// }

// for (let i = 0; i < fruits.length; i += 2) {
//     console.log(fruits[i]);
// }

// for (let i = fruits.length - 1 ; i >= 0; i--) {
//     console.log(fruits[i]);
// }


// for (let fruit of fruits) {
//     console.log(fruit);
// }

// to sort array
// fruits.sort().reverse();
// for (let fruit of fruits) {
//     console.log(fruit);
// }


// spread operator = ... allows you to iterate such as an
//                   array or strings to be expanded into
//                   seperate elements
//                   it is like unpacking the elements from bunch of elements.


//let numbers = [1, 2, 3, 4, 5];
//console.log(numbers);

// to get the max number
// let maxNum = Math.max(numbers);
// console.log(maxNum); // it wont give output and show as NaN

// to get the output use ...
// let maxNum = Math.max(...numbers);
// console.log(maxNum); // it gives 5

// let minNum = Math.min(...numbers);
// console.log(minNum);


// to spread the strings into single letters
// let name1 = "BroCode";
// let spread = [...name1];
// console.log(spread);

// let name1 = "BroCode";
// let spread = [...name1];
// console.log(spread.join("-"));

// to create a shallow copy
// we can combine two or more array using ... operator in javascript
// let fruits = [`apple`, `grape`, `pine`, `honey`];
// let newFruit = [...fruits];
// console.log(newFruit); // here we created two new array one is fruits another is newFruits


// let fruits = [`apple`, `grape`, `pine`, `honey`];
// let vegertabels = [`spinach`, `potato`, `carrots`, `tomato`]

// let food = [...fruits, ...vegertabels]
// console.log(food);


// let fruits = [`apple`, `grape`, `pine`, `honey`];
// let vegertabels = [`spinach`, `potato`, `carrots`, `tomato`]

// let food = [...fruits, ...vegertabels, `egg`, `milk`];
// console.log(food);


// rest parameters = (...rest) allows a function to work with a variable number
//                  number of arguments by bundling them into an array.
//                 spread = expands an array into seperate elements.
//                 rest = bundles seperate elements into an array


// function food(...foods) {
//     console.log(foods);
// }

// const food1 = 'pizza';
// const food2 = 'hamBurger';
// const food3 = 'sushi';
// const food4 = 'hotdog';
// const food5 = 'ramen';

// food(food1, food2, food3, food4, food5);

// function food(...foods) {
//     console.log(...foods); // used to spread
// }

// const food1 = 'pizza';
// const food2 = 'hamBurger';
// const food3 = 'sushi';
// const food4 = 'hotdog';
// const food5 = 'ramen';

// food(food1, food2, food3, food4, food5);

// function food(...foods) {
//     console.log(...foods);
// }
// function getFood(...foods) {
//     return foods;
// }

// const food1 = 'pizza';
// const food2 = 'hamBurger';
// const food3 = 'sushi';
// const food4 = 'hotdog';
// const food5 = 'ramen';

// const foods = getFood(food1, food2, food3, food4, food5);
// console.log(foods);


// // function to get the sum of digits
// function sum(...numbers) {
//     let result = 0;
//     for (let number of numbers) {
//         result += number;
//     }
//     return result
// }

// let total = sum(1, 2);
// console.log(`the sum is: ${total}`);


// create a function to get an average
// function getAverage(...numbers) {
//     let result = 0;
//     for (let number of numbers) {
//         result += number;
//     }
//     return result / numbers.length;
// }

// const total = getAverage(10, 32, 60, 40);
// console.log(`The average is: ${total}`)

// we can use rest parameters to combine the strings together

// function combineString(...joined) {
//     return joined.join(" ");
// }
// const fullname = combineString("Mr.", "Banoth", "Prashanth", "Nayak", "06");
// console.log(fullname);


function generatePassword(length, includeUppercase, includelowerCase, includeNumber, includeSymbols) {
    const lowercaseChars = `abcdefghijklmnopqrstuvwxyz`;
    const uppercaseChars = `ABCDEFGHIJKLMNOPQRSTUVWXYZ`;
    const numberChars = `0123456789`;
    const symbolChars = `!@#$%^&*()_+-*`;

    let storeChars = "";
    let password = "";

    storeChars += includeUppercase ? uppercaseChars : "";
    storeChars += includelowerCase ? lowercaseChars : "";
    storeChars += includeNumber ? numberChars : "";
    storeChars += includeSymbols ? symbolChars : "";

    if (length <= 0) {
        return `(password length must be at least 1)`;
    }
    if (storeChars.length === 0) {
        return `(atleast 1 set of characters need to be selected)`;
    }
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * storeChars.length);
        password += storeChars[randomIndex];
    }
    return password;
}

const passwordLength = 12;
const includeUppercase = true;
const includelowerCase = true;
const includeNumber = true
const includeSymbols = true

const password = generatePassword(passwordLength,
    includeUppercase,
    includelowerCase,
    includeNumber,
    includeSymbols
);

console.log(`generated password: ${password}`)