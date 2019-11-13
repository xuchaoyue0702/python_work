#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xlrd


class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = '../config/case.xlsx'
        if i is None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheets(i)

    def get_excel(self):
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self, i):
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        data = self.data.cell(row, cell).value
        return data
