from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

connect = create_engine("mysql+pymysql://root:123456@localhost:3306/practice?charset=utf8",
                        echo=False)  # 连接数据库，echo=True =>把所有的信息都打印出来

Base = declarative_base()

student_m2m_class = Table("student_m2m_class", Base.metadata,
                          Column("id", Integer, primary_key=True, autoincrement=True),
                          Column("student_id", Integer, ForeignKey("student.id")),
                          Column("class_id", Integer, ForeignKey("class.id")))

teacher_m2m_class = Table("teacher_m2m_class", Base.metadata,
                          Column("id", Integer, primary_key=True, autoincrement=True),
                          Column("teacher_id", Integer, ForeignKey("teacher.id")),
                          Column("class_id", Integer, ForeignKey("class.id")))


class CourseM2MClass(Base):
    __tablename__ = "course_m2m_class"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.id"))
    class_id = Column(Integer, ForeignKey("class.id"))
    course = relationship("CourseTable", backref="course_m2m_class")
    classes = relationship("ClassTable", backref="course_m2m_class")

    def __repr__(self):
        return "course_id: %s, class_id: %s" % (self.course_id, self.class_id)


class StudentTable(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(32), nullable=False)
    QQ = Column(String(32), nullable=False, unique=True)

    def __repr__(self):
        return "student id: %s  student name: %s  QQ: %s" % (self.id, self.student_name, self.QQ)


class TeacherTable(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(32), nullable=False)

    classes = relationship("ClassTable", secondary=teacher_m2m_class, backref="teacher")

    def __repr__(self):
        return "teacher name: %s" % self.teacher_name


class ClassTable(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(32), nullable=False)
    class_course = Column(String(32), nullable=False)

    students = relationship("StudentTable", secondary=student_m2m_class, backref="my_class")

    def __repr__(self):
        return "class name: %s   class_course: %s" % (self.class_name, self.class_course)


class CourseTable(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(32), nullable=False)

    def __repr__(self):
        return "course name: %s" % self.course_name


class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_m2m_class_id = Column(Integer, ForeignKey("course_m2m_class.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    study_status = Column(String(32), nullable=False, default="YES")
    homework_status = Column(String(32), nullable=False, default="NO")
    score = Column(Integer, nullable=False, default=0)

    course_m2m_class = relationship("CourseM2MClass", backref="my_study_record")
    student = relationship("StudentTable", backref="my_study_record")

    def __repr__(self):
        return " course_m2m_class_id: %s  student_id :%s  status:%s  score: %s" \
               % (self.course_m2m_class_id, self.student_id, self.study_status, self.score)


#Base.metadata.create_all(connect)  # 创建学生表和学生记录表，在第一次创建后注释


session_class = sessionmaker(connect)  # 创建与数据库的会话session class ,这里返回给session的是个class,不是实例
session = session_class()