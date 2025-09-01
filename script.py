
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
    r = pedir_si_no("Q4: ¿Es una planta, fruta, verdura o semilla?")
    if r == "s":
        plantas()
        return
    r = pedir_si_no("Q5: ¿Es un hongo?")
    if r == "s":
        hongos()
        return
    r = pedir_si_no("Q6: ¿Es un microorganismo?")
    if r == "s":
        microorganismos()
        return
    print("No se pudo ubicar con las preguntas.")

def rama_lugares():
    r = pedir_si_no("Q4: ¿Es un lugar natural?")
    if r == "s":
        lugares_naturales()
        return
    r = pedir_si_no("Q5: ¿Es una construcción hecha por el ser humano?")
    if r == "s":
        construcciones_humanas()
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
                        r = pedir_si_no("Q11: ¿Está adaptado a vivir en desiertos y puede pasar largos períodos sin agua?")
                        if r == "s":
                            print("Pensaste en Camello")
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
                r = pedir_si_no("Q8: ¿Hace cacareo o graznido?")
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
            print("Pensaste en un reptil doméstico como una iguana, o en un reptil pequeno).")
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
                                    r=pedir_si_no("¿Puede volar hacia atras?")
                                    if r == "s":
                                        print("Pensaste en un colibri")
                                    else:
                                        print("Pensaste en un Guacamaya o Loro")
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
                    r = pedir_si_no("Q9: ¿Vive principalmente en ríos, lagos o humedales (ej. manglares),con dientes visibles incluso con la boca cerrada?y es un carnívoro acuático?")
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
                                        r9 = pedir_si_no("Q14: ¿Es visto normalmente en casa y puede regenerar partes de su cuerpo?")
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
                r3 = pedir_si_no("Q3: ¿Es un pez cartilaginoso (tiburón, raya)?")
                if r3 == "s":
                    # Peces cartilaginosos
                    r4 = pedir_si_no("Q4: ¿Es grande, con dientes afilados y detecta sangre a distancia?")
                    if r4 == "s":
                        print("Pensaste en Tiburón blanco")
                    else:
                        print("Pensaste en otro pez cartilaginoso")
                else:
                    r3 = pedir_si_no("Q3: ¿Es un pez óseo (con aletas y escamas) o un invertebrado?")
                    if r3 == "s":
                        r5 = pedir_si_no("Q5: ¿Es agresivo en cardumen y famoso por morder humanos en películas de ríos tropicales?")
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

