from fpdf import FPDF
'''
P:portrait(vertical)
L:landscape(horizontal)

A4: 210x279mm

Para más Ejemplos: https://github.com/ALEX7320/guia-pdf-python
'''

def createPDF():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # TEXTO  -----

    pdf.set_font('Arial','',18)

    pdf.text(x= 60, y= 50, txt='Hola mundo 2')
    pdf.text(x= 60, y= 60, txt='Hola mundo 2')


    # IMAGEN (jpg/png) -----

    url = './src/Perfil1.png'

    pdf.image('./src/Perfil1.png', x= 20, y= 20, w = 60, h = 60)#, link = url)





    pdf.output('./src/sheet.pdf')


def run():
    createPDF()

if __name__ == '__main__':
    run()

