const notaPrimeiroBi = 8;
const notaSegundoBi = 6.3;
const notaTerceiroBi = -2;
const notaQuartoBi = Number.parseInt('5');
const media = (notaPrimeiroBi + notaSegundoBi + notaTerceiroBi + notaQuartoBi) / 4;
console.log(media.toFixed(2));

console.log(5 * '5');

const numero = 10;
const nome = 'Ana';

Number.isNaN(numero) // false
Number.isNaN(nome) // false
Number.isNaN(NaN) // true

isNaN(10) // false
isNaN(nome) // true
isNaN(NaN) // true
