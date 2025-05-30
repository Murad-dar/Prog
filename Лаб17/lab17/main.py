# main.py
"""
Лабораторная работа №17: SQLAlchemy ORM
Тема: Система управления курсами

Этот файл запускает всю программу:
1. Создает и заполняет базу данных
2. Выполняет запросы к базе данных
3. Показывает результаты

Автор: [Ваше имя]
Группа: [Ваша группа]
"""

import os
from database import populate_database
from queries import run_all_queries

def main():
    """Главная функция программы"""
    
    print("🎓 ЛАБОРАТОРНАЯ РАБОТА №17: SQLAlchemy ORM")
    print("📚 Тема: Система управления курсами")
    print("="*60)
    
    # Проверяем, существует ли база данных
    db_exists = os.path.exists('courses.db')
    
    if db_exists:
        print("📁 База данных найдена.")
        choice = input("Пересоздать базу данных? (y/n): ").lower().strip()
        if choice in ['y', 'yes', 'да', 'д']:
            print("\n🔄 Пересоздаем базу данных...")
            populate_database()
        else:
            print("\n✅ Используем существующую базу данных.")
    else:
        print("\n🆕 База данных не найдена. Создаем новую...")
        populate_database()
    
    print("\n" + "="*60)
    print("🔍 ВЫПОЛНЕНИЕ ЗАПРОСОВ К БАЗЕ ДАННЫХ")
    print("="*60)
    
    # Выполняем все запросы
    run_all_queries()
    
    print("\n✨ Программа завершена успешно!")
    print("📄 Файл базы данных: courses.db")

def demo_individual_queries():
    """Демонстрация отдельных запросов (для отладки)"""
    from queries import (
        query_1_all_students_and_courses,
        query_2_teachers_and_courses,
        query_3_popular_courses
    )
    
    print("ДЕМО: Выполнение отдельных запросов")
    print("-" * 40)
    
    query_1_all_students_and_courses()
    query_2_teachers_and_courses()
    query_3_popular_courses()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Ошибка выполнения: {e}")
        print("Проверьте правильность установки SQLAlchemy:")
        print("pip install sqlalchemy")
    
    # Для демонстрации можно раскомментировать:
    # demo_individual_queries()