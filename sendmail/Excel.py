#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
def __getWorkbook__():
    return xlwt.Workbook()
def __writeExcel__(restults,sheet):
    for row in range(len(restults)):
        for col in range(len(restults[row])):
           #sheet.write(row,col,restults[row][col])
            sheet.write(row,col,restults[row][col])
    return 
    
