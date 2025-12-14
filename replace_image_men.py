#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def replace_only_men_images():
    # Читаем файл
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Заменяем URL в каталоге
    content = content.replace(
        'src="https://images.unsplash.com/photo-1506368223429-bfa09b7c0ec2?q=80&w=800&auto=format&fit=crop" alt="Only for Men" class="product-image"',
        'src="only men.png" alt="Only for Men" class="product-image"'
    )

    # Заменяем URL в превью
    content = content.replace(
        'src="https://images.unsplash.com/photo-1506368223429-bfa09b7c0ec2?q=80&w=800&auto=format&fit=crop" alt="Only for Men" class="preview-image"',
        'src="only men.png" alt="Only for Men" class="preview-image"'
    )

    # Сохраняем файл
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Замены выполнены успешно!')
    return True

if __name__ == "__main__":
    replace_only_men_images()
