let estudante;
if (1 > 0) {
    estudante = 'Arthur';
    console.log(estudante);
    console.log("O nome do estudante é " + estudante);
}

console.log(estudante);
console.log("O nome do estudante é " + estudante);

let nome = "Ana";
if (1 > 0) {
    console.log(nome); // ‘Ana’
  }
  
  console.log(nome); // ‘Ana’
  
  function cumprimentar() {
    const nome = 'Camila'; // variável local
    const cumprimento = 'Olá'; // variável local
    console.log(`${cumprimento}, ${nome}!`); // “Olá, Camila!”
  }
  
  // as variáveis não podem ser acessada de fora da função
  console.log(`${cumprimento}, ${nome}!`); // Dará erro de “not defined” no console
  