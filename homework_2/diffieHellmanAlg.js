// Функция Диффи-Хеллмана
function diffieHellman(privateKey, publicKey, P) {
  return Math.pow(publicKey, privateKey) % P;
}

// Функция Алгоритм Цезаря
function caesarEncrypt(message, shift) {
  return message
    .split('')
    .map((char) => {
      const code = char.charCodeAt(0);
      // Выполняем только для кириллицы
      if (char.match(/[а-яА-Я]/)) {
        let offset = 1040; // для заглавных букв
        if (code >= 1072) offset = 1072; // для строчных букв
        return String.fromCharCode(((code - offset + shift) % 32) + offset);
      }
      return char;
    })
    .join('');
}

// Функция Дешифрование алгоритма Цезаря (вставляем противоположный сдвиг)
function caesarDecrypt(encryptedMessage, shift) {
  return caesarEncrypt(encryptedMessage, 32 - shift);
}

//Дано (Вариант-11)
const P = 13; // простое число
const G = 41; // примитивный корень по модулю P

// Приватные ключи участников
const privateKeyBob = 9;
const privateKeyAlice = 7;

// Публичные ключи участников
const publicKeyBob = Math.pow(G, privateKeyBob) % P;
const publicKeyAlice = Math.pow(G, privateKeyAlice) % P;

// Вычисляем общий секрет для Боба и Алисы
const sharedSecretBob = diffieHellman(privateKeyBob, publicKeyAlice, P);
const sharedSecretAlice = diffieHellman(privateKeyAlice, publicKeyBob, P);

if (sharedSecretAlice === sharedSecretBob) {
  const sharedSecret = sharedSecretAlice;
  console.log(`Общий секретный ключ совпал и равен ${sharedSecret}`);
  // Шифрование сообщения на стороне Боба
  const messageBob = 'Алиса! Мелофон у того толстого! ГАСИ ЕГО!'; // Сообщение от Боба
  console.log('Незашифрованное сообщение от Боба:', messageBob);
  const encryptedMessageBob = caesarEncrypt(messageBob, sharedSecret);
  console.log('Зашифрованное сообщение от Боба:', encryptedMessageBob);

  // Дешифрование сообщения на стороне Алисы
  const decryptedMessageAlice = caesarDecrypt(encryptedMessageBob, sharedSecret);
  console.log('Расшифрованное сообщение у Алисы:', decryptedMessageAlice);
}
