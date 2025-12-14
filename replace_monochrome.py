#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def replace_monochrome_classic():
    """Заменяет все упоминания 'Monochrome Classic' на 'Only for Men' в index.html"""
    
    file_path = 'index.html'
    
    try:
        # Читаем файл
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Подсчитываем количество замен
        original_count = content.count('Monochrome Classic')
        print(f"Найдено упоминаний 'Monochrome Classic': {original_count}")
        
        # Выполняем замену
        updated_content = content.replace('Monochrome Classic', 'Only for Men')
        
        # Проверяем что замена прошла успешно
        new_count = updated_content.count('Monochrome Classic')
        if new_count > 0:
            print(f"ОШИБКА: После замены осталось {new_count} упоминаний 'Monochrome Classic'")
            return False
            
        # Записываем обновленный файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
            
        print(f"Успешно заменено {original_count} упоминаний на 'Only for Men'")
        print("Файл index.html обновлен")
        return True
        
    except FileNotFoundError:
        print(f"ОШИБКА: Файл {file_path} не найден")
        return False
    except Exception as e:
        print(f"ОШИБКА при обработке файла: {e}")
        return False

if __name__ == "__main__":
    print("Замена 'Monochrome Classic' на 'Only for Men'...")
    success = replace_monochrome_classic()
    if success:
        print("✅ Задача выполнена успешно!")
    else:
        print("❌ Произошла ошибка при выполнении задачи")
