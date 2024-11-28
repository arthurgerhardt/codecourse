function exibeNome(nome) {
    return nome;
}

console.log(exibeNome("Evelyn")); // Output: Alice

exibeNome("Evelyn"); // Output: Alice //

function exibeIdade(idade) {
    return idade;
}
console.log(exibeIdade(25)); // Output: 25
exibeIdade(25); // Output: 25 //

function verificarPalindromo(palavra) {
    // Remove caracteres especiais e transforma a string em minúsculas
    const palavraLimpa = palavra.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
    // Inverte a string
    const palavraInvertida = palavraLimpa.split('').reverse().join('');
    // Verifica se a string original é igual à string invertida
    return palavraLimpa === palavraInvertida;
}

// Exemplo de uso
const palavra = "A base do teto desaba";
const resultado = verificarPalindromo(palavra);
console.log(`A palavra "${palavra}" é um palíndromo: ${resultado}`);

function encontrarMaiorNumero(num1, num2, num3) {
    let maiorNumero;

    if (num1 >= num2 && num1 >= num3) {
        maiorNumero = num1;
    } else if (num2 >= num1 && num2 >= num3) {
        maiorNumero = num2;
    } else {
        maiorNumero = num3;
    }

    console.log(`O maior número entre ${num1}, ${num2}, e ${num3} é ${maiorNumero}.`);
}

// Exemplo de uso
encontrarMaiorNumero(10, 25, 17);

const calculaPotencia = (base, expoente) => {
    return Math.pow(base, expoente);
};

// Exemplo de uso
let resultado1 = calculaPotencia(2, 3);
console.log(`O resultado de 2 elevado a 3 é ${resultado1}.`);

