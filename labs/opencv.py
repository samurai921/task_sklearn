import cv2
import numpy as np
import os

# Получение текущей директории
current_dir = os.getcwd()

# Путь к изображению
image_path = os.path.join(current_dir, 'input_image.png')

# Загрузка изображения
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Параметры для соляризации
solarize_threshold = 150

# Параметры для логарифмического контрастирования
log_alpha = 1.0

# Соляризация
inverted_image = cv2.bitwise_not(image)
_, thresholded_image = cv2.threshold(image, solarize_threshold, 255, cv2.THRESH_BINARY)
solarized_image = cv2.bitwise_and(image, thresholded_image)

# Логарифмическое контрастирование
log_transformed = np.uint8(np.log1p(image) * log_alpha)

# Путь для сохранения результатов
output_dir = os.path.join(current_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# Сохранение результатов
cv2.imwrite(os.path.join(output_dir, 'solarized_image.jpg'), solarized_image)
cv2.imwrite(os.path.join(output_dir, 'log_contrast_image.jpg'), log_transformed)
