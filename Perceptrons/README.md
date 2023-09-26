<h1>Perceptrons</h1>
<p>Um perceptron é o bloco de construção básico de uma RNA. Ele recebe várias entradas e produz uma saída com base em pesos atribuídos a essas entradas e um limite. Pode ser usado para tomar decisões simples.</p>
<h2>A seguir podemos conferir um exemplo semples para demonstrar como um perceptron funciona</h2>
<p>Para um melhor entendimento, vamos entender cada dado neste arquivo:</p>
<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Valor</th>
    </tr>
    <tr>
      <th>W</th>
      <td>Peso 1</td>
    </tr>
    <tr>
      <th>W2</th>
      <td>Peso 2 e 3</td>
    </tr>
    <tr>
      <th>Baias</th>
      <td>Valor BAIAS</td>
    </tr>
    <tr>
      <th>Limit</th>
      <td>Valor LIMIT</td>
    </tr>
    <tr>
      <th>x1</th>
      <td>Input 1</td>
    </tr>
    <tr>
      <th>x2</th>
      <td>Input 2</td>
    </tr>
    <tr>
      <th>x2</th>
      <td>Input 3</td>
    </tr>
  </thead>
</table>
<img src="./assets/codigoVsCode.png" alt="Imagem do codigo">
<p> Dado a narrativa apresentada, podemos ter algumas resoluções, a primeira pergunta tem o peso 6, já a segunda e terceira tem peso 2, como definimos o Limit em 5, podemos ter apenas duas respostas:\n 1º- se a primeira resposta for SIM, indepedente das outras respostas o retorno será "Você deve ir ao evento".\n 2º - se a primeira resposta for NAO, indepedente das outras respostas o retorno será "Você não deve ir ao evento" </p>