def frutas():
    r = pedir_si_no("Q7: ¿Es cítrica?")
    if r == "s":
        r = pedir_si_no("Q6: ¿Tiene un color anaranjado y pulpa anaranjada?")
        if r == "s":
            r = pedir_si_no("Q7: ¿Es más pequeña y fácil de pelar?")
            if r == "s":
                print("¡Pensaste en una mandarina!")
            else:
                print("¡Pensaste en una naranja!")
        else:
            r = pedir_si_no("Q8: ¿Es de color amarillo o verde fuerte?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Es muy ácido y pequeño y con color verde?")
                if r == "s":
                    print("¡Pensaste en un limón!")
                else:
                    print("¡Pensaste en una lima!")
            else:
                r = pedir_si_no("Q10: ¿El color de su pulpa es morado/rosado por dentro y más grande que una naranja?")
                if r == "s":
                    print("¡Pensaste en una toronja!")
                else:
                    r = pedir_si_no("Q11: ¿Tiene muchas semillas pequeñas y un sabor muy intenso?")
                    if r == "s":
                        print("¡Pensaste en un maracuyá!")
                    else:
                        print("Podría ser otra fruta cítrica menos común.")
    else:
        # No es cítrica
        r = pedir_si_no("Q8: ¿Es una fruta de color rojo?")
        if r == "s":
            r = pedir_si_no("Q9: ¿Es conocida como la fruta prohibida en cuentos o muy común en mercados?")
            if r == "s":
                print("¡Pensaste en una manzana roja!")
            else:
                r = pedir_si_no("Q10: ¿Es pequeña y tiene semillas visibles por fuera?")
                if r == "s":
                    r = pedir_si_no("Q11: ¿Se usa mucho en postres como pasteles o helados?")
                    if r == "s":
                        print("¡Pensaste en una fresa!")
                    else:
                        # Aquí insertamos la pregunta del jitomate
                        r= pedir_si_no("Q9: ¿Se consume principalmente como ingrediente en comidas saladas o salsas rojas?")
                        if r== "s":
                            print("¡Pensaste en un jitomate!")
                        else:
                            print("¡Pensaste en una frutilla similar a la fresa pero menos común!")  # opcional
                else:
                    r = pedir_si_no("Q10: ¿Es dura por fuera y al abrirla tiene muchas semillas internas jugosas?")
                    if r == "s":
                        print("¡Pensaste en una granada!")
                    else:
                        r = pedir_si_no("Q11: ¿Es muy pequeña y redonda, generalmente consumida de a una o en postres?")
                        if r == "s":
                            print("¡Pensaste en una cereza!")
                        else:
                            r = pedir_si_no("Q12: ¿Es más oscura, como morada o negra?")
                            if r == "s":
                                r = pedir_si_no("Q13: ¿Se usa en mermeladas o jugos?")
                                if r == "s":
                                    print("¡Pensaste en una mora!")
                                else:
                                    print("¡Pensaste en un arándano!")
        else:
            # No es roja
            r = pedir_si_no("Q9: ¿Es una fruta grande?")
            if r == "s":
                r = pedir_si_no("Q10: ¿Es verde por fuera y roja por dentro con semillas negras?")
                if r == "s":
                    print("¡Pensaste en una sandía!")
                else:
                    r = pedir_si_no("Q11: ¿Es amarilla por dentro y con cáscara dura, con una corona en la parte superior?")
                    if r == "s":
                        print("¡Pensaste en una piña!")
                    else:
                        r = pedir_si_no("Q15: ¿Es verde claro por fuera, alargada y anaranjada por dentro con semillas negras en el centro?")
                        if r == "s":
                            print("¡Pensaste en una papaya!")
                        else:
                            r = pedir_si_no("Q16: ¿Es redonda, con piel rugosa o reticulada, y pulpa anaranjada o verde por dentro?")
                            if r == "s":
                                print("¡Pensaste en un melón!")
                            else:
                                r = pedir_si_no("Q19: ¿Tiene cáscara dura, fibrosa, marrón por fuera y blanco por dentro?")
                                if r == "s":
                                    print("¡Pensaste en un coco!")
                                else:
                                    print("No se logró adivinar la fruta, revisa las características.")
            else:
                # No es grande
                r = pedir_si_no("Q10: ¿Es alargada y de color amarillo?")
                if r == "s":
                    print("¡Pensaste en un plátano!")
                else:
                    r = pedir_si_no("Q17: ¿Es de cáscara marrón y dura?")
                    if r == "s":
                        print("¡Pensaste en un coco!")
                    else:
                        r = pedir_si_no("Q18: ¿Tiene cáscara fina, vellosa y a veces nombrada como melocoton?")
                        if r == "s":
                            print("¡Pensaste en un durazno!")
                        else:
                            r = pedir_si_no("Q19: ¿Es verde o café por fuera y verde por dentro con semillas negras?")
                            if r == "s":
                                print("¡Pensaste en un kiwi!")
                            else:
                                r = pedir_si_no("Q20: ¿Se encuentra en racimos, son pequenas y redondeadas?")
                                if r == "s":
                                    print("¡Pensaste en una uva!")
                                else:
                                    print("¡Podría ser una pera, ciruela o higo!")
        return

