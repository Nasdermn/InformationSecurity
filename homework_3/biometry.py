import cv2

analysing_img = 'ox.png'

# Загрузка файлов каскадных классификаторов для определения лица, глаз и улыбки
face_cascade = cv2.CascadeClassifier('./faceparts/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./faceparts/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('./faceparts/haarcascade_smile.xml')

# Загрузка изображения
image = cv2.imread(f'./photos/{analysing_img}')

# Конвертация изображения в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Определение лица на изображении
faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

# Проход по обнаруженным лицам и наложение прямоугольника
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    # Определение глаз в области лица
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # Определение улыбки в области лица
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

# Отображение изображения с обозначенными лицами, глазами и улыбками
cv2.imshow('Detected Features', image)
cv2.waitKey(0)
cv2.destroyAllWindows()