import os

arreglo_mail = ['crocha09.09@gmail.com','pablo.ismael90@gmail.com',
				'erickmurillo22@gmail.com','mcu.caps@gmail.com']

def get_file_path(intance,filename):
    return os.path.join(intance.fileDir, filename)