def verduras():
    # Verduras y hortalizas más comunes con preguntas más específicas
    r = pedir_si_no("Q7: ¿Se consume principalmente la hoja de la planta?")
    if r == "s":
        r = pedir_si_no("Q6a1: ¿Tiene hojas verdes grandes y se usa en ensaladas?")
        if r == "s":
            print("¡Pensaste en Lechuga!")
        else:
            r = pedir_si_no("Q6a2: ¿Se cocina frecuentemente en sopas o guisos?")
            if r == "s":
                print("¡Pensaste en Espinaca o Acelga!")
            else:
                print("¡Pensaste en Rúcula, Berro o Endibia!")

    else:
        r = pedir_si_no("Q6b: ¿Se consume el tallo o raíz de la planta o se categoriza como un tubérculo ?")
        if r == "s":
            r = pedir_si_no("Q6b1: ¿Es un tubérculo de color naranja y crujiente?")
            if r == "s":
                print("¡Pensaste en Zanahoria!")
            else:
                r = pedir_si_no("Q6b2: ¿Es un tubérculo redondo y se encuentra bajo tierra?")
                if r == "s":
                    r = pedir_si_no("Q6b2a: ¿Es de color amarillo o blanco?")
                    if r == "s":
                        print("¡Pensaste en Papa!")
                    else:
                        print("¡Pensaste en Nabo o Remolacha!")
                else:
                    r = pedir_si_no("Q6b3: ¿Es un bulbo con aroma fuerte?")
                    if r == "s":
                        r2 = pedir_si_no("Q6b3a: ¿Al pelarlo normalmente hace llorar?")
                        if r2 == "s":
                            print("¡Pensaste en Cebolla!")
                        else:
                            r3 = pedir_si_no("Q6b3b: ¿Está compuesto por pequeños dientes comestibles?")
                            if r3 == "s":
                                print("¡Pensaste en Ajo!")
                            else:
                                print("¡Pensaste en Puerro o Espárrago!")
                    else:
                        r4 = pedir_si_no("Q6b4: ¿Es alargado y de color verde?")
                        if r4 == "s":
                            print("¡Pensaste en Pepino o Pepinillo!")
                        else:
                            r5 = pedir_si_no("Q6b5: ¿Es grande y de color morado o violeta?")
                            if r5 == "s":
                                print("¡Pensaste en Berenjena!")
                            else:
                                r6 = pedir_si_no("Q6b6: ¿Es redonda, roja y usualmente se usa en salsas?")
                                if r6 == "s":
                                    print("¡Pensaste en Tomate!")
                                else:
                                    print("¡Pensaste en Pimiento, Chayote o Calabacín!")
        return

def cereales():
    # Cereales y granos
    r = pedir_si_no("Q7: ¿Se consume principalmente como grano entero o molido?")
    if r == "s":
        r = pedir_si_no("Q8: ¿Es de color blanco o ligeramente amarillo y se consume cocido en casi todo el mundo?")
        if r == "s":
            print("¡Pensaste en arroz!")
        else:
            r = pedir_si_no(
                "Q9: ¿Se usa mucho para hacer tortillas, tamales o como base de platillos en México y América Latina?")
            if r == "s":
                print("¡Pensaste en maíz!")
            else:
                r = pedir_si_no("Q10: ¿Se utiliza principalmente para hacer pan, galletas y pasteles?")
                if r == "s":
                    print("¡Pensaste en trigo!")
                else:
                    r = pedir_si_no("Q11: ¿Es oscuro, se consume en guisos, sopas o ensaladas como legumbre?")
                    if r == "s":
                        r = pedir_si_no("Q12: ¿Es pequeño y redondo, muy común en cocina mexicana?")
                        if r == "s":
                            print("¡Pensaste en frijol!")
                        else:
                            r = pedir_si_no("Q13: ¿Es un grano pequeño, usado en sopas, ensaladas o como complemento de otros platillos?")
                            if r == "s":
                                print("¡Pensaste en lenteja o garbanzo!")
                            else:
                                r = pedir_si_no("Q14: ¿Es pequeño, redondo y se considera un superalimento?")
                                if r == "s":
                                    r = pedir_si_no("Q15: ¿Es plano y redondo, parecido a semillas de amaranto?")
                                    if r == "s":
                                        print("¡Pensaste en amaranto!")
                                    else:
                                        print("¡Pensaste en chía!")
        return

def plantas():
    r = pedir_si_no("Q5: ¿Es comestible?")
    if r == "s":
        r=pedir_si_no("Q6: ¿Es una fruta?")
        if r == "s":
            frutas()
        else:
            r=pedir_si_no("Q6: ¿Es una verdura u hortaliza?")
            if r == "s":
                print("")
                verduras()
            else:
                r=pedir_si_no("Q7: ¿Es un cereal o grano o leguminosa?")
                if r == "s":
                    print("")
                    cereales()
                else:
                    r=pedir_si_no("Q8: ¿Es una hierba comestible (condimento/especia)?")
                    if r == "s":
                        print("")
                    else:
                        print("No se logro advinar que oebsaste")

    else:
        r=pedir_si_no("Q5: ¿Es ornamental (flores o de jardín)?")
        if r == "s":
            print("Pensaste en flores o arboles decorativos")
        else:
            r=pedir_si_no("Q6: ¿Se usa con fines medicinales o industriales?")
            if r == "s":
                print("pensaste en ")
            else:
                print("pensaste en un tipo de planta muy poco comun")

