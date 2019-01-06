#Usuario

u1 = Usuario(USU_COD = 1, USU_NOM = "Encargado")

u1.save()

u2 = Usuario(USU_COD = 2, USU_NOM = "Voluntario")

u2.save()

#Genero

g1 = Genero(GEN_COD = "M", GEN_NOM = "Macho")

g1.save()

#Vacuna

v1 = Vacuna(VAC_ID = 1, VAC_NOM = "Antirábica")

v1.save()

#Estado

e1 = Estado(EST_COD = "APR", EST_NOM = "Aprobada")

e1.save()

#Desparasitación

d1 = Desparasitacion(DES_COD = "SI", DES_NOM = "La mascota esta desparasitada")

d1.save()

#Tipo_Mas


tm1 = Tipo_Mas(TIPO_COD = "GA", TIPO_NOM = "Gato")

tm1.save()

#Adoptante

a1 = Adoptante(ADO_RUN = "15478521", ADO_USU = u2, ADO_NOM = "PEDRO", 
ADO_APELL = "Soto", ADO_EDAD = 41, ADO_FONO = 74586317, ADO_MAIL = "pedro@gmail.com",
ADO_DIR = "San Pablo 4512")

a1.save()

#Mascota

m1 = Mascota(MAS_ID = 7845, MAS_NOM = "Lupita", MAS_TIPO = tm1, MAS_GEN = g1,
MAS_DES = d1 , MAS_EDAD = 1) #MAS_VAC = ????????????)

m1.save()

#Solicitud

s1 = Solicitud(SOL_ID = 1420, SOL_RUN = a1, SOL_MAS = m1, SOL_EST = e1, 
SOL_FEC = "04/03/2015")

s1.save()




