'''
Created on 23 Feb 2014

@author: ByteBoxx
'''

#===============================================================================
# 
#===============================================================================




from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import landscape

testImagePath = "C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\testemjpg5.jpeg" 
testImagePath2 = "C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\testemjpg6.jpeg" 

c = canvas.Canvas("test.pdf", pagesize=landscape(A3))
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min135_tex.jpeg", 70.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min90_tex.jpeg", 220.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min45_tex.jpeg", 370.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\front_tex.jpeg", 520.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\45_tex.jpeg", 670.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\90_tex.jpeg", 820.08,450)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\135_tex.jpeg", 970.08,450)

c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min135.jpeg", 70.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min90.jpeg", 220.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\min45.jpeg", 370.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\front.jpeg", 520.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\45.jpeg", 670.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\90.jpeg", 820.08,75)
c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\135.jpeg", 970.08,75)



c.drawImage("C:\\Users\\ByteBoxx\\Documents\\maya\\projects\\default\\images\\CAS_logo.jpeg", 0,0)
c.setFont('Helvetica', 24, leading=None)
c.setFillColorRGB(0.2, 0.2, 0.2, 1)
c.drawString(970, 55, "20131020_Emily")
c.showPage()
c.save()