def hongos():
    r = pedir_si_no("Q1: ¿Es comestible sin riesgos para la salud?")
    if r == "s":
        r = pedir_si_no("Q2: ¿Es pequeño y se consume en ensaladas o sopas comunes?")
        if r == "s":
            print("¡Pensaste en champiñón!")
        else:
            r = pedir_si_no("Q3: ¿Es grande y se usa en platos gourmet o al horno?")
            if r == "s":
                print("¡Pensaste en portobello!")
            else:
                r = pedir_si_no("Q4: ¿Tiene forma de abanico o crece en racimos en la madera?")
                if r == "s":
                    print("¡Pensaste en hongo ostra!")
                else:
                    print("¡Pensaste en setas comestibles variadas!")
    else:
        r = pedir_si_no("Q5: ¿Es de color rojo con puntos blancos o de apariencia llamativa?")
        if r == "s":
            print("¡Pensaste en Amanita muscaria (venenoso)!")
        else:
            r = pedir_si_no("Q6: ¿Es oscuro y se utiliza en cocina gourmet como condimento?")
            if r == "s":
                print("¡Pensaste en trufa!")
            else:
                print("¡Pensaste en otro hongo venenoso o tóxico!")

def microorganismos():
    r = pedir_si_no("Q1: ¿Es visible solo con microscopio?")
    if r == "s":
        r = pedir_si_no("Q2: ¿Vive principalmente en agua o ambientes húmedos?")
        if r == "s":
            r = pedir_si_no("Q3: ¿Realiza fotosíntesis y produce oxígeno?")
            if r == "s":
                print("¡Pensaste en algas microscópicas!")
            else:
                print("¡Pensaste en protozoos o mohos acuáticos!")
        else:
            r = pedir_si_no("Q4: ¿Se utiliza en alimentos como pan, yogurt o cerveza?")
            if r == "s":
                print("¡Pensaste en bacterias o levaduras beneficiosas!")
            else:
                r = pedir_si_no("Q5: ¿Puede causar enfermedades?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Se replica solo dentro de células y no con nutrición propia?")
                    if r == "s":
                        print("¡Pensaste en un virus!")
                    else:
                        print("¡Pensaste en bacterias patógenas!")
                else:
                    print("¡Pensaste en otros microorganismos benignos!")
    else:
        print("No se pudo identificar el microorganismo.")

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
    
    # MÁQUINAS Y ELECTRÓNICOS
    r = pedir_si_no("Q4: ¿Requiere electricidad para funcionar?")
    if r == "s":
        
        # comunicación 
        r = pedir_si_no("Q5: ¿Tiene pantalla?")
        if r == "s":
            
            # dispositivos con pantalla
            r = pedir_si_no("Q6: ¿Es portátil?") #que se pueda llevar fácilemente
            if r == "s":
                r = pedir_si_no("Q7: ¿Tiene pantalla táctil?")
                if r == "s":
                    print("Smartphone")
                else:
                    print("Computadora portátil")
            else:
                r = pedir_si_no("Q8: ¿Se usa principalmente para entretenimiento?")
                if r == "s":
                    print("Televisión")
                else:
                    print("PC de escritorio")
        else:
            
            #electrodoméstico
            # sin pantalla
            r = pedir_si_no("Q6: ¿Se usa en la cocina?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Mantiene cosas frías?")
                if r == "s":
                    r = pedir_si_no("Q8: ¿Mantiene cosas congeladas?")
                    if r == "s":
                        print("Congelador")
                    else:
                        print("Refrigerador")
                else:
                    r = pedir_si_no("Q8: ¿Calienta comida rápidamente?")
                    if r == "s":
                        print("Microondas")
                    else:
                        r = pedir_si_no("Q9: ¿Lava ropa?")
                        if r == "s":
                            print("Lavadora")
                        else:
                            print("Otro electrodoméstico")
            else:
                r = pedir_si_no("Q7: ¿Reproduce música?")
                if r == "s":
                    print("Radio")
                else:
                    r = pedir_si_no("Q8: ¿Limpia el suelo?")
                    if r == "s":
                        print("Aspiradora")
                    else:
                        print("Otro aparato eléctrico")
    
    # ROPA Y ACCESORIOS
    elif pedir_si_no("Q4: ¿Se lleva puesto en el cuerpo?") == "s":
        
        r = pedir_si_no("Q5: ¿Se lleva en los pies?")
        if r == "s":
            
            # calzado
            r = pedir_si_no("Q6: ¿Es utilizado comúnmente como calzado formal?")
            if r == "s":
                print("Zapatos")
            else:
                r = pedir_si_no("Q7: ¿Es utilizado principalmente para deporte o ejercicio?")
                if r == "s":
                    print("Tenis")
                else:
                    r = pedir_si_no("Q8: ¿Al usarlo se ven los dedos de los pies?")
                    if r == "s":
                        print("Sandalias")
                    else:
                        print("Botas")
        else:
            r = pedir_si_no("Q6: ¿Cubre el torso o las piernas?")
            if r == "s":
                
                # vestimenta
                r = pedir_si_no("Q7: ¿Es ropa interior?")
                if r == "s":
                    r = pedir_si_no("Q8: ¿Es para la parte superior del cuerpo?")
                    if r == "s":
                        print("Sostén/Camiseta interior")
                    else:
                        print("Calzones/Boxers")
                else:
                    r = pedir_si_no("Q8: ¿Es para nadar o la playa?")
                    if r == "s":
                        r = pedir_si_no("Q9: ¿Es de una sola pieza?")
                        if r == "s":
                            print("Traje de baño")
                        else:
                            print("Un bikini")
                    else:
                        r = pedir_si_no("Q9: ¿Se puede colocar encima de otra ropa?")
                        if r == "s":
                            r = pedir_si_no("Q10: ¿Tiene mangas?")
                            if r == "s":
                                r = pedir_si_no("Q11: ¿Es muy largo y amplio?")
                                if r == "s":
                                    print("Abrigo")
                                else:
                                    print("Chamarra")
                            else:
                                print("Chaleco")
                        else:
                            r = pedir_si_no("Q10: ¿Cubre las piernas?")
                            if r == "s":
                                r = pedir_si_no("Q11: ¿Cubre hasta los tobillos?")
                                if r == "s":
                                    print("Pantalón")
                                else:
                                    print("Short")
                            else:
                                r = pedir_si_no("Q11: ¿Tiene mangas?")
                                if r == "s":
                                    r = pedir_si_no("Q12: ¿Es formal?")
                                    if r == "s":
                                        print("Camisa")
                                    else:
                                        r = pedir_si_no("Q13: ¿Es típicamente femenina?")
                                        if r == "s":
                                            print("Blusa")
                                        else:
                                            print("Playera")
                                else:
                                    print("Vestido")
            else:
                
               # accesorios
                r = pedir_si_no("Q7: ¿Se lleva en la cabeza?")
                if r == "s":
                    r = pedir_si_no("Q8: ¿Protege del sol o lluvia?")
                    if r == "s":
                        r = pedir_si_no("Q9: ¿Tiene visera")
                        if r == "s":
                            print("Gorra/Sombrero")
                        else:
                            print("Capucha")
                    else:
                        r = pedir_si_no("Q9: ¿Ayuda a ver mejor?")
                        if r == "s":
                            r = pedir_si_no("Q10: ¿Protege del sol?")
                            if r == "s":
                                print("Gafas de sol")
                            else:
                                print("Lentes")
                        else:
                            r = pedir_si_no("Q10: ¿Es decorativo o para el cabello?")
                            if r == "s":
                                print("Diadema/Banda")
                            else:
                                print("Casco")
                else:
                    r = pedir_si_no("Q8: ¿Se lleva en las orejas?")
                    if r == "s":
                        print("Aretes/Pendientes")
                    else:
                        r = pedir_si_no("Q9: ¿Se lleva en el cuello?")
                        if r == "s":
                            r = pedir_si_no("Q10: ¿Es para abrigarse?")
                            if r == "s":
                                print("Bufanda")
                            else:
                                r = pedir_si_no("Q11: ¿Es de metal o joyería?")
                                if r == "s":
                                    print("Collar")
                                else:
                                    print("Corbata")
                        else:
                            r = pedir_si_no("Q10: ¿Se lleva en las manos o muñecas?")
                            if r == "s":
                                r = pedir_si_no("Q11: ¿Muestra la hora?")
                                if r == "s":
                                    print("Reloj")
                                else:
                                    r = pedir_si_no("Q12: ¿Es joyería decorativa?")
                                    if r == "s":
                                        print("Pulsera/Anillo")
                                    else:
                                        print("Guantes")
                            else:
                                r = pedir_si_no("Q11: ¿Se lleva en la cintura?")
                                if r == "s":
                                    print("Cinturón")
                                else:
                                    print("Otro accesorio")

