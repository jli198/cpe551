#lecture8Classes.py
#Kevin Ryan
#Section B
#AAI/CPE/EE 551
#Spring 2023

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee(Person):
  def compute_salary(self):
    return 60000
  
  def number_of_vacation(self):
    return 20

class Engineer(Employee):
  def compute_salary(self):
    return 100000
  
class Manager(Employee):
  def set_workers(self, people):
    self.workers = people

  def compute_salary(self):
    return 90000
  
  def number_of_vacation(self):
    return 25