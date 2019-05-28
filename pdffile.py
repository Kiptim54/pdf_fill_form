from fdfgen import forge_fdf
import os


name="Jenga Tech Solutions" 
telephone='0719-656'

fields = [('name', name),('telephone',telephone)]
fdf = forge_fdf("",fields,[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()


os.system('pdftk brenda.pdf fill_form data.fdf output output.pdf flatten')