def lugares_naturales(): #Q4
    r = pedir_si_no("Q6: ¿Es principalmente acuático?")
    if r == "s":
        r = pedir_si_no("Q7: ¿Es de agua salada?")
        if r == "s":
            r2 = pedir_si_no("Q8: ¿Tiene olas y playa?")
            if r2 == "s":
                print("Pensaste en una playa o costa")
            else:
                print("Pensaste en el mar o océano")
        else:
            r2 = pedir_si_no("Q8: ¿El agua fluye continuamente?")
            if r2 == "s":
                print("Pensaste en un río")
            else:
                r3 = pedir_si_no("Q9: ¿Está contenido en un espacio limitado y tranquilo?")
                if r3 == "s":
                    print("Pensaste en un lago")
                else:
                    r4 = pedir_si_no("Q10: ¿El agua cae desde una altura?")
                    if r4 == "s":
                        print("Pensaste en una cascada")
                    else:
                        print("Lugar acuático poco común")
    else:
        r = pedir_si_no("Q7: ¿Es muy alto y rocoso?")
        if r == "s":
            r2 = pedir_si_no("Q8: ¿Tiene forma cónica y expulsa lava o humo?")
            if r2 == "s":
                print("Pensaste en un volcán")
            else:
                print("Pensaste en una montaña")
        else:
            r2 = pedir_si_no("Q8: ¿Tiene mucha vegetación?")
            if r2 == "s":
                print("Pensaste en un bosque o selva")
            else:
                r3 = pedir_si_no("Q9: ¿Es árido y arenoso?")
                if r3 == "s":
                    print("Pensaste en un desierto")
                else:
                    r4 = pedir_si_no("Q10: ¿Está bajo tierra?")
                    if r4 == "s":
                        print("Pensaste en una cueva")
                    else:
                        print("Lugar terrestre poco común")
        return

