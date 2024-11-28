let deposito = 10000;
let saque = 100;
let operacao;
operacao = deposito - saque;
console.log(operacao);

let numero = 10; // Você pode alterar este valor para qualquer número
let resultado = (numero % 2 === 0) ? "Par" : "Ímpar";
console.log(`O número ${numero} é ${resultado}.`);

let usuarioLogado = true; // Simula se o usuário está logado
let permissaoAdmin = true; // Simula se o usuário tem permissão de administrador

if (usuarioLogado && permissaoAdmin) {
    console.log("Acesso permitido: O usuário está logado e tem permissão de administrador.");
} else {
    console.log("Acesso negado: O usuário não está logado ou não tem permissão de administrador.");
}

let verdadeiro = true;
let falso = false;

console.log("OR lógico (||):", verdadeiro || falso); // Saída: true

let idadeMinima = 18;
let idadeUsuario = 17;

if (idadeUsuario >= idadeMinima) {
    console.log("Acesso permitido");
} else {
    console.log("Acesso negado");
}

