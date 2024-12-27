// Gera um número aleatório entre 1 e 100
const randomNumber = Math.floor(Math.random() * 100) + 1;
console.log('Número sorteado:', randomNumber); // Para fins de depuração

// Função para verificar o palpite do usuário
function checkGuess() {
    const guess = document.getElementById('guess').value;
    const result = document.getElementById('result');

    if (guess == randomNumber) {
        result.textContent = 'Parabéns! Você acertou!';
        result.style.color = 'green';
    } else if (guess < randomNumber) {
        result.textContent = 'Tente um número maior!';
        result.style.color = 'red';
    } else {
        result.textContent = 'Tente um número menor!';
        result.style.color = 'red';
    }
}
