const estudante = "Arthur";
const docente = "Raphael";
const cumprimento = "Nosso lema é ' estudar bastante '";
const citacao = `Raphael diz que o nosso lema é 'estudar.'`;
console.log(cumprimento);
console.log(citacao);
console.log(`O estudante chama ${estudante} e o docente chama ${docente}.`);

// Template strings
const senha = 'SenhaSegura123' + estudante.toUpperCase();
console.log(senha);