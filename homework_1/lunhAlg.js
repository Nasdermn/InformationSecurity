const trueNumber = 5062821234567892;
const falseNumber = '5062 8217 3456 7892';
const badNumber = 123;

function lunhAlg(cardNumber) {
  // Удаляем любые пробельные символы из строки
  const trimmedInput = cardNumber.toString().replace(/\s/g, '');

  // Проверяем длину строки
  if (trimmedInput.length !== 16) {
    return false;
  }

  // Преобразуем строку в массив чисел
  const arr = trimmedInput.split('').map(Number);

  // Проходимся по числам, начиная с конца
  for (let i = arr.length - 2; i >= 0; i -= 2) {
    let doubled = arr[i] * 2;
    // Если результат удвоения больше 9, вычитаем 9
    if (doubled > 9) {
      doubled -= 9;
    }
    arr[i] = doubled;
  }

  // Суммируем все числа
  const sum = arr.reduce((acc, curr) => acc + curr, 0);

  // Если сумма делится на 10 без остатка, номер корректен
  return sum % 10 === 0;
}

console.log(lunhAlg(trueNumber));
console.log(lunhAlg(falseNumber));
console.log(lunhAlg(badNumber));
