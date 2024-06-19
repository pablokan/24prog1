from libreria.funcs import inputChoiceMenu, edad
personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-03-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,03-07-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]
def cantidadPersonasXpais(pais, listaP):
    contador = 0
    for persona in  listaP:
        #if pais in persona: # si se apellida como un pais, falla
        if pais == persona.split(',')[1]:
            contador += 1
    return contador

cantArgentos = cantidadPersonasXpais("Argentina", personas)
print(f'La cantidad de personas de Argentina es {cantArgentos}')
otroPais = inputChoiceMenu('United States/France/Norway','Ingrese otro país del que desea saber la cantidad de personas: ')
cantExtranjeros = cantidadPersonasXpais(otroPais, personas)
print(f'La cantidad de personas de {otroPais} es {cantExtranjeros}')

def edadesSegunInicial(inicial, listaP):
    for persona in listaP:
        if inicial == persona.split(',')[0].split()[1][0]:
            print(edad(persona.split(',')[2]))

edadesSegunInicial('B', personas)
