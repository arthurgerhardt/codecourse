let frase = "Estudando JavaScript no curso da Alura."
console.log(frase.includes("JavaScript")); // Retorna true
console.log(frase.length); // Retorna 41)
console.log(frase.toUpperCase()); // Retorna "ESTUDANDO JAVASCRIPT NO CURSO DA ALURA."

let numero1 = null;
let numero2;
console.log(numero1); // Retorna null
console.log(numero2); // Retorna undefined

let numero3 = 4;
let texto1 = "Curso da Alura";
let verdadeiro = true;
console.log(`O número é ${numero3}, o texto é ${texto1} e o valor booleano é ${verdadeiro}.`); // Retorna "O número é 4"

let numero4 = 10;
let numero5 = '10';
String(10); // Retorna '10'
Number('10'); // Retorna 10)
console.log(numero4, numero5); // Retorna 10 10

let texto2 = "Estudando JavaScript";
console.log(texto2.toLowerCase()); // Retorna "estudando javascript"
console.log(texto2.toUpperCase()); // Retorna "ESTUDANDO JAVASCRIPT"
console.log(texto2.charAt(0)); // Retorna "E"
console.log(texto2.charAt(10)); // Retorna "" (vazio)