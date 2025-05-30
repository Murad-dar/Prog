# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

# Таблица связи многие-ко-многим для студентов и курсов
student_course = Table('student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
    Column('enrollment_date', DateTime, default=datetime.now)
)

class Teacher(Base):
    """Модель преподавателя"""
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    specialization = Column(String(100))
    
    # Связь с курсами (один преподаватель - много курсов)
    courses = relationship("Course", back_populates="teacher")
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.first_name} {self.last_name}')>"

class Student(Base):
    """Модель студента"""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    
    # Связь с курсами через промежуточную таблицу (многие-ко-многим)
    courses = relationship("Course", secondary=student_course, back_populates="students")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}')>"

class Course(Base):
    """Модель курса"""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    
    # Связи
    teacher = relationship("Teacher", back_populates="courses")
    students = relationship("Student", secondary=student_course, back_populates="courses")
    
    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"