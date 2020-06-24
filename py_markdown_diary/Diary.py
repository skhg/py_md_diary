#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
import calendar
import os


class Diary(object):

    @staticmethod
    def validate_month(month_str):
        try:
            return datetime.strptime(month_str, '%Y-%m')
        except ValueError:
            print('Error: \'' + month_str + '\' is not a valid YYYY-MM year/month combination')
            exit()

    @staticmethod
    def validate_year(year_str):
        try:
            return datetime.strptime(year_str, '%Y')
        except ValueError:
            print('Error: \'' + year_str + '\' is not a valid YYYY year')
            exit()

    @staticmethod
    def write_month_file(month, filename):
        days_in_month = calendar.monthrange(month.year, month.month)[1]

        with open(filename, 'w') as open_file:
            open_file.writelines('# ' + month.strftime('%B') + '\n')
            open_file.writelines('\n')

            current_week = 0

            for d in range(0, days_in_month):
                todays_date = month + timedelta(days=d)

                temp_week = int(todays_date.strftime('%W')) + 1

                if current_week != temp_week:
                    current_week = temp_week
                    open_file.writelines('\n')
                    open_file.writelines('\n')
                    open_file.writelines('## Week ' + str(current_week) + '\n')
                    open_file.writelines('\n')

                day_of_week = int(todays_date.strftime('%w'))

                if day_of_week != 0 and day_of_week != 6:
                    open_file.writelines('### ' + todays_date.strftime('%a') + ' ' + todays_date.strftime('%-d') + '\n')
                    open_file.writelines('\n')
                    open_file.writelines('\n')

    @staticmethod
    def create_month_file(month):
        filename = str(month.strftime('%m')) + ' ' + str(month.strftime('%B')) + '.md'

        if not Diary.file_exists(filename):
            Diary.write_month_file(month, filename)

    @staticmethod
    def create_year_files(year):
        for m in range(1, 13):
            Diary.create_month_file(date(year.year, m, 1))

    @staticmethod
    def file_exists(filename):
        if os.path.exists(filename):
            print('Note: Diary \'' + filename + '\' already exists. Will not be modified.')
            return True

        return False
