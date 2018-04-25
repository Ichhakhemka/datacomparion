from itertools import izip_longest
import xlrd

rb1 = xlrd.open_workbook('C:\\Users\\ichha\\testdata1.xlsx')
rb2 = xlrd.open_workbook('C:\\Users\\ichha\\testdata2.xlsx')

sheet1 = rb1.sheet_by_index(0)
sheet2 = rb2.sheet_by_index(0)

col_names = sheet1.row_values(0)
for rownum in range(1,max(sheet1.nrows, sheet2.nrows)):

    if rownum < sheet1.nrows:
        row_rb1 = sheet1.row_values(rownum)
        row_rb2 = sheet2.row_values(rownum)

        for colnum, (c1, c2) in enumerate(izip_longest(row_rb1, row_rb2)):
            if c1 != c2:
                colname = col_names[colnum]
                print "Userid {},{} - {} != {}".format(int(row_rb1[0]), colname, c1, c2)

    else:
        print "Row {} missing".format(rownum+1)