def construcciones_humanas():
    # Edificios habitacionales
    r = pedir_si_no("Q6: ¿Se utiliza principalmente para vivir?")
    if r == "s":
        r = pedir_si_no("Q7: ¿Es una construcción grande y lujosa, a menudo histórica?")
        if r == "s":
            r = pedir_si_no("Q8: ¿Tiene torreones, murallas o aspecto de fortaleza?")
            if r == "s":
                print("¡Pensaste en un castillo!")
            else:
                r = pedir_si_no("Q9: ¿Se trata de una residencia enorme con jardines extensos?")
                if r == "s":
                    print("¡Pensaste en una mansión o villa!")
                else:
                    print("¡Pensaste en un chalet o hacienda!")
        else:
            r = pedir_si_no("Q8: ¿Está compuesto por varios pisos y viviendas similares en un mismo edificio?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Es moderno y alto, con muchos apartamentos por piso?")
                if r == "s":
                    print("¡Pensaste en un rascacielos o condominio!")
                else:
                    print("¡Pensaste en un departamento o dúplex/tríplex!")
            else:
                r = pedir_si_no("Q9: ¿Es una vivienda pequeña y rústica, normalmente en zonas de campo o montaña?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Es de madera o materiales naturales y se usa como refugio temporal?")
                    if r == "s":
                        print("¡Pensaste en una cabaña o refugio!")
                    else:
                        print("¡Pensaste en un rancho o villa rural!")
                else:
                    r = pedir_si_no("Q10: ¿Se utiliza temporalmente para alojamiento de viajeros o estudiantes?")
                    if r == "s":
                        r = pedir_si_no("Q11: ¿Es un hotel con servicios para turistas?")
                        if r == "s":
                            print("¡Pensaste en un hotel!")
                        else:
                            r3 = pedir_si_no("Q11: ¿Es una residencia para estudiantes o albergue juvenil?")
                            if r3 == "s":
                                print("¡Pensaste en una residencia estudiantil o albergue!")
                            else:
                                print("¡Pensaste en otro tipo de vivienda pequeña o alojamiento temporal!")
    else:
        r = pedir_si_no("Q7: ¿Se utiliza para educación, salud o cultura?")
        if r == "s":
            r = pedir_si_no("Q8: ¿Está relacionado con la educación?")
            if r == "s":
                r2 = pedir_si_no("Q9: ¿Reciben principalmente niños o adolescentes?")
                if r2 == "s":
                    print("¡Pensaste en una escuela o colegio!")
                else:
                    r3 = pedir_si_no("Q10: ¿Es un centro de educación superior con facultades y campus extensos?")
                    if r3 == "s":
                        print("¡Pensaste en una universidad!")
                    else:
                        print("¡Pensaste en otro tipo de institución educativa!")
            else:
                r = pedir_si_no("Q11: ¿Se relaciona con la salud?")
                if r == "s":
                    r2 = pedir_si_no("Q12: ¿Atiende a toda la población con diferentes servicios médicos?")
                    if r2 == "s":
                        print("¡Pensaste en un hospital o clínica pública!")
                    else:
                        print("¡Pensaste en un consultorio o clínica pequeña!")
                else:
                    r = pedir_si_no("Q13: ¿Se relaciona con la cultura o las artes?")
                    if r == "s":
                        r2 = pedir_si_no("Q14: ¿Guarda colecciones de objetos históricos o artísticos para exhibición?")
                        if r2 == "s":
                            print("¡Pensaste en un museo!")
                        else:
                            r3 = pedir_si_no("Q15: ¿Ofrece espacios para presentaciones, obras o conciertos?")
                            if r3 == "s":
                                r4 = pedir_si_no("Q16: ¿Se centra principalmente en teatro y espectáculos en vivo?")
                                if r4 == "s":
                                    print("¡Pensaste en un teatro!")
                                else:
                                    print("¡Pensaste en un centro cultural!")
                            else:
                                r5 = pedir_si_no(
                                    "Q17: ¿Se enfoca en el préstamo y consulta de libros y material bibliográfico?")
                                if r5 == "s":
                                    r6 = pedir_si_no("Q18: ¿Está asociada a una universidad?")
                                    if r6 == "s":
                                        print("¡Pensaste en una biblioteca universitaria!")
                                    else:
                                        print("¡Pensaste en una biblioteca pública!")
                                else:
                                    print("¡Pensaste en otro edificio cultural o educativo!")
        else:
            r = pedir_si_no("Q8: ¿Sirve para trasladar personas o mercancías?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Está relacionado con el transporte aéreo?")
                if r == "s":
                    r2 = pedir_si_no("Q10: ¿Es para aviones comerciales con pistas y terminales grandes?")
                    if r2 == "s":
                        print("¡Pensaste en un aeropuerto!")
                    else:
                        r3 = pedir_si_no("Q11: ¿Es para helicópteros o vuelos pequeños?")
                        if r3 == "s":
                            print("¡Pensaste en un helipuerto!")
                        else:
                            print("¡Pensaste en otra instalación aérea!")
                else:
                    r = pedir_si_no("Q12: ¿Está relacionado con transporte acuático?")
                    if r == "s":
                        r2 = pedir_si_no("Q13: ¿Permite embarcar y desembarcar barcos grandes, ferris o barcos de carga?")
                        if r2 == "s":
                            print("¡Pensaste en un puerto o muelle!")
                        else:
                            r3 = pedir_si_no("Q14: ¿Es para pasajeros pequeños, ferrys o transporte local?")
                            if r3 == "s":
                                print("¡Pensaste en una estación de ferry!")
                            else:
                                print("¡Pensaste en otra instalación acuática!")
                    else:
                        r = pedir_si_no("Q15: ¿Está relacionado con transporte terrestre?")
                        if r == "s":
                            r2 = pedir_si_no("Q16: ¿Es una vía de tránsito, carretera o autopista?")
                            if r2 == "s":
                                r3 = pedir_si_no("Q17: ¿Tiene pasos elevados, viaductos o túneles?")
                                if r3 == "s":
                                    r4 = pedir_si_no("Q18: ¿Es solo para peatones?")
                                    if r4 == "s":
                                        print("¡Pensaste en un paso peatonal elevado o subterráneo!")
                                    else:
                                        print("¡Pensaste en un viaducto o túnel!")
                                else:
                                    print("¡Pensaste en una carretera o autopista!")
                            else:
                                r3 = pedir_si_no(
                                    "Q19: ¿Es un puente que conecta dos zonas separadas por agua o terreno?")
                                if r3 == "s":
                                    print("¡Pensaste en un puente!")
                                else:
                                    print("¡Pensaste en un estacionamiento/estacion/!")
            else:
                r = pedir_si_no("Q9: ¿Tiene valor histórico, cultural o religioso?")
                if r == "s":
                    r2 = pedir_si_no("Q10: ¿Es una construcción antigua reconocida por su historia o arquitectura?")
                    if r2 == "s":
                        r3 = pedir_si_no("Q11: ¿Está asociado con ceremonias religiosas o rituales?")
                        if r3 == "s":
                            print("¡Pensaste en un templo o lugar de culto!")
                        else:
                            r4 = pedir_si_no(
                                "Q12: ¿Es una estructura monumental de gran tamaño, visible en la ciudad o región?")
                            if r4 == "s":
                                print("¡Pensaste en una pirámide, castillo o monumento histórico!")
                            else:
                                print("¡Pensaste en una escultura pública o monumento menor!")
                else:
                    # Lugares de ocio o deporte
                    r2 = pedir_si_no("Q10: ¿Se utiliza para actividades deportivas?")
                    if r2 == "s":
                        r3 = pedir_si_no(
                            "Q11: ¿Se practica principalmente un deporte colectivo en él (fútbol, baloncesto, etc.)?")
                        if r3 == "s":
                            print("¡Pensaste en un estadio o arena!")
                        else:
                            r4 = pedir_si_no(
                                "Q12: ¿Se utiliza para deportes individuales o específicos (natación, patinaje, golf, ciclismo)?")
                            if r4 == "s":
                                r5 = pedir_si_no("Q13: ¿Es al aire libre y con circuitos o pistas largas?")
                                if r5 == "s":
                                    r6 = pedir_si_no("Q14: ¿Se usa para carreras de autos o motos?")
                                    if r6 == "s":
                                        print("¡Pensaste en un autódromo o circuito de carreras!")
                                    else:
                                        r7 = pedir_si_no("Q15: ¿Es para ciclismo o carreras de bicicletas?")
                                        if r7 == "s":
                                            print("¡Pensaste en un velódromo!")
                                        else:
                                            r8 = pedir_si_no("Q16: ¿Es un campo con césped y hoyos?")
                                            if r8 == "s":
                                                print("¡Pensaste en un campo de golf!")
                                            else:
                                                print("¡Pensaste en otra instalación deportiva individual!")
                                else:
                                    r5 = pedir_si_no("Q17: ¿Es un gimnasio, polideportivo o pista cubierta?")
                                    if r5 == "s":
                                        print("¡Pensaste en un gimnasio o polideportivo!")
                                    else:
                                        r6 = pedir_si_no("Q18: ¿Es una piscina pública o acuaparque?")
                                        if r6 == "s":
                                            print("¡Pensaste en una piscina pública o acuaparque!")
                                        else:
                                            r7 = pedir_si_no("Q19: ¿Es una pista de patinaje o skatepark?")
                                            if r7 == "s":
                                                print("¡Pensaste en pista de patinaje o skatepark!")
                                            else:
                                                print("¡Pensaste en otra instalación deportiva!")
                    else:
                        r3 = pedir_si_no("Q11: ¿Se utiliza para entretenimiento o recreación?")
                        if r3 == "s":
                            r4 = pedir_si_no("Q12: ¿Es al aire libre y con atracciones mecánicas o temáticas?")
                            if r4 == "s":
                                print("¡Pensaste en parque de diversiones o parque temático!")
                            else:
                                r5 = pedir_si_no("Q13: ¿Sirve para espectáculos, cine o teatro?")
                                if r5 == "s":
                                    r6 = pedir_si_no("Q14: ¿Es al aire libre?")
                                    if r6 == "s":
                                        print("¡Pensaste en teatro al aire libre o anfiteatro!")
                                    else:
                                        print("¡Pensaste en cine o teatro cerrado!")
                                else:
                                    r6 = pedir_si_no(
                                        "Q15: ¿Es un centro de entretenimiento, zoológico, acuario o jardín botánico?")
                                    if r6 == "s":
                                        print("¡Pensaste en zoológico, acuario, jardín botánico o centro de ocio!")
                                    else:
                                        print("¡Pensaste en otra instalación recreativa o de entretenimiento!")
        return






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
        return

    # Q3
    r = pedir_si_no("Q3: ¿Es un lugar o una construcción (por ejemplo: ciudad, montaña, edificio, río, etc)?")
    if r == "s":
        rama_lugares()
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
