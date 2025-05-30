# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Teacher, Student, Course

# Создание движка базы данных SQLite
engine = create_engine('sqlite:///courses.db', echo=True)

# Создание всех таблиц
Base.metadata.create_all(engine)

# Создание сессии для работы с БД
Session = sessionmaker(bind=engine)
session = Session()

def populate_database():
    """Заполнение базы данных тестовыми данными"""
    
    print("Начинаем заполнение базы данных...")
    
    # Очистка существующих данных (если есть)
    session.query(Student).delete()
    session.query(Course).delete() 
    session.query(Teacher).delete()
    session.commit()
    
    # 1. Создание преподавателей
    teachers = [
        Teacher(
            first_name="Анна", 
            last_name="Петрова", 
            email="anna.petrova@university.ru", 
            specialization="Программирование"
        ),
        Teacher(
            first_name="Михаил", 
            last_name="Иванов", 
            email="mikhail.ivanov@university.ru", 
            specialization="Математика"
        ),
        Teacher(
            first_name="Елена", 
            last_name="Сидорова", 
            email="elena.sidorova@university.ru", 
            specialization="Дизайн"
        ),
        Teacher(
            first_name="Дмитрий", 
            last_name="Козлов", 
            email="dmitry.kozlov@university.ru", 
            specialization="Веб-разработка"
        )
    ]
    
    # 2. Создание студентов
    students = [
        Student(
            first_name="Алексей", 
            last_name="Смирнов", 
            email="alexey.smirnov@student.ru", 
            phone="+7-900-123-45-67"
        ),
        Student(
            first_name="Мария", 
            last_name="Васильева", 
            email="maria.vasileva@student.ru", 
            phone="+7-900-234-56-78"
        ),
        Student(
            first_name="Игорь", 
            last_name="Николаев", 
            email="igor.nikolaev@student.ru", 
            phone="+7-900-345-67-89"
        ),
        Student(
            first_name="Ольга", 
            last_name="Федорова", 
            email="olga.fedorova@student.ru", 
            phone="+7-900-456-78-90"
        ),
        Student(
            first_name="Андрей", 
            last_name="Морозов", 
            email="andrey.morozov@student.ru", 
            phone="+7-900-567-89-01"
        ),
        Student(
            first_name="Светлана", 
            last_name="Попова", 
            email="svetlana.popova@student.ru", 
            phone="+7-900-678-90-12"
        )
    ]
    
    # Добавляем преподавателей и студентов в сессию
    session.add_all(teachers)
    session.add_all(students)
    session.commit()  # Сохраняем в БД
    
    print("Преподаватели и студенты добавлены.")
    
    # 3. Создание курсов (после добавления преподавателей)
    courses = [
        Course(
            title="Python для начинающих", 
            description="Основы программирования на Python", 
            teacher_id=1  # Анна Петрова
        ),
        Course(
            title="Веб-разработка с Django", 
            description="Создание веб-приложений на Django", 
            teacher_id=1  # Анна Петрова
        ),
        Course(
            title="Высшая математика", 
            description="Курс высшей математики для программистов", 
            teacher_id=2  # Михаил Иванов
        ),
        Course(
            title="Дискретная математика", 
            description="Основы дискретной математики", 
            teacher_id=2  # Михаил Иванов
        ),
        Course(
            title="UI/UX Дизайн", 
            description="Проектирование пользовательских интерфейсов", 
            teacher_id=3  # Елена Сидорова
        ),
        Course(
            title="JavaScript и React", 
            description="Современная фронтенд разработка", 
            teacher_id=4  # Дмитрий Козлов
        )
    ]
    
    session.add_all(courses)
    session.commit()
    
    print("Курсы добавлены.")
    
    # 4. Записываем студентов на курсы
    # Алексей - Python и Django
    students[0].courses.extend([courses[0], courses[1]])
    
    # Мария - Python, Математика и Дизайн
    students[1].courses.extend([courses[0], courses[2], courses[4]])
    
    # Игорь - обе математики и JavaScript
    students[2].courses.extend([courses[2], courses[3], courses[5]])
    
    # Ольга - Дизайн и JavaScript
    students[3].courses.extend([courses[4], courses[5]])
    
    # Андрей - Python и JavaScript
    students[4].courses.extend([courses[0], courses[5]])
    
    # Светлана - Дизайн и математика
    students[5].courses.extend([courses[4], courses[2]])
    
    session.commit()
    
    print("Студенты записаны на курсы.")
    print("База данных успешно заполнена!")

if __name__ == "__main__":
    populate_database()