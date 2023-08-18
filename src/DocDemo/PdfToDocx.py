from pdf2docx import Converter

# 指定输入的 PDF 文件路径
input_pdf = "C:/Users/lenovo/Desktop/交付实施体会.pdf"

# 指定输出的 DOCX 文件路径
output_docx = "C:/Users/lenovo/Desktop/交付实施体会.docx"

# 调用转换函数
cv = Converter(input_pdf)
cv.convert(output_docx, start=0, end=None)
cv.close()
