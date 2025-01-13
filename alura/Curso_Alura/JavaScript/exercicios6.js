// Cria um array vazio
let meuArray = [];

// Adiciona três números inteiros ao array usando o método push()
meuArray.push(1);
meuArray.push(2);
meuArray.push(3);

// Exibe o array resultante
console.log("Array resultante:", meuArray);

// Cria um array vazio chamado clinica
let clinica = [];

// Simula a chegada de três animais diferentes
clinica.push("Cachorro - Rex");
clinica.push("Gato - Mia");
clinica.push("Pássaro - Pepe");

// Exibe a lista de animais na clínica
console.log("Lista de animais na clínica:", clinica);

// Remove os animais da lista um por vez
let atendido1 = clinica.shift(); // Remove o primeiro animal da lista
console.log(`${atendido1} foi atendido e removido da fila.`);
let atendido2 = clinica.shift(); // Remove o próximo animal da lista
console.log(`${atendido2} foi atendido e removido da fila.`);
let atendido3 = clinica.shift(); // Remove o último animal da lista
console.log(`${atendido3} foi atendido e removido da fila.`);

// Exibe o estado final da lista
console.log("Estado final da lista de animais na clínica:", clinica);
