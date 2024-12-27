// Bem-vindo ao jogo de adivinhação em JavaScript!

const numerosecreto = 42;
let numero;
let naoacertou = true;

console.log("******************************************");
console.log("**** Bem-vindo ao jogo de adivinhação! ****");
console.log("******************************************");

// Função para pegar o input do usuário (simulação no ambiente Node.js)
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Função para perguntar ao usuário
function perguntar() {
    readline.question('Qual é o seu chute? \n', (input) => {
        numero = parseInt(input);
        console.log(`Seu chute foi: ${numero}`);
        let acertou = (numero === numerosecreto);
        if (acertou) {
            console.log("Parabéns! Você acertou!");
            console.log("Você é um bom jogador! Jogue de novo!");
            naoacertou = false;
            readline.close();
        } else {
            let maior = numero > numerosecreto;
            if (maior) {
                console.log("Seu chute foi maior que o número secreto.");
            } else {
                console.log("Seu chute foi menor que o número secreto.");
            }
            perguntar(); // Chama a função novamente para continuar o jogo
        }
    });
}

// Inicia o jogo perguntando pela primeira vez
perguntar();
