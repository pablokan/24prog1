personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

masReciente = 0
nombreMasJoven = ''
for persona in personas:
    if "Europe" in persona:
        fN = int(persona[-4:] + persona[-7:-5] + persona[-10:-8])
        #print(fN)
        if fN > masReciente:
            masReciente = fN
            nombreMasJoven = persona[:persona.find(' ')]
print(nombreMasJoven)

