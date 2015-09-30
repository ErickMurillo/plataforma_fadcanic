import os

arreglo_mail = ['crocha09.09@gmail.com','keniaregina@gmail.com',
				'delrysimons@yahoo.com','changenowlestsdoit@gmail.com',
				'vgo1993@yahoo.es','vgonzalez@fadcanic.org.ni']

def get_file_path(intance,filename):
    return os.path.join(intance.fileDir, filename)
