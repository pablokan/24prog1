class Musica:

    def __init__(self, nombre, albunes, reproduciones):
        self.nombre=nombre
        self.albunes= albunes
        self.reproduciones= reproduciones

    



class Bandas(Musica):

    def __init__(self, nombre, albunes, reproduciones, cantantes ):
        super().__init__(nombre, albunes, reproduciones)
        self.cantantes= cantantes
        
class Solista(Musica):
    
    def __init__(self, nombre, albunes,reproduciones, edad):
        super().__init__(nombre, albunes, reproduciones)
        self.edad =edad



class Plataforma_Web:
    lista_bandas=[]
    lista_solista=[]

    

    def __init__(self, nombre):
        self.nombre = nombre

    def Carga (self):
        bandas=[["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"]    ,["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
        ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]]
        
        solistas=[["Peter Gabriel", 10, 17319533, 70],["Jeff Beck", 3, 1023998, 76]]

        for band in bandas:
            band= Bandas(band[0],band[1],band[2],band[3])           
            
            self.lista_bandas.append(band)

        for solist in solistas:
            solist=Solista(solist[0],solist[1],solist[2],solist[3])
            self.lista_solista.append(solist)




    def TotalReproduciones(self):
        
        sumabandas= 0
        sumasolista=0
        
        for reprob in self.lista_bandas:
            sumabandas+=reprob.reproduciones
        
        for reprosol in self.lista_solista:
            sumasolista+= reprosol.reproduciones
        
        total= sumabandas + sumasolista
        print(f' total reprosucion del sitio: {sumasolista}')


    def solista_mayor(self):
        nombre_solista_mEdad= ''
        edad= -999999999
        for solinom in self.lista_solista:
            if solinom.edad> edad:
                edad=solinom.edad
                nombre_solista_mEdad = solinom.nombre
        
        print(f'el cantante mas viejo es {nombre_solista_mEdad}')

    def info_banda(self):
        for cant in self.lista_bandas:
                cant.nombre
        return cant.nombre

    def Cant_Albun ():
        pass
                
        
        

  



empresa1= Plataforma_Web('sol')
empresa1.Carga()
print(empresa1.TotalReproduciones())
print(empresa1.solista_mayor())
print(f' los nombres de los cantantes de las bandas son {empresa1.info_banda()}')






        




    

