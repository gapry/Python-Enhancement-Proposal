from __future__ import annotations

class Student:
  def __init__(self, m_name, m_id):
    self.student_name = m_name
    self.student_id = m_id

  def __str__(self):
    msg = "student = " + self.get_student_name() + "\n"
    msg += "id      = " + self.get_student_id()
    return msg

  def get_student(self, m_name, m_id) -> Student:
    return Student(m_name, m_id)

  def get_student_name(self):
    return self.student_name.capitalize()

  def get_student_id(self):
    return self.student_id

s1 = Student("sam", "s11")
s2 = Student("mary", "s12")

print(s1)
print(s2)
print(s1.get_student("john", "s13"))
