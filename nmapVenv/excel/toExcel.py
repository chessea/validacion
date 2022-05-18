import openpyxl

class ListaToExcel:
  
    @classmethod
    def datosToExcel(cls,lista):
        try:
            book =openpyxl.load_workbook('/home/fr/Documentos/validacion/nmapVenv/store/validacion.xlsx')
            sheet = book['levantamiento']
            sheet['B3']=lista[0]
            sheet['B4']=lista[1]
            sheet['B11']=lista[2]
            sheet['B17']=lista[3]
            sheet['B22']=lista[4]
            sheet['B19']=lista[5]
            sheet['B23']=lista[6]
            print('FIN ENCABEZADO')

            book.save(f'/home/fr/Documentos/validacion/nmapVenv/store/levantamiento.xlsx')
            print('FIN SH RUN') 
        except Exception as e:
            print('ERROR Al aguardar datos')               