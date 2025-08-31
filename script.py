
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
def identificar_mamifero():  #salvajes mamiferos
    # Primero, si es carnívoro
    r = pedir_si_no("Q6: ¿Es carnívoro?")
    if r == "s":
        r = pedir_si_no("Q7: ¿Es felino?")
        if r == "s":
            r = pedir_si_no("Q8: ¿Es muy grande?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Es un felino grande sin manchas visibles?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Tiene rayas en el pelaje?")
                    if r == "s":
                        print("Pensaste en Tigre")
                    else:
                        r = pedir_si_no("Q11: ¿Tiene melena prominente?")
                        if r == "s":
                            print("Pensaste en León")
                        else:
                            print("Pensaste en Puma")
            else:
                r = pedir_si_no("Q9: ¿Tiene manchas en el pelaje?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Son rosetas grandes con centro más oscuro?")
                    if r == "s":
                        print("Pensaste en Jaguar")
                    else:
                        r = pedir_si_no("Q11: ¿Son manchas pequeñas, redondas, y el cuerpo es delgado y rápido?")
                        if r == "s":
                            print("Pensaste en Guepardo")
                        else:
                            print("Pensaste en Leopardo")
                else:
                    print("Felino pequeño salvaje poco común")

        else:  # No felino
            r = pedir_si_no("Q8: ¿Es de tamaño mediano/grande?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Es un tipo de oso?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Es un oso con pelaje blanco y vive en el Ártico?")
                    if r == "s":
                        print("Pensaste en Oso polar")
                    else:
                        print("Pensaste en Oso pardo")
                else:
                    r = pedir_si_no("Q10: ¿Es Hiena?")
                    if r == "s":
                        print("Pensaste en Hiena")
                    else:
                        print("Pensaste en Lobo")
            else:
                r = pedir_si_no("¿Aúlla o emite llamadas largas y aullidos?")
                if r == "s":
                    print("Pensaste en Lobo")
                else:
                    r = pedir_si_no("¿Emite un sonido similar a una risa o carcajada?")
                    if r == "s":
                        print("Pensaste en Hiena")
                    else:
                        print("Carnívoro grande poco común")
    else:  # No carnívoro
        r = pedir_si_no("Q7: ¿Es herbívoro?")
        if r == "s":
            # Herbívoros grandes
            r = pedir_si_no("Q8: ¿Es un herbívoro de gran tamaño (altura > 1,5 m o peso > 500 kg)?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Tiene cuello muy largo y patas muy altas?")
                if r == "s":
                    print("Pensaste en Jirafa")
                else:
                    r = pedir_si_no("Q9: ¿Tiene trompa larga y flexible para alcanzar hojas?")
                    if r == "s":
                        print("Pensaste en Elefante")
                    else:
                        r = pedir_si_no("Q10: ¿Tiene uno o más cuernos en la cabeza?")
                        if r == "s":
                            print("Pensaste en Rinoceronte")
                        else:
                            r = pedir_si_no("Q11: ¿Es robusto con cuerpo voluminoso y pasa tiempo en agua dulce?")
                            if r == "s":
                                print("Pensaste en Hipopótamo")
                            else:
                                print("Pensaste en Búfalo")
            else:
                # Herbívoros medianos/pequeños
                r = pedir_si_no("Q9: ¿Es trepador o pasa la mayor parte del tiempo en árboles?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Es marsupial y con orejas redondeadas?")
                    if r == "s":
                        print("Pensaste en Koala")
                    else:
                        r = pedir_si_no("Q11: ¿Es pequeño, ágil y con cola larga que ayuda a equilibrarse?")
                        if r == "s":
                            print("Pensaste en Lémur")
                        else:
                            r = pedir_si_no("Q12: ¿Es un primate grande con cuerpo robusto y rostro ancho?")
                            if r == "s":
                                r = pedir_si_no("Q13: ¿Tiene pecho y hombros muy musculosos y postura erguida?")
                                if r == "s":
                                    print("Pensaste en Gorila")
                                else:
                                    r = pedir_si_no("Q14: ¿Es ágil, social y con cara expresiva?")
                                    if r == "s":
                                        print("Pensaste en Chimpancé")
                                    else:
                                        r = pedir_si_no("Q15: ¿Se desplaza lentamente entre ramas con brazos largos?")
                                        if r == "s":
                                            print("Pensaste en Orangután")
                                        else:
                                            print("Pensaste en Babuino u otro primate grande")
                            else:
                                print("Mamífero trepador poco común")
                else:
                    # Herbívoros terrestres
                    r = pedir_si_no("Q10: ¿Es saltador con patas traseras fuertes?")
                    if r == "s":
                        print("Pensaste en Canguro")
                    else:
                        r = pedir_si_no("Q11: ¿Tiene cornamenta o cuernos ramificados?")
                        if r == "s":
                            r = pedir_si_no("Q12: ¿Es esbelto y ágil con astas ramificadas?")
                            if r == "s":
                                print("Pensaste en Venado")
                            else:
                                print("Pensaste en Antílope")
                        else:
                            r = pedir_si_no("Q12: ¿Tiene rayas en el cuerpo?")
                            if r == "s":
                                print("Pensaste en Cebra")
                            else:
                                r = pedir_si_no("Q13: ¿Tiene púas largas o defensas en el cuerpo?")
                                if r == "s":
                                    print("Pensaste en Puercoespín")
                                else:
                                    r = pedir_si_no("Q13: ¿Es un roedor grande semiacuático?")
                                    if r == "s":
                                        print("Pensaste en Carpincho")
                                    else:
                                        r = pedir_si_no("Q13: ¿Es robusto y terrestre con hocico ancho?")
                                        if r == "s":
                                            print("Pensaste en Jabalí")
                                        else:
                                            print("Herbívoro terrestre pequeño/mediano poco común")
        else:
            # Omnívoros
            r = pedir_si_no("Q8: ¿Se alimenta de plantas y ocasionalmente carne?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Tiene pelaje blanco y negro y se alimenta principalmente de bambú?")
                if r == "s":
                    print("Pensaste en Panda")
                else:
                    r = pedir_si_no("Q10: ¿Es un oso robusto de gran tamaño?")
                    if r == "s":
                        r = pedir_si_no("Q11: ¿Vive en regiones polares?")
                        if r == "s":
                            print("Pensaste en Oso polar")
                        else:
                            print("Pensaste en Oso pardo")
                    else:
                        print("Mamífero omnívoro poco común")


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
                r = pedir_si_no("Q7: ¿Es un canino  o felino ?")
                if r == "s":
                    r = pedir_si_no("Q8: ¿ladra?")
                    if r == "s":
                        print("Pensaste en un perro")
                    else:
                        print("Pensaste en un gato")
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
        r = pedir_si_no("Q5: ¿Es un mamífero?")
        if r == "s":
            identificar_mamifero()
            return


            #  Aves salvajes

        r = pedir_si_no("Q6: ¿Es un ave?")
        if r == "s":
            r = pedir_si_no("Q7: ¿Es un ave rapaz (caza otros animales)?")
            if r == "s":
                r = pedir_si_no("Q7a: ¿Es nocturna?")
                if r == "s":
                    print("Identificado: Búho o Lechuza")
                else:
                    r = pedir_si_no("Q7b: ¿Aparece en el escudo de la bandera mexicana?")
                    if r == "s":
                        print("Identificado: Águila")
                    else:
                        r = pedir_si_no("Q7c: ¿Se alimenta principalmente de carroña?")
                        if r == "s":
                            print("Identificado: Buitre")
                        else:
                            r = pedir_si_no("Q7d: ¿Es de gran tamaño con plumaje oscuro y alas largas para planear?")
                            if r == "s":
                                print("Identificado: Cóndor")
                            else:
                                print("Identificado: Halcón")
            else:
                r = pedir_si_no("Q8: ¿Vive principalmente en el agua o depende mucho de ella?")
                if r == "s":
                    r = pedir_si_no("Q8a: ¿Nada y no vuela, con colores blanco y negro regularmente?")
                    if r == "s":
                        print("Identificado: Pingüino")
                    else:
                        r = pedir_si_no("Q8b: ¿Tiene patas muy largas y rosadas?")
                        if r == "s":
                            print("Identificado: Flamenco")
                        else:
                            r = pedir_si_no("Q8c: ¿Tiene pico grande en forma de bolsa(forma de cuña o platano)?")
                            if r == "s":
                                print("Identificado: Pelícano")
                            else:
                                print("Identificado: Cisne, Gaviota, Cigüeña o Pato salvaje")
                else:
                    r = pedir_si_no("Q9: ¿Es un ave grande que no vuela?")
                    if r == "s":
                        print("Identificado: Avestruz, Emú o Casuario")
                    else:
                        r = pedir_si_no("Q10: ¿Es un ave muy colorida o exótica?")
                        if r == "s":
                            r = pedir_si_no("Q10a: ¿Tiene pico muy grande y colorido?")
                            if r == "s":
                                print("Identificado: Tucán")
                            else:
                                r = pedir_si_no("Q10b: ¿Tiene cola muy vistosa en forma de abanico?")
                                if r == "s":
                                    print("Identificado: Pavo real")
                                else:
                                    print("Identificado: Guacamaya o Loro")
                        else:
                            print("Identificado: Cuervo")
            return



        #  Reptiles salvajes
        r = pedir_si_no("Q7: ¿Es un reptil?")
        if r == "s":
            # Caparazón
            r = pedir_si_no("Q7: ¿Tiene caparazón?")
            if r == "s":
                r = pedir_si_no("Q8: ¿Vive principalmente en agua y es conocido por caminar lento?")
                if r == "s":
                    print("Identificado: Tortuga marina")
                else:
                    print("Identificado: Tortuga terrestre salvaje")
            else:  # Sin caparazón
                # Serpientes venenosas
                r = pedir_si_no("Q8: ¿Es venenoso?")
                if r == "s":
                    r = pedir_si_no("Q9: ¿Es una serpiente grande y constrictora?")
                    if r == "s":
                        print("Identificado: Anaconda o Pitón")
                    else:
                        r = pedir_si_no("Q10: ¿Tiene veneno por colmillos largos (cobra)?")
                        if r == "s":
                            print("Pensaste en Cobra")
                        else:
                            r = pedir_si_no("Q11: ¿Tiene veneno y castañetea o tiene cascabel?")
                            if r == "s":
                                print("Pensaste en serpiente Cascabel")
                            else:
                                print("Pensaste en una serpiente venenosa")
                else:  # Reptiles no venenosos
                    r = pedir_si_no("Q9: ¿Vive principalmente en ríos, lagos o humedales (ej. manglares),tiene cuerpo robusto  y es un carnívoro acuático?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Tiene hocico ancho y fuerte mandíbula (Cocodrilo)?")
                        if r == "s":
                            print("Pensaste en Cocodrilo")
                        else:
                            print("Pensaste en Caimán")
                    else:
                        r = pedir_si_no("Q10: ¿Es de tamaño mediano y puede cambiar de color ?")
                        if r == "s":
                            print("Pensaste en Camaleón")
                        else:
                            r = pedir_si_no("Q11: ¿Es grande, robusto y salvaje (Dragón de Komodo o Lagarto monitor)?")
                            if r == "s":
                                r = pedir_si_no("Q12: ¿Es un Dragón de Komodo?")
                                if r == "s":
                                    print("Pensaste en Dragón de Komodo")
                                else:
                                    print("Pensaste en un Lagarto")
                            else:
                                r = pedir_si_no("Q12: ¿Es pequeño y ágil,con cuerpo escamoso?")
                                if r == "s":
                                    r = pedir_si_no("Q13: ¿Tiene cola larga y puede cambiar ligeramente de color para camuflarse y es típico de climas tropicales?")
                                    if r == "s":
                                        print("Pensaste en Iguana")
                                    else:
                                        r9 = pedir_si_no("Q14: ¿Es visto normalmente en cas y puede regenerar pastes d esu cuerpo?")
                                        if r9 == "s":
                                            print("Identificado: Lagartija")
                                        else:
                                            print("Identificado: Gecko")
                                else:
                                    print("Pensaste en un reptil no venenoso poco común")
            return



        # Anfibios salvajes
        # Anfibios salvajes
        r = pedir_si_no("Q8: ¿Es un anfibio?")
        if r == "s":
            r2 = pedir_si_no("Q2: ¿Vive principalmente en agua o cerca de cuerpos de agua?")
            if r2 == "s":
                # Anfibios acuáticos
                r3 = pedir_si_no("Q3: ¿Tiene branquias externas visibles en etapa adulta?")
                if r3 == "s":
                    # Axolote vs Triturus
                    r4 = pedir_si_no(
                        "Q4: ¿Es famoso por ser símbolo de la Ciudad de México y aparece en carteles o billetes?")
                    if r4 == "s":
                        print("Identificado: Axolote")
                    else:
                        r5 = pedir_si_no("Q5: ¿Es pequeño y de colores brillantes, como en documentales de naturaleza?")
                        if r5 == "s":
                            print("Identificado: Triturus")
                        else:
                            print("Identificado: Salamandra")
                else:
                    # Ranas acuáticas
                    r4 = pedir_si_no("Q4: ¿Aparece en películas de princesas o cuentos infantiles?")
                    if r4 == "s":
                        print("Identificado: Sapo")
                    else:
                        print("Identificado: Rana")
            else:
                # Anfibios terrestres
                r3 = pedir_si_no("Q3: ¿Tiene piel rugosa y cuerpo robusto, típico de los que salen en cuentos?")
                if r3 == "s":
                    print("Identificado: Sapo")
                else:
                    r4 = pedir_si_no("Q4: ¿Es pequeño y ágil, de colores llamativos?")
                    if r4 == "s":
                        print("Identificado: Rana")
                    else:
                        print("Identificado: Salamandra")
            return

        #  Peces salvajes
        # Peces y animales acuáticos salvajes
        r = pedir_si_no("Q9: ¿Es un pez?")
        if r == "s":
            r2 = pedir_si_no("Q2: ¿Es un mamífero marino (respira aire, da a luz crías vivas)?")
            if r2 == "s":
                # Mamíferos marinos
                r3 = pedir_si_no("Q3: ¿Es considerado el animal mas grande del mundo y de color azul?")  # Ballena azul
                if r3 == "s":
                    print("Pensaste en Ballena azul")
                else:
                    r4 = pedir_si_no("Q4: ¿Es depredador tope y famoso por atacar tiburones en documentales?")
                    if r4 == "s":
                        print("Pensaste en Orca")
                    else:
                        print("Pensaste en Delfín")
            else:
                r3 = pedir_si_no("Q3: ¿Es un pez óseo (con aletas y escamas) o un invertebrado?")
                if r3 == "s":
                    # Peces óseos
                    r4 = pedir_si_no("Q4: ¿Es grande, con dientes afilados y detecta sangre a distancia?")
                    if r4 == "s":
                        print("Pensaste en Tiburón blanco")
                    else:
                        r5 = pedir_si_no(
                            "Q5: ¿Es agresivo en cardumen y famoso por morder humanos en películas de ríos tropicales?")
                        if r5 == "s":
                            print("Pensaste en Piraña")
                        else:
                            r6 = pedir_si_no(
                                "Q6: ¿Se encuentra comúnmente enlatado como alimento (ej. atún o sardina)?")
                            if r6 == "s":
                                print("Pensaste en Atún o Sardina")
                            else:
                                r7 = pedir_si_no("Q7: ¿Vive en agua dulce y es popular en pesca deportiva?")
                                if r7 == "s":
                                    print("Pensaste en Trucha")
                                else:
                                    print("Pensaste en otro pez óseo")
                else:
                    # Invertebrados acuáticos
                    r4 = pedir_si_no("Q4: ¿Tiene tentáculos y cuerpo blando sin columna?")
                    if r4 == "s":
                        r5 = pedir_si_no("Q5: ¿Es enorme y vive en profundidades, protagonista de mitos marinos?")
                        if r5 == "s":
                            print("Pensaste en Calamar gigante")
                        else:
                            r6 = pedir_si_no("Q6: ¿Es pequeño y con branquias visibles, famoso en acuarios?")
                            if r6 == "s":
                                print("Pensaste en Pulpo")
                            else:
                                print("Pensaste en otro cefalópodo")
                    else:
                        # Equinodermos
                        r5 = pedir_si_no("Q5: ¿Tiene forma de estrella?")
                        if r5 == "s":
                            print("Pensaste en Estrella de mar")
                        else:
                            r6 = pedir_si_no("Q6: ¿Es redondo y con pinchos?")
                            if r6 == "s":
                                print("Pensaste en Erizo de mar")
                        r7 = pedir_si_no("Q7: ¿Es una medusa, flotante y con tentáculos finos?")
                        if r7 == "s":
                            print("Pensaste en Medusa")
            return

        #  Invertebrados salvajes
        #  Invertebrados salvajes
        r = pedir_si_no("Q10: ¿Es un insecto o invertebrado?")
        if r == "s":
            r = pedir_si_no("Q2: ¿Tiene seis patas (como un insecto clásico como hormiga, mariposa o mosca )?")
            if r == "s":
                r = pedir_si_no("Q3: ¿Puede volar?")
                if r == "s":
                    r = pedir_si_no("Q4: ¿Produce miel o néctar?")
                    if r == "s":
                        print("Pensaste en una Abeja")
                    else:
                        r = pedir_si_no("Q5: ¿Pica con aguijón?")
                        if r == "s":
                            print("Pensaste en una Avispa")
                        else:
                            r = pedir_si_no("Q6: ¿Es muy pequeña y molesta en la comida?")
                            if r == "s":
                                print("Pensaste en una Mosca")
                            else:
                                r = pedir_si_no("Q7: ¿Transmite enfermedades peligrosas?")
                                if r == "s":
                                    print("Pensaste en un Mosquito")
                                else:
                                    print("Pensaste en una Mariposa)")
                else:
                    r = pedir_si_no("Q8: ¿Vive en colonias organizadas bajo tierra?")
                    if r == "s":
                        print("Pensaste en una Hormiga")
                    else:
                        r = pedir_si_no("Q9: ¿Se alimenta de madera?")
                        if r == "s":
                            print("Pensaste en un Termita")
                        else:
                            print("Pensaste en un Escarabajo")
            else:
                # No insecto clásico, puede ser arácnido o crustáceo
                r = pedir_si_no("Q10: ¿Tiene ocho patas?")
                if r == "s":
                    r = pedir_si_no("Q11: ¿Es muy grande y peluda?")
                    if r == "s":
                        print("Pensaste en una Tarántula")
                    else:
                        r = pedir_si_no("Q12: ¿Tiene pinza y veneno en la cola?")
                        if r == "s":
                            print("Pensaste en un Escorpión")
                        else:
                            print("Pensaste en una Araña")
                else:
                    # Otros invertebrados
                    r = pedir_si_no("Q13: ¿Vive en el agua?")
                    if r == "s":
                        print("Pensaste en Cangrejo")
                    else:
                        r = pedir_si_no("Q14: ¿Tiene concha en espiral y se mueve muy lento?")
                        if r == "s":
                            print("Pensaste en un Caracol")
                        else:
                            r = pedir_si_no("Q15: ¿Se alimenta de sangre?")
                            if r == "s":
                                r = pedir_si_no("Q16: ¿Es muy pequeña y salta?")
                                if r == "s":
                                    print("Pensaste en Pulga")
                                else:
                                    print("Pensaste en Garrapata ")
                            else:
                                print("Invertebrado desconocido")
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
