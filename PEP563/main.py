#!/usr/bin/env python

from __future__ import annotations

__author__     = "Gapry"
__copyright__  = "Copyright 2020, Gapry"
__date__       = "2020/01/14"
__deprecated__ = False
__license__    = "MIT"
__maintainer__ = "Gapry"
__status__     = "PoC"
__version__    = "1.0.0"

class Student:
  def __init__(self, m_name, m_id):
    self.student_name = m_name
    self.student_id = m_id

  def __str__(self):
    return ("{0}\n{1}\n").format("student = " + self.get_student_name(),
                                 "id      = " + self.get_student_id())

  def reset(self, m_name, m_id) -> Student:
    return Student(m_name, m_id)

  def get_student_name(self):
    return self.student_name.capitalize()

  def get_student_id(self):
    return self.student_id

if __name__ == '__main__':
  sam = Student("sam", "id55")
  sky = Student("sky", "id66")
  print(sam)
  print(sky)
  print(sam.reset("john", "id5566"))
