# queries.py
from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from models import Teacher, Student, Course, student_course
from database import engine

# Создаем сессию для запросов
Session = sessionmaker(bind=engine)
session = Session()

def query_1_all_students_and_courses():
    """Запрос 1: Показать всех студентов и их курсы"""
    print("=== СТУДЕНТЫ И ИХ КУРСЫ ===")
    
    students = session.query(Student).all()
    
    for student in students:
        print(f"\n{student.first_name} {student.last_name} ({student.email})")
        if student.courses:
            for course in student.courses:
                print(f"  - {course.title}")
        else:
            print("  - Не записан ни на один курс")

def query_2_teachers_and_courses():
    """Запрос 2: Показать преподавателей и количество их курсов"""
    print("\n=== ПРЕПОДАВАТЕЛИ И КОЛИЧЕСТВО КУРСОВ ===")
    
    # Запрос с группировкой и подсчетом
    teachers_with_count = session.query(
        Teacher.first_name,
        Teacher.last_name,
        Teacher.specialization,
        func.count(Course.id).label('course_count')
    ).join(Course).group_by(Teacher.id).all()
    
    for teacher in teachers_with_count:
        print(f"{teacher.first_name} {teacher.last_name} ({teacher.specialization}) - {teacher.course_count} курс(ов)")

def query_3_popular_courses():
    """Запрос 3: Самые популярные курсы (по количеству студентов)"""
    print("\n=== ПОПУЛЯРНЫЕ КУРСЫ ===")
    
    # Запрос с подсчетом студентов на каждом курсе
    popular_courses = session.query(
        Course.title,
        func.count(student_course.c.student_id).label('student_count')
    ).join(student_course).group_by(Course.id).order_by(desc('student_count')).all()
    
    for course in popular_courses:
        print(f"{course.title} - {course.student_count} студент(ов)")

def query_4_students_by_course():
    """Запрос 4: Показать студентов конкретного курса"""
    print("\n=== СТУДЕНТЫ КУРСА 'Python для начинающих' ===")
    
    # Находим курс Python
    python_course = session.query(Course).filter(
        Course.title == "Python для начинающих"
    ).first()
    
    if python_course:
        print(f"Курс: {python_course.title}")
        print(f"Преподаватель: {python_course.teacher.first_name} {python_course.teacher.last_name}")
        print("Студенты:")
        for student in python_course.students:
            print(f"  - {student.first_name} {student.last_name} ({student.email})")
    else:
        print("Курс не найден")

def query_5_teacher_workload():
    """Запрос 5: Нагрузка преподавателей (общее количество студентов)"""
    print("\n=== НАГРУЗКА ПРЕПОДАВАТЕЛЕЙ ===")
    
    # Подсчитываем общее количество студентов у каждого преподавателя
    workload = session.query(
        Teacher.first_name,
        Teacher.last_name,
        func.count(student_course.c.student_id).label('total_students')
    ).join(Course).join(student_course).group_by(Teacher.id).order_by(desc('total_students')).all()
    
    for teacher in workload:
        print(f"{teacher.first_name} {teacher.last_name} - {teacher.total_students} студент(ов)")

def query_6_courses_without_students():
    """Запрос 6: Курсы без студентов"""
    print("\n=== КУРСЫ БЕЗ СТУДЕНТОВ ===")
    
    # Находим курсы, на которые никто не записан
    empty_courses = session.query(Course).filter(
        ~Course.students.any()
    ).all()
    
    if empty_courses:
        for course in empty_courses:
            print(f"- {course.title} (преподаватель: {course.teacher.first_name} {course.teacher.last_name})")
    else:
        print("Все курсы имеют записавшихся студентов")

def query_7_students_multiple_courses():
    """Запрос 7: Студенты, записанные на несколько курсов"""
    print("\n=== СТУДЕНТЫ НА НЕСКОЛЬКИХ КУРСАХ ===")
    
    # Студенты с количеством курсов больше 1
    active_students = session.query(
        Student.first_name,
        Student.last_name,
        func.count(student_course.c.course_id).label('course_count')
    ).join(student_course).group_by(Student.id).having(
        func.count(student_course.c.course_id) > 1
    ).order_by(desc('course_count')).all()
    
    for student in active_students:
        print(f"{student.first_name} {student.last_name} - {student.course_count} курс(ов)")

def query_8_detailed_course_info():
    """Запрос 8: Подробная информация о каждом курсе"""
    print("\n=== ПОДРОБНАЯ ИНФОРМАЦИЯ О КУРСАХ ===")
    
    courses = session.query(Course).all()
    
    for course in courses:
        print(f"\n📚 {course.title}")
        print(f"   Описание: {course.description}")
        print(f"   Преподаватель: {course.teacher.first_name} {course.teacher.last_name}")
        print(f"   Количество студентов: {len(course.students)}")
        if course.students:
            print("   Студенты:")
            for student in course.students:
                print(f"     - {student.first_name} {student.last_name}")

def query_9_teachers_by_specialization():
    """Запрос 9: Преподаватели по специализации"""
    print("\n=== ПРЕПОДАВАТЕЛИ ПО СПЕЦИАЛИЗАЦИЯМ ===")
    
    # Группируем преподавателей по специализации
    specializations = session.query(Teacher.specialization).distinct().all()
    
    for spec in specializations:
        print(f"\n{spec[0]}:")
        teachers = session.query(Teacher).filter(
            Teacher.specialization == spec[0]
        ).all()
        
        for teacher in teachers:
            course_count = len(teacher.courses)
            print(f"  - {teacher.first_name} {teacher.last_name} ({course_count} курс(ов))")

def run_all_queries():
    """Запуск всех запросов по порядку"""
    print("="*60)
    print("ВЫПОЛНЕНИЕ ЗАПРОСОВ К БАЗЕ ДАННЫХ")
    print("="*60)
    
    query_1_all_students_and_courses()
    query_2_teachers_and_courses()
    query_3_popular_courses()
    query_4_students_by_course()
    query_5_teacher_workload()
    query_6_courses_without_students()
    query_7_students_multiple_courses()
    query_8_detailed_course_info()
    query_9_teachers_by_specialization()
    
    print("\n" + "="*60)
    print("ВСЕ ЗАПРОСЫ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("="*60)

if __name__ == "__main__":
    run_all_queries()