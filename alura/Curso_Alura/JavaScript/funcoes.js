function exibeInfosEstudante(nome, nota) {
    //nome = "Marcelo";
    console.log(`O estudante ${nome} obteve a nota ${nota}`);
}

exibeInfosEstudante('Marcelo', 7);
exibeInfosEstudante('Maria', 5);
exibeInfosEstudante('João', 9);


function dividir(dividendo, divisor) {
    if (divisor !== 0) {
      return dividendo / divisor;
    } else {
      return 'favor não dividir por zero';
    }
   }
   
   const resultado = dividir(10, 5);
   console.log(resultado); // 2
   const resultadoZero = dividir(10, 0);
   console.log(resultadoZero); // 'favor não dividir por zero'

   
   function saudacao(nome) {
    return `Olá, ${nome}!`;
}

const mensagem = saudacao("Maria");
console.log(mensagem);

   
   



