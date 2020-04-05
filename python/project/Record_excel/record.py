import xlwt,xlrd

workbook = xlwt.Workbook(encoding="utf-8")
sheet1 = workbook.add_sheet("每日记录")
# xls 格式可以打开,xlsx格式save无法保存


# 操作表格

sheet1.write(0,0, "课程")
sheet1.write(0,1, "学习时长(次数)")
sheet1.write(0,2, "日期")
sheet1.write(0,3, "其他")

workbook.save(r"D:\东蒙 人工智能课程\cs learning git\python\Project\Record_excel\files\学习记录.xls")