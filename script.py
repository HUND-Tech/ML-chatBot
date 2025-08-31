
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
    r = pedir_si_no("Q2: ¿Es un objeto natural (no fabricado por humanos)?")
    if r == "s":
        #obj_natural()
        return
    r = pedir_si_no("Q3: ¿Es artificial (fabricado por humanos)?")
    if r == "s":
        #obj_artificial()
        return
    r = pedir_si_no("Q5: ¿Es un producto de consumo?")
    if r == "s":
        #consumo()
        return
    r = pedir_si_no("Q6: ¿Es un residuo o desecho?")
    if r == "s":
        #residuos()
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

        #  Peces salvajes
        r = pedir_si_no("Q1: ¿Es un pez?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Es de agua salada?")
            if r == "s":
                print("Identificado: Pez de mar (atún, tiburón, pez loro, etc.)")
            else:
                print("Identificado: Pez de agua dulce (trucha, carpa, pez gato, etc.)")
            return

        #  Invertebrados salvajes
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

def obj_natural():#Q2
    
   #MINERALES
    r = pedir_si_no("Q3: ¿Es un mineral?")
    if r == "s":
        
        #minerales metálicos
        r = pedir_si_no("Q4: ¿Es metálico?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Es un considerado un metal precioso?")
            if r == "s":
                
                # metales preciosos
                r = pedir_si_no("Q6: ¿Es amarillo y muy blando?")
                if r == "s":
                    print("Oro")
                else:
                    r = pedir_si_no("Q7: ¿Es plateado y brillante?")
                    if r == "s":
                        print("Plata")
                    else:
                        print("Platino")
            else:
                
                # metales comunes                
                r = pedir_si_no("Q8: ¿Tiene color rojo naranjoso?")
                if r == "s":
                    print("Cobre")
                else:
                    r = pedir_si_no("Q9: ¿Es magnético?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Es común en herramientas?")
                        if r == "s":
                            print("Hierro")
                        else:
                            print("Níquel")
                    else:
                        r = pedir_si_no("Q11: ¿Es MUY ligero?")
                        if r == "s":
                            print("Aluminio")
                        else:
                            r = pedir_si_no("Q12: ¿Es blando y tóxico?")
                            if r == "s":
                                print("Plomo")
                            else:
                                r = pedir_si_no("Q13: ¿Es frágil pero resistente a la corrosión?")
                                if r == "s":
                                    print("Zinc")
                                else:
                                    r = pedir_si_no("Q14: ¿Es comúnmente usado en soldaduras?")
                                    if r == "s":
                                        print("Estaño")
                                    else:
                                        r = pedir_si_no("Q15: ¿Es líquido a temperatura ambiente?")
                                        if r == "s":
                                            print("Mercurio")
                                        else:
                                            print("Otro mineral metálico")
        else:
            
            # minerales no metálicos
            r = pedir_si_no("Q16: ¿Es MUY duro?")
            if r == "s":
                
                # piedras preciosas y cuarzo
                r = pedir_si_no("Q17: ¿Puede rayar a los demás minerales)?")
                if r == "s":
                    print("Diamante")
                else:
                    r = pedir_si_no("Q18: ¿Es rojo intenso?")
                    if r == "s":
                        print("Rubí")
                    else:
                        r = pedir_si_no("Q19: ¿Es azul profundo?")
                        if r == "s":
                            print("Zafiro")
                        else:
                            r = pedir_si_no("Q20: ¿Es verde intenso?")
                            if r == "s":
                                print("Esmeralda")
                            else:
                                print("Otra gema dura (cuarzo, amatista, topacio, turmalina, granate, etc.)")
            else:
                
                # minerales blandos o intermedios
                r = pedir_si_no("Q17: ¿Se puede rayar con la uña?")
                if r == "s":
                    r = pedir_si_no("Q18: ¿Es translúcido y muy blando?")
                    if r == "s":
                        print("Yeso")
                    else:
                        r = pedir_si_no("Q19: ¿Tiene sabor salado?")
                        if r == "s":
                            print("Halita (sal de mesa)")
                        else:
                            print("Otro mineral muy blando (talco, etc.)")
                else:
                    r = pedir_si_no("Q20: ¿Reacciona con efervescencia)?")
                    if r == "s":
                        print("Calcita (u otro carbonato)")
                    else:
                        print("Otro mineral no metálico (fluorita, apatito, feldespatos, etc.)")


    #ROCAS
    elif pedir_si_no("Q4: ¿Es una roca ?") == "s":
        
         # tipos principales
        r = pedir_si_no("Q5: ¿Es ígnea ?") #(formada por magma o lava)
        if r == "s":
            
            # igneas
            r = pedir_si_no("Q6: ¿Se formó en la superficie?")
            if r == "s":
                
                # extrusivas
                r = pedir_si_no("Q7: ¿Es negra y de grano fino?")
                if r == "s":
                    print("Basalto")
                else:
                    r = pedir_si_no("Q8: ¿Tiene bordes filosos?")
                    if r == "s":
                        print("Obsidiana")
                    else:
                        print("Andesita o riolita")
            else:
                
                # intrusivas
                r = pedir_si_no("Q6: ¿Es blanca rosada y de grano grueso?")
                if r == "s":
                    print("Granito")
                else:
                    print("Gabro o diorita")

        else:
            r = pedir_si_no("Q5: ¿Es sedimentaria") #(formada por acumulación de sedimentos)
            if r == "s":
                
                # sedimentarias
                r = pedir_si_no("Q6: ¿Se raya con la uña fácilmente?")
                if r == "s":
                    print("Yeso o caliza blanda")
                else:
                    r = pedir_si_no("Q7: ¿Reacciona con efervescencia?")
                    if r == "s":
                        print("Caliza o dolomita")
                    else:
                        r = pedir_si_no("Q8: ¿Está formada por granos de arena visibles?")
                        if r == "s":
                            print("Arenisca")
                        else:
                            r = pedir_si_no("Q9: ¿Contiene fragmentos grandes y redondeados?")
                            if r == "s":
                                print("Conglomerado")
                            else:
                                print("Lutita o arcilla")

            else:
                # metamórficas
                r = pedir_si_no("Q6: ¿Presenta capas o foliación visible?")
                if r == "s":
                    r = pedir_si_no("Q7: ¿Es de grano muy fino y se rompe en láminas delgadas?")
                    if r == "s":
                        print("Pizarra")
                    else:
                        r = pedir_si_no("Q8: ¿Tiene bandas claras y oscuras alternadas?")
                        if r == "s":
                            print("Gneis")
                        else:
                            print("Esquisto")
                else:
                    r = pedir_si_no("Q7: ¿Es dura, masiva y puede tener aspecto cristalino?")
                    if r == "s":
                        r = pedir_si_no("Q8: ¿Se raya con cuchillo)?")
                        if r == "s":
                            print("Mármol")
                        else:
                            print("Cuarcita")
                    else:
                        print("Otra roca metamórfica menos común")
                        
    #RESTOS ORGÁNICOS NO VIVOS                    
    r = pedir_si_no("Q4: ¿Proviene de un ser vivo?")
    if r == "s":
        
        # de acuerdo a su oirgen
        r = pedir_si_no("Q5: Su origen es vegetal?")
        if r == "s":
            
            # origen Vegetal
            r = pedir_si_no("Q6: ¿Está fosilizado?") # (petrificado, mineralizado)
            if r == "s":
                r = pedir_si_no("Q7: ¿Es un tronco?")
                if r == "s":
                    print("Tronco petrificado")
                else:
                    r = pedir_si_no("Q8: ¿Es una hoja impresa en roca?")
                    if r == "s":
                        print("Hoja fósil")
                    else:
                        r = pedir_si_no("Q9: ¿Es resina fosilizada?")
                        if r == "s":
                            print("Ámbar")
                        else:
                            print("Otro fósil vegetal")
            else:
                
                # No fosilizado
                r = pedir_si_no("Q7: ¿Es leñoso?") #(tronco, rama)
                if r == "s":
                    r = pedir_si_no("Q8: ¿Presenta anillos de crecimiento visibles?")
                    if r == "s":
                        print("Madera")
                    else:
                        print("Fragmento de tronco o rama")
                else:                 
                        r = pedir_si_no("Q8: ¿Está carbonizado?")
                        if r == "s":
                            print("Carbón vegetal")
                        else:
                            print("Otro resto vegetal")

        else:
            
            # de orugen Animal fosilizado
            r = pedir_si_no("Q12: ¿Está fosilizado?")
            if r == "s":
                r = pedir_si_no("Q13: ¿Es un hueso?")
                if r == "s":
                    r = pedir_si_no("Q14: ¿Es un hueso grande?") #(ej. fémur, mandíbula)
                    if r == "s":
                        print("Hueso fósil grande")
                    else:
                        print("Hueso fósil pequeño")
                else:
                    r = pedir_si_no("Q15: ¿Es una concha?")
                    if r == "s":
                        r = pedir_si_no("Q16: ¿Es bivalva?")
                        if r == "s":
                            print("Concha fósil bivalva")
                        else:
                            print("Caracol fósil (concha univalva)")
                    else:
                        r = pedir_si_no("Q17: ¿Es un diente fosilizado?")
                        if r == "s":
                            print("Diente fósil")
                        else:
                            print("Otro fósil animal")
            else:
                
                # de origen animal no fosilizado
                r = pedir_si_no("Q13: ¿Es un fragmento completo?")
                if r == "s":
                    r = pedir_si_no("Q14: ¿Es un hueso largo?") #(como fémur, húmero)
                    if r == "s":
                        r = pedir_si_no("Q15: ¿Es parte de una extremidad superior?")
                        if r == "s":
                            print("Un hueso de húmero")
                        else:
                            print("Un hueso de fémur")
                    else:
                        r = pedir_si_no("Q16: ¿Es un hueso plano?") #(como cráneo, costilla)
                        if r == "s":
                            r = pedir_si_no("Q17: ¿Protege órganos internos?")
                            if r == "s":
                                print("Costilla")
                            else:
                                print("Cráneo")
                        else:
                            r = pedir_si_no("Q18: ¿Es pequeño e irregular?") #(como vértebra, mano, pie)
                            if r == "s":
                                print("Vértebra o hueso pequeño")
                            else:
                                print("Un hueso de mano o pie")
                else:
                    print("Fragmento de hueso")

def obj_artificial():#Q3
    #HERRAMIENTAS Y UTENSILIOS
    #MÁQUINAS Y ELECTRÓNICOS
    #MUEBLES
    #CONSTRUCCIONES Y ESTRUCTURAS
    #VEHÍCULOS Y MEDIOS DE TRANSPORTE
    #ROPA Y ACCESORIOS
    #JUGUETES Y ARTÍCULOS DE OCIO
    #INSTRUMENTOS MUSICALES
    #ARTÍCULOS DEPORTIVOS

            

       




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