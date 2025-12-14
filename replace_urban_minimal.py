#!/usr/bin/env python3
import re

# Читаем файл
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Заменяем только изображения с alt="Urban Minimal"
old_pattern = 'src="https://images.unsplash.com/photo-1519812061168-5b6b5e8a888c?q=80&w=800&auto=format&fit=crop" alt="Urban Minimal"'
new_pattern = 'src="AdobeStock_416681212_unisex.jpeg" alt="Urban Minimal"'

# Выполняем замену
new_content = content.replace(old_pattern, new_pattern)

# Записываем файл
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Изображения Urban Minimal успешно заменены!")
