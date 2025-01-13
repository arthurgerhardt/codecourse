const numero_secreto = 42;
let numero;
let naoacertou = true;

while (naoacertou) {
  numero = parseInt(prompt("Digite um número:"));
  console.log("Você digitou: " + numero);
  let acertou = (numero_secreto == numero);
  let maior = (numero_secreto < numero);

  if (acertou) {
    alert("Parabéns, você acertou!");
    naoacertou = false;
  } else if (maior) {
    alert("O número secreto é maior!");
  } else {
    alert("O número secreto é maior!");
  }
}