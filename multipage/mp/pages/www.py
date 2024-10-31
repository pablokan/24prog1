import os
archivos = os.listdir('mp/pages')
archivos = ['.' + name[:-3] for name in archivos if not name.startswith('_')]
print('imports de init:', archivos)  