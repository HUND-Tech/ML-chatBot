
#--------------------------------------------  RAMAS PRINCIPALES --------------------------------------------#
def rama_abstracto():
    r = pedir_si_no("Q2: ¿Es un animal?")
    if r == "s":
        #animales()
        return
    r = pedir_si_no("Q3: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q4: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q5: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_seres_vivos():
    r = pedir_si_no("Q3: ¿Es un animal?")
    if r == "s":
        animales()
        return
    r = pedir_si_no("Q4: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q5: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q6: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_lugares():
    r = pedir_si_no("Q4: ¿Es un animal?")
    if r == "s":
        #animales()
        return
    r = pedir_si_no("Q5: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q6: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q7: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_persona():
    r = pedir_si_no("Q5: ¿Es un animal?")
    if r == "s":
        #animales()
        return
    r = pedir_si_no("Q6: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q7: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q8: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_fenomeno():
    r = pedir_si_no("Q6: ¿Es un animal?")
    if r == "s":
        #animales()
        return
    r = pedir_si_no("Q7: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q8: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q9: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_objeto():
    r = pedir_si_no("Q7: ¿Es un animal?")
    if r == "s":
        #animales()
        return
    r = pedir_si_no("Q8: ¿Es una planta?")
    if r == "s":
        # plantas()
        return
    r = pedir_si_no("Q9: ¿Es un hongo?")
    if r == "s":
        # hongo()
        return
    r = pedir_si_no("Q10: ¿Es un microorganismo?")
    if r == "s":
        # microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")




#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#




#------------------------------------------- SUB-RAMAS PRINCIPALES ------------------------------------------#

def animales(): #Q3
    r = pedir_si_no("Q4: ¿Es doméstico (vive normalmente con humanos)?")
    if r == "s":

        r = pedir_si_no("Q5: ¿Es un mamífero?")
        if r == "s":
            r = pedir_si_no("Q6: ¿Es pequeño (menos de 1 m de longitud, ej.raton)?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Hace chillidos agudos?")
                if r == "s":
                    print("hamster, raton")
                else:
                    print("conejo")
            else:
                r = pedir_si_no("Q7: ¿Ladra o maúlla?")
                if r == "s":

                    print("perro/gato")
                else:
                    r = pedir_si_no("Q8: ¿Es de granja lechera o de pastoreo típico?")
                    if r == "s":
                        r=pedir_si_no("Q9: ¿Tiene lana?")
                        if r == "s":
                            print("oveja")
                        else:
                            print("vaca/cabra")
                    else:
                        r=pedir_si_no("Q9: ¿Relincha?")
                        if r == "s":
                            print("caballo")
                        else:
                            print("cerdo")
            return

        r = pedir_si_no("Q6: ¿Tiene plumas (es un ave doméstica)?")
        if r == "s":
            r = pedir_si_no("Q7: ¿Canta o arrulla?")  # canario, paloma, periquito
            if r == "s":
                print("Ave pequeña doméstica (canario, periquito, paloma).")
            else:
                r = pedir_si_no("Q8: ¿Hace cacareo o graznido?")  # gallina, pato, ganso
                if r == "s":
                    print("Ave doméstica grande (gallina, pato, ganso).")
                else:
                    print("Ave doméstica poco comun.")
            return

        r = pedir_si_no("¿Vive principalmente en agua?")
        if r == "s":
            r = pedir_si_no("¿Es pequeño y ornamental?")
            if r == "s":
                print("Pez ornamental doméstico (goldfish, guppy, betta).")
            else:
                print("Pez doméstico o acuático poco comun.")
            return

        r = pedir_si_no("¿Es un reptil sin caparazón")
        if r == "s":
            print("Reptil doméstico (gecko, iguana, otros pequeños reptiles).")
            return

        r = pedir_si_no("¿Es un reptil con caparazón (tortuga terrestre o acuática)?")
        if r == "s":
            print("Clasificación: Tortuga doméstica.")
            return

        r = pedir_si_no("¿Es un anfibio?")
        if r == "s":
            print("Anfibio doméstico (rana de terrario).")
            return

        r = pedir_si_no("¿Es una tarántula u otro invertebrado exótico doméstico?")
        if r == "s":
            print("Invertebrado doméstico (tarántula, escorpión, insecto exótico).")
            return
        print("No se pudo ubicar con las preguntas.")



    else: #salvajes-----------------------------------------------------
        r = pedir_si_no("Q1: ¿Es un mamífero?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Es carnívoro?")
            if r == "s":
                r = pedir_si_no("Q3: ¿Es grande (ej. león, tigre, oso)?")
                if r == "s":
                    print("Identificado: Mamífero carnívoro grande (león, tigre, oso, lobo, etc.)")
                else:
                    print("Identificado: Mamífero carnívoro pequeño/mediano (zorro, lince, hurón, etc.)")
            else:
                r = pedir_si_no("Q3: ¿Es herbívoro?")
                if r == "s":
                    r = pedir_si_no("Q4: ¿Es muy grande (elefante, rinoceronte, jirafa)?")
                    if r == "s":
                        print("Identificado: Mamífero herbívoro grande")
                    else:
                        print("Identificado: Mamífero herbívoro mediano (ciervo, cebra, caballo salvaje, etc.)")
                else:
                    print("Identificado: Mamífero omnívoro (mapache, cerdo salvaje, oso omnívoro, etc.)")
            return

        #  Aves salvajes
        r = pedir_si_no("Q1: ¿Es un ave?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Es rapaz (caza otros animales)?")
            if r == "s":
                print("Identificado: Ave rapaz (águila, halcón, búho, etc.)")
            else:
                r = pedir_si_no("Q3: ¿Vive principalmente en agua?")
                if r == "s":
                    print("Identificado: Ave acuática salvaje (pato, cisne, pingüino, etc.)")
                else:
                    print("Identificado: Ave terrestre o migratoria (paloma salvaje, gaviota, colibrí, etc.)")
            return

        #  Reptiles salvajes
        r = pedir_si_no("Q1: ¿Es un reptil?")
        if r == "s":
            r2 = pedir_si_no("Q2: ¿Tiene caparazón?")
            if r2 == "s":
                print("Identificado: Tortuga salvaje")
            else:
                r3 = pedir_si_no("Q3: ¿Es venenoso?")
                if r3 == "s":
                    print("Identificado: Serpiente venenosa u otro reptil peligroso")
                else:
                    print("Identificado: Reptil no venenoso (iguana, lagarto, etc.)")
            return

        # Anfibios salvajes
        r = pedir_si_no("Q1: ¿Es un anfibio?")
        if r == "s":
            r2 = pedir_si_no("Q2: ¿Vive principalmente en agua?")
            if r2 == "s":
                print("Identificado: Anfibio acuático (ranas, salamandras, tritones, etc.)")
            else:
                print("Identificado: Anfibio terrestre (sapos, algunas ranas, etc.)")
            return

        # 5️⃣ Peces salvajes
        r = pedir_si_no("Q1: ¿Es un pez?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Es de agua salada?")
            if r == "s":
                print("Identificado: Pez de mar (atún, tiburón, pez loro, etc.)")
            else:
                print("Identificado: Pez de agua dulce (trucha, carpa, pez gato, etc.)")
            return

        # 6️⃣ Invertebrados salvajes
        r = pedir_si_no("Q1: ¿Es un invertebrado (araña, insecto, molusco, etc.)?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Es artrópodo (insecto, araña, cangrejo)?")
            if r == "s":
                r = pedir_si_no("Q3: ¿Es venenoso?")
                if r == "s":
                    print("Identificado: Artrópodo venenoso (tarántula, escorpión, avispa, etc.)")
                else:
                    print("Identificado: Artrópodo no venenoso (mariposa, abeja, cangrejo, etc.)")
            else:
                print("Identificado: Invertebrado no artrópodo (moluscos, caracoles, pulpos, etc.)")
            return

        # Fallback
        print("No pude identificar el animal salvaje.")






#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#


def pedir_si_no(pregunta):
    """Pide repetidamente hasta que el usuario responda 's' o 'n' (acepta 'si'/'no')."""
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r in ("s", "si"):
            return "s"
        if r in ("n", "no"):
            return "n"
        print("Por favor responde 's' (sí) o 'n' (no).")

def main():
    print("Piensa en lo que sea y lo adivinaré en (hasta) 20 preguntas.\nResponde solo 's' o 'n'.\n")

    # Q1
    r = pedir_si_no("Q1: ¿Es algo abstracto o intangible (idea, emoción, número, concepto)?")
    if r == "s":
        # Agotar rama Abstracto/Intangible
        rama_abstracto()
        # Entraste en: Abstracto/Intangible -> (aquí agotar preguntas de esa categoría).
        return

    # Q2
    r = pedir_si_no("Q2: ¿Es un ser vivo?")
    if r == "s":
        # Agotar rama Seres vivos
        rama_seres_vivos()
        # Entraste en: Seres vivos -> (aquí agotar preguntas de esa categoría).
        return

    # Q3
    r = pedir_si_no("Q3: ¿Es un lugar o una construcción (por ejemplo: ciudad, montaña, edificio, río)?")
    if r == "s":
        # Agotar rama Lugares/Construcciones
        rama_lugares()
        # Entraste en: Lugar/Construcción -> (aquí agotar preguntas de esa categoría).
        return

    # Q4
    r = pedir_si_no("Q4: ¿Es una persona o un personaje (real o ficticio)?")
    if r == "s":
        # Agotar rama Persona/Personaje
        rama_persona()
        # Entraste en: Persona/Personaje -> (aquí agotar preguntas de esa categoría).
        return

    # Q5
    r = pedir_si_no(
        "Q5: ¿Es un fenómeno natural, un cuerpo celeste o una forma de energía (por ejemplo: lluvia, sol, luz, terremoto)?")
    if r == "s":
        # Agotar rama Fenómenos / Cuerpos celestes / Energía
        rama_fenomeno()
        # Entraste en: Fenómeno/Cuerpo celeste/Energía -> (aquí agotar preguntas de esa categoría).
        return

    # Q6
    r = pedir_si_no("Q6: ¿Es un objeto inanimado o cosa tangible (sea natural o fabricada por humanos)?")
    if r == "s":
        # Agotar rama Objetos inanimados
        rama_objeto()
        # Entraste en: Objeto inanimado -> (aquí agotar preguntas de esa categoría).
        return

    # Si todas las raíces son 'n'
    print("No se pudo ubicar con las preguntas raíz.")


if __name__ == "__main__":
    main()
