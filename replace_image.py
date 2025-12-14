#!/usr/bin/env python3
import re

# Читаем файл
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Заменяем все ссылки на изображения Urban Minimal
old_url = 'https://images.unsplash.com/photo-1519812061168-5b6b5e8a888c?q=80&w=800&auto=format&fit=crop'
new_url = 'AdobeStock_416681212_unisex.jpeg'

# Выполняем замену
new_content = content.replace(old_url, new_url)

# Записываем файл
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Заменено {content.count(old_url)} изображений на {new_url}")
