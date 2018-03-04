# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     005-static_class_method
   Description :   url = "https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner"
   Author :       pinglin
   date：          18-3-4
-------------------------------------------------
"""
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return "{0}-{1}-{2}".format(self.month, self.day, self.year)

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date1 = Date(4, 3, 2018)
date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print(date1.display())
print(date2.display())
print(is_date)