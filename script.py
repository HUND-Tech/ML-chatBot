
#--------------------------------------------  RAMAS PRINCIPALES --------------------------------------------#
def rama_abstracto():
    """Rama para conceptos abstractos e intangibles"""
    print("\n--- CATEGORÍA: ABSTRACTOS/INTANGIBLES ---")
    
    # EMOCIONES Y SENTIMIENTOS
    r = pedir_si_no("Q3: ¿Está relacionado con emociones o sentimientos?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una emoción positiva?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Se siente hacia otras personas?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Afecto profundo?")
                if r == "s":
                    print("EMOCIÓN: amor")
                else:
                    r = pedir_si_no("Q7: ¿Implica agradecimiento hacia otro?")
                    if r == "s":
                        print("EMOCIÓN: gratitud")
                    else:
                        r = pedir_si_no("Q8: ¿Es admiración hacia alguien o algo?")
                        if r == "s":
                            print("EMOCIÓN: respeto")
                        else:
                            r = pedir_si_no("Q9: ¿Es entusiasmo o motivación?")
                            if r == "s":
                                print("EMOCIÓN: entusiasmo")
                            else:
                                print("EMOCIÓN POSITIVA GENERAL: felicidad/placer")
            else:
                r = pedir_si_no("Q6: ¿Es expectativa positiva hacia el futuro?")
                if r == "s":
                    print("EMOCIÓN: esperanza")
                else:
                    r = pedir_si_no("Q7: ¿Es sensación de paz y armonía?")
                    if r == "s":
                        print("EMOCIÓN: serenidad")
                    else:
                        print("EMOCIÓN POSITIVA GENERAL: placer, satisfacción, bienestar")
        else:
            # EMOCIONES NEGATIVAS
            r = pedir_si_no("Q5: ¿Involucra a otras personas?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Se relaciona con la comparación?")
                if r == "s":
                    r = pedir_si_no("Q7: ¿Es envidia o celos?")
                    if r == "s":
                        print("EMOCIÓN NEGATIVA: envidia")
                    else:
                        r = pedir_si_no("Q8: ¿Es más una emoción de juicio social?")
                        if r == "s":
                            print("EMOCIÓN NEGATIVA: Vergüenza o humillación")
                else:
                    r = pedir_si_no("Q7: ¿Puede provocar llanto y malestar?")
                    if r == "s":
                        print("EMOCIÓN NEGATIVA: Tristeza")
                    else:
                        r = pedir_si_no("Q8: ¿Causa irritación intensa?")
                        if r == "s":
                            print("EMOCIÓN NEGATIVA: Enojo, odio o ira")
                        else:
                            r = pedir_si_no("Q9: ¿Es una respuesta ante una amenaza?")
                            if r == "s":
                                r = pedir_si_no("Q10: ¿La amenaza es un peligro presente, claro y conocido?")
                                if r == "s":
                                    print("EMOCIÓN NEGATIVA: miedo")
                                else:
                                    print("EMOCIÓN NEGATIVA: ansiedad")
            else:
                r = pedir_si_no("Q6: ¿Se relaciona con el pasado?")
                if r == "s":
                    r = pedir_si_no("Q7: ¿Tiene que ver con recordar momentos buenos?")
                    if r == "s":
                        print("EMOCIÓN NEGATIVA: Nostalgia")
                    else:
                        r = pedir_si_no("Q8: ¿Surge del remordimiento?")
                        if r == "s":
                            print("EMOCIÓN NEGATIVA: Culpa")
        return

    # CONCEPTOS MATEMÁTICOS
    r = pedir_si_no("Q3: ¿Es un concepto matemático o numérico?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es un número específico?")
        if r == "s":
            print("NÚMEROS: enteros, decimales, fracciones, números primos, π, e, etc")
        else:
            r = pedir_si_no("Q5: ¿Es una operación matemática?")
            if r == "s":
                print("OPERACIONES: suma, resta, multiplicación, división, potencia, raíz, integral, derivada")
            else:
                r = pedir_si_no("Q6: ¿Se relaciona con magnitudes y medidas?")
                if r == "s":
                    print("MAGNITUDES: Longitud, área, volumen")
                else:
                    r = pedir_si_no("Q7: ¿Es una rama de las matemáticas?")
                    if r == "s":
                        print("RAMA MATEMÁTICA: Álgebra, geometría, trigonometría, probabilidad, estadística, cálculo")
        return

    # IDEAS FILOSÓFICAS / CONCEPTOS ABSTRACTOS
    r = pedir_si_no("Q3: ¿Es una idea filosófica o concepto abstracto?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Está relacionado con la existencia o la realidad?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Se refiere al mero hecho de existir?")
            if r == "s":
                print("ABSTRACTO: Existencia, Ser")
            else:
                r = pedir_si_no("Q6: ¿Es lo opuesto (ausencia total)?")
                if r == "s":
                    print("ABSTRACTO: Nada")
                else:
                    r = pedir_si_no("Q7: ¿Se refiere a la existencia real y efectiva de algo?")
                    if r == "s":
                        print("ABSTRACTO: Realidad")
                    else:
                        r = pedir_si_no("Q8: ¿Es el estado de conocimiento de la realidad interna?")
                        if r == "s":
                            print("ABSTRACTO: Consciencia")
        else:
            r = pedir_si_no("Q5: ¿Se relaciona con las Dimensiones Universales?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Es una medida continua?")
                if r == "s":
                    print("DIMENSIONES: Tiempo")
                else:
                    r = pedir_si_no("Q7: ¿Es la extensión que ocupa un objeto?")
                    if r == "s":
                        print("DIMENSIONES: Espacio")
        return

    # CONCEPTOS TEMPORALES
    r = pedir_si_no("Q3: ¿Está relacionado con el tiempo?")
    if r == "s":
        print("CONCEPTOS TEMPORALES: tiempo, eternidad, momento, pasado, presente, futuro, ciclo, destino")
        return

    # CONCEPTOS ESPIRITUALES / RELIGIOSOS
    r = pedir_si_no("Q3: ¿Es un concepto espiritual o religioso?")
    if r == "s":
        print("CONCEPTOS ESPIRITUALES: alma, fe, dios, karma, nirvana, reencarnación, infierno, cielo, pecado")
        return

    # CUALIDADES MORALES / VALORES
    r = pedir_si_no("Q3: ¿Se trata de una cualidad moral?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Se enfoca en cómo tratamos a los demás?")
        if r == "s":
            print("VALOR: Amistad, solidaridad, empatía")
        else:
            r = pedir_si_no("Q5: ¿Se refiere a lo que consideramos correcto o justo?")
            if r == "s":
                print("VALOR: Justicia, igualdad") 
            else:
                r = pedir_si_no("Q6: ¿Implica apoyo o cuidado mutuo?")
                if r == "s":
                    print("VALOR: Solidaridad")
        return

    # CONCEPTOS LÓGICOS
    r = pedir_si_no("Q3: ¿Es un concepto lógico, relacionado con la verdad o el razonamiento?")   
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una cualidad de una proposición?")
        if r == "s":
            print("CONCEPTO: verdad, falsedad")
        else:
            r = pedir_si_no("Q5: ¿Es un fenómeno contradictorio?")
            if r == "s":
                print("CONCEPTO: Paradoja")
        return

    # IDEAS, MEMORIA Y LENGUAJE
    r = pedir_si_no("Q3: ¿Se relaciona con ideas, memoria o lenguaje?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es la capacidad de recordar?")
        if r == "s":
            print("PENSAMIENTO: Memoria, recuerdo")
        else:
            r = pedir_si_no("Q5: ¿Es una creación mental que no existe físicamente?")
            if r == "s":
                print("PENSAMIENTO: Imaginación")
            else: 
                r = pedir_si_no("Q6: ¿Es la unidad básica del lenguaje?")
                if r == "s": 
                    print("LENGUAJE: Palabra, letra, simbolo, signo")
                else:
                    r = pedir_si_no("Q7: ¿Se refiere a la capacidad de razonar o reflexionar?")
                if r == "s":
                    print("PENSAMIENTO: Pensamiento crítico, reflexión")
        return

    # ORGANIZACIÓN SOCIAL
    r = pedir_si_no("Q3: ¿Está ligado a cómo se organiza la sociedad o en las personas entre sí?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es la capacidad de decidir por uno mismo?")
        if r == "s":
            print("SOCIAL: Libertad")
        else:
            r = pedir_si_no("Q5: ¿Es el ejercicio de control o influencia?")
            if r == "s":
                print("SOCIAL: Poder")
            else:
                r = pedir_si_no("Q6: ¿Es el aprecio que uno tiene por sí mismo?")
                if r == "s":
                    print("SOCIAL: Amor propio, autoestima, dignidad")
                else:
                    r = pedir_si_no("Q7: ¿Se refiere a la relación de confianza o cooperación con otros?")
                if r == "s":
                    print("SOCIAL: Confianza, cooperación, solidaridad")

        return


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
    print("Estas pensando en un lugar muy poco común")

def rama_fenomeno():
    
    r = pedir_si_no("Q3: ¿Es un FENÓMENO NATURAL observable?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es METEOROLÓGICO/ATMOSFÉRICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con la PRECIPITACIÓN?")
            if r == "s":
                print("METEOROLÓGICOS · PRECIPITACIÓN: lluvia, nieve, granizo, aguanieve, rocío")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con el VIENTO?")
            if r == "s":
                print("METEOROLÓGICOS · VIENTO: brisa, ventisca, huracán, tornado, tifón, ciclón")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con FENÓMENOS ELÉCTRICOS?")

            if r == "s":
                print("METEOROLÓGICOS · ELÉCTRICOS: rayo, relámpago, trueno, tormenta eléctrica")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con TEMPERATURA?")
            if r == "s":
                print("METEOROLÓGICOS · TÉRMICOS: calor, frío, ola de calor, helada, punto de rocío")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con EFECTOS ÓPTICOS?")
            if r == "s":
                print("METEOROLÓGICOS · ÓPTICOS: arcoíris, halo, espejismo, parhelio, corona solar")
                return
            print("METEOROLÓGICOS · PRESIÓN: alta presión, baja presión, frente climático")
            return
        
        r = pedir_si_no("Q4: ¿Es GEOLÓGICO/TERRESTRE?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con SISMOS o movimiento terrestre?")
            if r == "s":
                print("GEOLÓGICOS · SÍSMICOS: terremoto, temblor, tsunami, maremoto")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con VOLCANES?")
            if r == "s":
                print("GEOLÓGICOS · VOLCÁNICOS: erupción, lava, ceniza, fumarola, magma")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con EROSIÓN/DERRUMBES?")
            if r == "s":
                print("GEOLÓGICOS · EROSIÓN: deslizamiento, avalancha, derrumbe, alud")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con FORMACIÓN del relieve?")
            if r == "s":
                print("GEOLÓGICOS · FORMACIÓN: montañas, valles, cañones, placas tectónicas")
                return
            print("GEOLÓGICOS · SUBSUELO: magma, mineralización, géiser, termal")
            return
        
        r = pedir_si_no("Q4: ¿Es HIDROLÓGICO/ACUÁTICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con MAREAS?")
            if r == "s":
                print("HIDROLÓGICOS · MAREAS: marea alta, marea baja, maremoto")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con CORRIENTES?")
            if r == "s":
                print("HIDROLÓGICOS · CORRIENTES: corriente marina, corriente fluvial, remolino")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con OLAS/MAR?")
            if r == "s":
                print("HIDROLÓGICOS · OLAS: olas, tsunami, marejada, resaca")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con el CICLO DEL AGUA?")
            if r == "s":
                print("HIDROLÓGICOS · CICLO DEL AGUA: evaporación, condensación, precipitación, escorrentía")
                return
            print("HIDROLÓGICOS · ESTADOS/EVENTOS: congelación, deshielo, inundación, sequía")
            return
        
        r = pedir_si_no("Q4: ¿Es ASTRONÓMICO/ESPACIAL?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Se refiere al ESPACIO/medio?")
            if r == "s":
                print("ASTRONÓMICOS · ESPACIO: vacío cósmico, medio interestelar, gravedad cero")
                return
            r = pedir_si_no("Q5: ¿Se refiere a CUERPOS/EVENTOS orbitales?")
            if r == "s":
                print("ASTRONÓMICOS · CUERPOS: planetas, sol, luna, estrellas")
                return
            r = pedir_si_no("Q5: ¿Es un EVENTO astrofísico?")
            if r == "s":
                print("ASTRONÓMICOS · EVENTOS: supernova, agujero negro, nebulosa, galaxia")
                return
            r = pedir_si_no("Q5: ¿Es un FENÓMENO LUMINOSO?")
            if r == "s":
                print("ASTRONÓMICOS · LUMINOSOS: aurora boreal, luz zodiacal, lluvia de estrellas")
                return
            print("ASTRONÓMICOS · ORBITALES: rotación, traslación, perihelio, afelio")
            return
        
        r = pedir_si_no("Q4: ¿Es BIOLÓGICO/ECOLÓGICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con CICLOS biológicos?")
            if r == "s":
                print("BIOLÓGICOS · CICLOS: fotosíntesis, respiración, descomposición")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con COMPORTAMIENTOS?")
            if r == "s":
                print("BIOLÓGICOS · COMPORTAMIENTO: migración, hibernación, estivación, eclosión")
                return
            r = pedir_si_no("Q5: ¿Es un FENÓMENO ECOLÓGICO?")
            if r == "s":
                print("BIOLÓGICOS · ECOLÓGICOS: sucesión, simbiosis, depredación, competencia")
                return
            print("BIOLÓGICOS · BIOLUMINISCENCIA: luz natural en seres vivos")
            return
        
        print("NADA")
        return
    
   
    r = pedir_si_no("Q3: ¿Es una FORMA DE ENERGÍA?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es TÉRMICA?")
        if r == "s":
            print("ENERGÍA · TÉRMICA: calor, temperatura, conducción, convección, radiación")
            return
        r = pedir_si_no("Q4: ¿Es ELÉCTRICA?")
        if r == "s":
            print("ENERGÍA · ELÉCTRICA: electricidad, corriente, voltaje, resistencia, circuito")
            return
        r = pedir_si_no("Q4: ¿Es MAGNÉTICA?")
        if r == "s":
            print("ENERGÍA · MAGNÉTICA: magnetismo, campo magnético, electromagnetismo")
            return
        r = pedir_si_no("Q4: ¿Es LUMINOSA/RADIANTE?")
        if r == "s":
            print("ENERGÍA · LUMINOSA/RADIANTE: luz, fotones, espectro electromagnético, radiación")
            return
        r = pedir_si_no("Q4: ¿Es SONORA?")
        if r == "s":
            print("ENERGÍA · SONORA: sonido, onda sonora, eco, resonancia, ultrasonido")
            return
        r = pedir_si_no("Q4: ¿Es MECÁNICA?")
        if r == "s":
            print("ENERGÍA · MECÁNICA: movimiento, fuerza, trabajo, potencia, cinética, potencial")
            return
        r = pedir_si_no("Q4: ¿Es QUÍMICA?")
        if r == "s":
            print("ENERGÍA · QUÍMICA: reacción química, combustión, oxidación, fermentación")
            return
        r = pedir_si_no("Q4: ¿Es NUCLEAR?")
        if r == "s":
            print("ENERGÍA · NUCLEAR: fisión, fusión, radiactividad, desintegración")
            return
        print("ENERGÍA · CONCEPTOS COSMOLÓGICOS: energía oscura, materia oscura")
        return
    
    
    r = pedir_si_no("Q3: ¿Es un FENÓMENO FÍSICO?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Está relacionado con la ESTRUCTURA ATÓMICA?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Con ÁTOMOS?")
            if r == "s":
                print("FÍSICOS · ÁTOMOS: protones, neutrones, electrones")
                return
            r = pedir_si_no("Q5: ¿Con PARTÍCULAS subatómicas?")
            if r == "s":
                print("FÍSICOS · PARTÍCULAS: quark, leptón, bosón, hadrón")
                return
            r = pedir_si_no("Q5: ¿Con ESTADOS exóticos?")
            if r == "s":
                print("FÍSICOS · ESTADOS: plasma, condensado Bose-Einstein")
                return
            print("FÍSICOS · INTERACCIONES: fuerza nuclear fuerte/débil")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con los ESTADOS DE LA MATERIA?")
        if r == "s":
            r = pedir_si_no("Q5: ¿SÓLIDO?")
            if r == "s":
                print("FÍSICOS · SÓLIDO: cristalino, amorfo, polímero")
                return
            r = pedir_si_no("Q5: ¿LÍQUIDO?")
            if r == "s":
                print("FÍSICOS · LÍQUIDO: viscoso, fluido, superfluido")
                return
            r = pedir_si_no("Q5: ¿GASEOSO?")
            if r == "s":
                print("FÍSICOS · GASEOSO: comprimido, ideal, real")
                return
            print("FÍSICOS · PLASMA: ionizado, conductor")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con las FUERZAS FUNDAMENTALES?")
        if r == "s":
            r = pedir_si_no("Q5: ¿GRAVEDAD?")
            if r == "s":
                print("FÍSICOS · GRAVEDAD: atracción, curvatura del espaciotiempo")
                return
            r = pedir_si_no("Q5: ¿ELECTROMAGNETISMO?")
            if r == "s":
                print("FÍSICOS · ELECTROMAGNETISMO: campos electromagneticos, luz, electricidad, magnetismo")
                return
            r = pedir_si_no("Q5: ¿NUCLEAR FUERTE?")
            if r == "s":
                print("FÍSICOS · NUCLEAR FUERTE: núcleos atómicos, hadrones")
                return
            print("FÍSICOS · NUCLEAR DÉBIL: desintegración radiactiva")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con FENÓMENOS CUÁNTICOS?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Dualidad ONDA-PARTÍCULA?")
            if r == "s":
                print("CUÁNTICOS · DUALIDAD: onda-partícula")
                return
            r = pedir_si_no("Q5: ¿Principios (incertidumbre/exclusión)?")
            if r == "s":
                print("CUÁNTICOS · PRINCIPIOS: incertidumbre, exclusión")
                return
            r = pedir_si_no("Q5: ¿ENTRELAZAMIENTO?")
            if r == "s":
                print("CUÁNTICOS · ENTRELAZAMIENTO: no-localidad")
                return
            print("CUÁNTICOS · TÚNELES: efecto túnel")
            return
        
        print("FENÓMENO FÍSICO FUNDAMENTAL NO ESPECIFICADO")
        return
    
    
    r = pedir_si_no("Q3: ¿Es un FENÓMENO QUÍMICO?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una REACCIÓN?")
        if r == "s":
            print("QUÍMICOS · REACCIONES: síntesis, descomposición, sustitución, combustión")
            return
        r = pedir_si_no("Q4: ¿Es un EQUILIBRIO/INTERACCIÓN?")
        if r == "s":
            print("QUÍMICOS · EQUILIBRIOS: químico, ácido-base, redox, solubilidad")
            return
        r = pedir_si_no("Q4: ¿Tiene que ver con ESTADOS dispersos?")
        if r == "s":
            print("QUÍMICOS · ESTADOS: coloide, suspensión, emulsión, solución")
            return
        print("QUÍMICOS · PROPIEDADES: pH, conductividad, reactividad, catálisis")
        return
    
    
    r = pedir_si_no("Q3: ¿Es un FENÓMENO SOCIAL o HUMANO?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Se refiere a GLOBALIZACIÓN?")
        if r == "s":
            print("SOCIALES · GLOBALIZACIÓN: económica, cultural, tecnológica")
            return
        r = pedir_si_no("Q4: ¿Se refiere a MIGRACIÓN?")
        if r == "s":
            print("SOCIALES · MIGRACIÓN: humana, animal, patrones")
            return
        r = pedir_si_no("Q4: ¿Se refiere a TENDENCIAS?")
        if r == "s":
            print("SOCIALES · TENDENCIAS: moda, pensamiento, comportamiento colectivo")
            return
        print("SOCIALES · REVOLUCIONES: industrial, tecnológica, social")
        return
    
    print("FENÓMENO/ENERGÍA NO CLASIFICADO")

def rama_objeto():
    r = pedir_si_no("Q7: ¿Es un objeto natural?")
    if r == "s":
        obj_natural()
        return
    r = pedir_si_no("Q8: ¿Es un objeto crado con intervención humana?")
    if r == "s":
        obj_artificial()
        return
    r = pedir_si_no("Q9: ¿Es un producto de consumo?")
    if r == "s":
        producto_consumo()
        return
    r = pedir_si_no("Q10: ¿Es un residuo o desecho?")
    if r == "s":
        residuos()
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
            r = pedir_si_no("Q6: ¿Es pequeño (menos de 50cm de longitud, ej.raton)?")
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

        r = pedir_si_no("Q7: ¿Vive principalmente en agua?")
        if r == "s":
            r = pedir_si_no("Q8: ¿Es pequeño y ornamental?")
            if r == "s":
                print("Pez ornamental doméstico (goldfish, guppy, betta).")
            else:
                print("Pez doméstico.")
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
                            r = pedir_si_no("Q11: ¿Tiene pico muy grande y colorido?")
                            if r == "s":
                                print("Identificado: Tucán")
                            else:
                                r = pedir_si_no("Q12: ¿Tiene cola muy vistosa en forma de abanico?")
                                if r == "s":
                                    print("Identificado: Pavo real")
                                else:
                                    r=pedir_si_no("Q13: ¿Puede volar hacia atras?")
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
            r = pedir_si_no("Q8: ¿Es de color amarillo o verde fuerte por fuera?")
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
                        print("¡Pensaste en un maracuyá/kiwi!")
                    else:
                        print("Podría ser otra fruta cítrica menos común como kiwi.")
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
                                print("Pensaste en un fruta roja poco conocida")
        else:
            # No es roja
            r = pedir_si_no("Q9: ¿Es una fruta grande?")  #corregir linea
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
            print("Pensaste en una flore o arboles decorativos")
        else:
            r=pedir_si_no("Q6: ¿Se usa con fines medicinales o industriales?")
            if r == "s":
                print("pensaste en Manzanilla/Sabila ")
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

def obj_natural():#Q7
    
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

def obj_artificial():#Q8
    
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
    elif pedir_si_no("Q5: ¿Se lleva puesto en el cuerpo?") == "s":
        
        r = pedir_si_no("Q6: ¿Se lleva en los pies?")
        if r == "s":
            
            # calzado
            r = pedir_si_no("Q7: ¿Es utilizado comúnmente como calzado formal?")
            if r == "s":
                print("Zapatos")
            else:
                r = pedir_si_no("Q8: ¿Es utilizado principalmente para deporte o ejercicio?")
                if r == "s":
                    print("Tenis")
                else:
                    r = pedir_si_no("Q9: ¿Al usarlo se ven los dedos de los pies?")
                    if r == "s":
                        print("Sandalias")
                    else:
                        print("Botas")
        else:
            r = pedir_si_no("Q7: ¿Cubre el torso o las piernas?")
            if r == "s":
                
                # vestimenta
                r = pedir_si_no("Q8: ¿Es ropa interior?")
                if r == "s":
                    r = pedir_si_no("Q9: ¿Es para la parte superior del cuerpo?")
                    if r == "s":
                        print("Sostén/Camiseta interior")
                    else:
                        print("Calzones/Boxers")
                else:
                    r = pedir_si_no("Q9: ¿Es para nadar o la playa?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Es de una sola pieza?")
                        if r == "s":
                            print("Traje de baño")
                        else:
                            print("Un bikini")
                    else:
                        r = pedir_si_no("Q10: ¿Se puede colocar encima de otra ropa?")
                        if r == "s":
                            r = pedir_si_no("Q11: ¿Tiene mangas?")
                            if r == "s":
                                r = pedir_si_no("Q12: ¿Es muy largo y amplio?")
                                if r == "s":
                                    print("Abrigo")
                                else:
                                    print("Chamarra")
                            else:
                                print("Chaleco")
                        else:
                            r = pedir_si_no("Q11: ¿Cubre las piernas?")
                            if r == "s":
                                r = pedir_si_no("Q12: ¿Cubre hasta los tobillos?")
                                if r == "s":
                                    print("Pantalón")
                                else:
                                    print("Short")
                            else:
                                r = pedir_si_no("Q12: ¿Tiene mangas?")
                                if r == "s":
                                    r = pedir_si_no("Q13: ¿Es formal?")
                                    if r == "s":
                                        print("Camisa")
                                    else:
                                        r = pedir_si_no("Q14: ¿Es típicamente femenina?")
                                        if r == "s":
                                            print("Blusa")
                                        else:
                                            print("Playera")
                                else:
                                    print("Vestido")
            else:
                
               # accesorios
                r = pedir_si_no("Q8: ¿Se lleva en la cabeza?")
                if r == "s":
                    r = pedir_si_no("Q9: ¿Protege del sol o lluvia?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Tiene visera")
                        if r == "s":
                            print("Gorra/Sombrero")
                        else:
                            print("Capucha")
                    else:
                        r = pedir_si_no("Q10: ¿Ayuda a ver mejor?")
                        if r == "s":
                            r = pedir_si_no("Q11: ¿Protege del sol?")
                            if r == "s":
                                print("Gafas de sol")
                            else:
                                print("Lentes")
                        else:
                            r = pedir_si_no("Q11: ¿Es decorativo o para el cabello?")
                            if r == "s":
                                print("Diadema/Banda")
                            else:
                                print("Casco")
                else:
                    r = pedir_si_no("Q9: ¿Se lleva en las orejas?")
                    if r == "s":
                        print("Aretes/Pendientes")
                    else:
                        r = pedir_si_no("Q10: ¿Se lleva en el cuello?")
                        if r == "s":
                            r = pedir_si_no("Q11: ¿Es para abrigarse?")
                            if r == "s":
                                print("Bufanda")
                            else:
                                r = pedir_si_no("Q12: ¿Es de metal o joyería?")
                                if r == "s":
                                    print("Collar")
                                else:
                                    print("Corbata")
                        else:
                            r = pedir_si_no("Q11: ¿Se lleva en las manos o muñecas?")
                            if r == "s":
                                r = pedir_si_no("Q12: ¿Muestra la hora?")
                                if r == "s":
                                    print("Reloj")
                                else:
                                    r = pedir_si_no("Q13: ¿Es joyería decorativa?")
                                    if r == "s":
                                        print("Pulsera/Anillo")
                                    else:
                                        print("Guantes")
                            else:
                                r = pedir_si_no("Q12: ¿Se lleva en la cintura?")
                                if r == "s":
                                    print("Cinturón")
                                else:
                                    print("Otro accesorio")
    
    # VEHÍCULOS Y MEDIOS DE TRANSPORTE
    elif pedir_si_no("Q6: ¿Se usa para transportarse?") == "s":
        
        r = pedir_si_no("Q7: ¿Se mueve por tierra?")
        if r == "s":
            
            # terrestres
            r = pedir_si_no("Q8: ¿Tiene motor?")
            if r == "s":
                r = pedir_si_no("Q9: ¿Tiene cuatro ruedas?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Es para muchas personas?")
                    if r == "s":
                        r = pedir_si_no("Q11: ¿Es para más de 20 personas)?")
                        if r == "s":
                            print("Autobús")
                        else:
                            print("Camioneta/Van")
                    else:
                        r = pedir_si_no("Q11: ¿Es para carga?")
                        if r == "s":
                            print("Camión")
                        else:
                            print("Carro")
                else:
                    r = pedir_si_no("Q10: ¿Tiene ruedas?")
                    if r == "s":
                        print("Motocicleta")
                    else:
                        print("Tren")
            else:
                r = pedir_si_no("Q9: ¿Tiene ruedas?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Tiene pedales?")
                    if r == "s":
                        print("Bicicleta")
                    else:
                        print("Patineta/Scooter")
                else:
                    print("Patines")
        else:
            r = pedir_si_no("Q8: ¿Se mueve por el aire?")
            if r == "s":
                
                # aéreos
                r = pedir_si_no("Q9: ¿Tiene motor?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Es para MUCHAS personas?")
                    if r == "s":
                        print("Avión")
                    else:
                        r = pedir_si_no("Q11: ¿Tiene hélices?")
                        if r == "s":
                            print("Helicóptero")
                        else:
                            print("Avioneta")
                else:
                    r = pedir_si_no("Q10: ¿Usa aire caliente?")
                    if r == "s":
                        print("Globo aerostático")
                    else:
                        print("Planeador")
            else:
                
                # acuáticos
                r = pedir_si_no("Q9: ¿Tiene motor?")
                if r == "s":
                    r = pedir_si_no("Q10: ¿Tiene capacidad como para 10 personas o más?")
                    if r == "s":
                        r = pedir_si_no("Q11: ¿Es de dimensiones MUY grandes?")
                        if r == "s":
                            print("Barco/Ferry")
                        else:
                            print("Yate")
                    else:
                        print("Lancha")
                else:
                    r = pedir_si_no("Q10: ¿Usa remos?")
                    if r == "s":
                        r = pedir_si_no("Q11: ¿Es para una persona?")
                        if r == "s":
                            print("Kayak")
                        else:
                            print("Canoa/Bote")
                    else:
                        print("Velero")
    # MUEBLES
    elif pedir_si_no("Q4: ¿Es un mueble?") == "s":
        
        r = pedir_si_no("Q5: ¿Se usa principalmente para sentarse?")
        if r == "s":
            
            # asientos
            r = pedir_si_no("Q6: ¿Es para una sola persona?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Tiene respaldo?")
                if r == "s":
                    r = pedir_si_no("Q8: ¿Tiene brazos?")
                    if r == "s":
                        print("Sillón")
                    else:
                        print("Silla")
                else:
                    print("Taburete")
            else:
                print("Sofá")
        else:
            
            # almacenamiento
            r = pedir_si_no("Q6: ¿Tiene superficie plana para trabajar?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Tiene cajones?")
                if r == "s":
                    print("Escritorio")
                else:
                    print("Mesa")
            else:
                r = pedir_si_no("Q8: ¿Tiene puertas?")
                if r == "s":
                    print("Armario")
                else:
                    print("Estante")
        return
    
   # HERRAMIENTAS Y UTENSILIOS
    else:
     r = pedir_si_no("Q5: ¿Se usa para escribir o dibujar?")
    if r == "s":
        # escritura y dibujo
        r = pedir_si_no("Q6: ¿Usa tinta?")
        if r == "s":
            r = pedir_si_no("Q7: ¿Viene en varios colores?")
            if r == "s":
                r = pedir_si_no("Q8: ¿Tiene punta gruesa?")
                if r == "s":
                    print("Marcador")
                else:
                    print("Plumón")
            else:
                print("Pluma")
        else:
            r = pedir_si_no("Q7: ¿Usa grafito?")
            if r == "s":
                r = pedir_si_no("Q8: ¿Es de madera?")
                if r == "s":
                    print("Lápiz")
                else:
                    print("Lapicero")
            else:
                r = pedir_si_no("Q8: ¿Se usa para borrar?")
                if r == "s":
                    print("Goma de borrar")
                
    else:
        r = pedir_si_no("Q6: ¿Se usa en la cocina?")
        if r == "s":
            
            # utensilios de cocina
            r = pedir_si_no("Q7: ¿Se usa para cortar?")
            if r == "s":
                r = pedir_si_no("Q8: ¿Es MUY afilado?")
                if r == "s":
                    print("Cuchillo")
                else:
                    print("Tijeras de cocina")
            else:
                r = pedir_si_no("Q8: ¿Se usa para comer?")
                if r == "s":
                    r = pedir_si_no("Q9: ¿Tiene dientes/púas?")
                    if r == "s":
                        print("Tenedor")
                    else:
                        r = pedir_si_no("Q10: ¿Es cóncavo?")
                        if r == "s":
                            print("Cuchara")
                        else:
                            print("Cuchillo de mesa")
                else:
                    r = pedir_si_no("Q9: ¿Se usa para cocinar/preparar?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Tiene mango largo?")
                        if r == "s":
                            print("Espátula/Cuchara de cocina")
                        else:
                            print("Abrelatas")
                    else:
                        print("Plato/Tazón")
        else:
            r = pedir_si_no("Q7: ¿Se usa para reparar o construir?")
            if r == "s":
                
                # herramientas de trabajo
                r = pedir_si_no("Q8: ¿Se usa para golpear?")
                if r == "s":
                    r = pedir_si_no("Q9: ¿Tiene cabeza de metal?")
                    if r == "s":
                        print("Martillo")
                    else:
                        print("Mazo")
                else:
                    r = pedir_si_no("Q9: ¿Se usa para apretar o aflojar?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Tiene forma de cruz?")
                        if r == "s":
                            print("Destornillador")
                        else:
                            print("Llave inglesa")
                    else:
                        r = pedir_si_no("Q10: ¿Se usa para cortar?")
                        if r == "s":
                            r = pedir_si_no("Q11: ¿Tiene dientes?")
                            if r == "s":
                                print("Sierra")
                            else:
                                print("Tijeras")
                        else:
                            print("Pinzas")
            else:
                r = pedir_si_no("Q8: ¿Se usa para limpiar?")
                if r == "s":
                    
                    # herramientas de limpieza
                    r = pedir_si_no("Q9: ¿Tiene cerdas o fibras?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Tiene mango largo?")
                        if r == "s":
                            print("Escoba")
                        else:
                            print("Cepillo de limpieza")
                    else:
                        r = pedir_si_no("Q10: ¿Absorbe líquidos?")
                        if r == "s":
                            print("Esponja/Trapo")
                        else:
                            print("Recogedor")
                else:
                    r = pedir_si_no("Q9: ¿Se usa para medir?")
                    if r == "s":
                        r = pedir_si_no("Q10: ¿Mide longitud?")
                        if r == "s":
                            print("Regla/Metro")
                        else:
                            print("Balanza/Báscula")
                    else:
                        print("Otro utensilio")

def producto_consumo():#9 
    
    # PRODUCTOS DE CONSUMO
    r = pedir_si_no("Q10: ¿Es comestible o bebible?")
    if r == "s":
        
        # ALIMENTOS Y BEBIDAS
        r = pedir_si_no("Q11: ¿Es líquido?")
        if r == "s":
            
            # bebidas
            r = pedir_si_no("Q12: ¿Contiene alcohol?")
            if r == "s":
                r = pedir_si_no("Q13: ¿Es destilado?")
                if r == "s":
                    r = pedir_si_no("Q14: ¿Es transparente?")
                    if r == "s":
                        print("Vodka/Tequila")
                    else:
                        print("Whisky/Ron")
                else:
                    r = pedir_si_no("Q14: ¿Es espumoso?")
                    if r == "s":
                        print("Cerveza/Champagne")
                    else:
                        print("Vino")
            else:
                r = pedir_si_no("Q13: ¿Normalmente está caliente?")
                if r == "s":
                    r = pedir_si_no("Q14: ¿Contiene cafeína?")
                    if r == "s":
                        print("Café")
                    else:
                        print("Té/Chocolate caliente")
                else:
                    r = pedir_si_no("Q14: ¿Es gaseoso?")
                    if r == "s":
                        r = pedir_si_no("Q15: ¿Es dulce?")
                        if r == "s":
                            print("Refresco")
                        else:
                            print("Agua mineral")
                    else:
                        r = pedir_si_no("Q15: ¿Es de origen animal?")
                        if r == "s":
                            print("Leche")
                        else:
                            r = pedir_si_no("Q16: ¿Su líquido proviene de una fruta?")
                            if r == "s":
                                print("Jugo")
                            else:
                                print("Agua (como bebida)")
        else:
            
            # alimentos sólidos
            r = pedir_si_no("Q3: ¿Es dulce?")
            if r == "s":
                r = pedir_si_no("Q4: ¿Es procesado?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Se hornea?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Tiene relleno?")
                        if r == "s":
                            print("Pastel/Dona")
                        else:
                            print("Galleta/Pan dulce")
                    else:
                        r = pedir_si_no("Q6: ¿Es de chocolate?")
                        if r == "s":
                            print("Chocolate")
                        else:
                            print("Caramelo/Gomita/Dulce")
                else:
                    r = pedir_si_no("Q5: ¿Crece en árbol?")
                    if r == "s":
                        print("Fruta")
                    else:
                        print("Miel")
            else:
                r = pedir_si_no("Q4: ¿Es de origen animal?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Es carne?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Es de res?")
                        if r == "s":
                            print("Carne de res")
                        else:
                            r = pedir_si_no("Q7: ¿Es de ave?")
                            if r == "s":
                                print("Pollo/Pavo")
                            else:
                                print("Cerdo/Pescado")
                    else:
                        r = pedir_si_no("Q6: ¿Es lácteo?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Es sólido?")
                            if r == "s":
                                print("Queso")
                            else:
                                print("Yogurt")
                        else:
                            print("Huevo")
                else:
                    r = pedir_si_no("Q5: ¿Se cocina antes de comer?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Es cereal/grano?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Se hierve en agua?")
                            if r == "s":
                                print("Arroz/Pasta")
                            else:
                                print("Pan")
                    else:
                        r = pedir_si_no("Q6: ¿Es procesado?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Es salado?")
                            if r == "s":
                                print("Papas fritas/Galletas saladas")
                            else:
                                print("Cereal")
                        else:
                            print("Ensalada/Fruta")
    
    # MEDICAMENTOS Y SUPLEMENTOS
    elif pedir_si_no("Q2: ¿Es para la salud o medicina?") == "s":
        
        r = pedir_si_no("Q3: ¿Es líquido?")
        if r == "s":
            r = pedir_si_no("Q4: ¿Se toma por la boca?")
            if r == "s":
                r = pedir_si_no("Q5: ¿Es para niños principalmente?")
                if r == "s":
                    print("Jarabe infantil")
                else:
                    print("Jarabe para adultos")
            else:
                r = pedir_si_no("Q5: ¿Se aplica en la piel?")
                if r == "s":
                    print("Crema/Pomada")
                else:
                    print("Gotas para ojos/oídos")
        else:
            r = pedir_si_no("Q4: ¿Es píldora o pastilla?")
            if r == "s":
                r = pedir_si_no("Q5: ¿Es para dolor?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es de venta libre?")
                    if r == "s":
                        print("Aspirina/Paracetamol")
                    else:
                        print("Analgésico más fuerte")
                else:
                    r = pedir_si_no("Q6: ¿Es vitamina o suplemento?")
                    if r == "s":
                        print("Vitaminas/Suplemento")
                    else:
                        r = pedir_si_no("Q7: ¿Es antibiótico?")
                        if r == "s":
                            print("Antibiótico")
                        else:
                            print("Medicina especializada")
            else:
                r = pedir_si_no("Q5: ¿Se aplica en la piel?")
                if r == "s":
                    print("Vendaje/Curita")
                else:
                    print("Inyección/Vacuna")
    
    # PRODUCTOS DE HIGIENE Y LIMPIEZA
    else:
        r = pedir_si_no("Q3: ¿Es para higiene personal?")
        if r == "s":
            
            # higiene personal
            r = pedir_si_no("Q4: ¿Es líquido?")
            if r == "s":
                r = pedir_si_no("Q5: ¿Es para el cabello?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Limpia el cabello?")
                    if r == "s":
                        print("Shampoo")
                    else:
                        print("Acondicionador")
                else:
                    r = pedir_si_no("Q6: ¿Es para el cuerpo?")
                    if r == "s":
                        r = pedir_si_no("Q7: ¿Hace espuma?")
                        if r == "s":
                            print("Jabón líquido/Gel de baño")
                        else:
                            print("Loción/Crema corporal")
                    else:
                        r = pedir_si_no("Q7: ¿Es para la boca?")
                        if r == "s":
                            print("Enjuague bucal")
                        else:
                            print("Perfume/Colonia")
            else:
                r = pedir_si_no("Q5: ¿Es para los dientes?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es pasta?")
                    if r == "s":
                        print("Pasta dental")
                    else:
                        print("Cepillo de dientes")
                else:
                    r = pedir_si_no("Q6: ¿Es para el cuerpo?")
                    if r == "s":
                        r = pedir_si_no("Q7: ¿Absorbe humedad?")
                        if r == "s":
                            print("Desodorante")
                        else:
                            print("Jabón en barra")
                    else:
                        r = pedir_si_no("Q7: ¿Es de papel?")
                        if r == "s":
                            r = pedir_si_no("Q8: ¿Es para la nariz?")
                            if r == "s":
                                print("Pañuelos")
                            else:
                                print("Papel higiénico")
                        else:
                            print("Toalla sanitaria/Pañal")
        else:
            
            # productos de limpieza del hogar
            r = pedir_si_no("Q4: ¿Es líquido?")
            if r == "s":
                r = pedir_si_no("Q5: ¿Es para lavar ropa?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Suaviza la ropa?")
                    if r == "s":
                        print("Suavizante")
                    else:
                        print("Detergente líquido")
                else:
                    r = pedir_si_no("Q6: ¿Es para lavar trastes?")
                    if r == "s":
                        print("Jabón para trastes")
                    else:
                        r = pedir_si_no("Q7: ¿Desinfecta?")
                        if r == "s":
                            print("Cloro/Desinfectante")
                        else:
                            print("Limpiador multiusos")
            else:
                r = pedir_si_no("Q5: ¿Es en polvo?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es para lavar ropa?")
                    if r == "s":
                        print("Detergente en polvo")
                    else:
                        print("Limpiador en polvo")
                else:
                    r = pedir_si_no("Q6: ¿Se usa para limpiar superficies?")
                    if r == "s":
                        r = pedir_si_no("Q7: ¿Es abrasivo?")
                        if r == "s":
                            print("Esponja/Fibra")
                        else:
                            print("Toallitas húmedas")
                    else:
                        r = pedir_si_no("Q7: ¿Absorbe olores?")
                        if r == "s":
                            print("Ambientador")
                        else:
                            print("Bolsas de basura")

def residuos(): #10
   
    # RESIDUOS Y DESECHOS
    r = pedir_si_no("Q1: ¿Es de origen orgánico?")
    if r == "s":
        
        # RESIDUOS ORGÁNICOS
        r = pedir_si_no("Q2: ¿Proviene de comida?")
        if r == "s":
            
            # desechos de comida
            r = pedir_si_no("Q3: ¿Es de fruta?")
            if r == "s":
                r = pedir_si_no("Q4: ¿Es la parte exterior?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Es dura?")
                    if r == "s":
                        print("Cáscara de coco/nuez")
                    else:
                        print("Cáscara de plátano/naranja")
                else:
                    r = pedir_si_no("Q5: ¿Es el centro/semilla?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Es grande y duro?")
                        if r == "s":
                            print("Hueso de durazno/aguacate")
                        else:
                            print("Semillas pequeñas")
                    else:
                        print("Pulpa de fruta podrida")
            else:
                r = pedir_si_no("Q4: ¿Es de verdura?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Son hojas exteriores?")
                    if r == "s":
                        print("Hojas de lechuga/col")
                    else:
                        r = pedir_si_no("Q6: ¿Son cáscaras?")
                        if r == "s":
                            print("Cáscara de papa/cebolla")
                        else:
                            print("Verdura podrida")
                else:
                    r = pedir_si_no("Q5: ¿Es de carne o pescado?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Son huesos?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Son grandes?")
                            if r == "s":
                                print("Huesos de pollo/res")
                            else:
                                print("Espinas de pescado")
                        else:
                            print("Grasa/piel de carne")
                    else:
                        r = pedir_si_no("Q6: ¿Es pan o cereal?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Está mohoso?")
                            if r == "s":
                                print("Pan con moho")
                            else:
                                print("Pan duro/migajas")
                        else:
                            r = pedir_si_no("Q7: ¿Es líquido?")
                            if r == "s":
                                print("Aceite usado/leche agria")
                            else:
                                print("Comida echada a perder")
        else:
            
            # desechos de plantas/jardín
            r = pedir_si_no("Q3: ¿Es de árbol?")
            if r == "s":
                r = pedir_si_no("Q4: ¿Son hojas?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Están secas?")
                    if r == "s":
                        print("Hojas secas")
                    else:
                        print("Hojas verdes caídas")
                else:
                    r = pedir_si_no("Q5: ¿Son ramas?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Son gruesas?")
                        if r == "s":
                            print("Ramas gruesas/troncos")
                        else:
                            print("Ramas/palitos")
                    else:
                        print("Corteza de árbol")
            else:
                r = pedir_si_no("Q4: ¿Es pasto o césped?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Está cortado?")
                    if r == "s":
                        print("Pasto cortado")
                    else:
                        print("Pasto seco/maleza")
                else:
                    r = pedir_si_no("Q5: ¿Son flores?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Están marchitas?")
                        if r == "s":
                            print("Flores marchitas")
                        else:
                            print("Pétalos caídos")
                    else:
                        r = pedir_si_no("Q6: ¿Es de jardín?")
                        if r == "s":
                            print("Hojas de plantas/arbustos")
                        else:
                            print("Materia orgánica descompuesta")
    
    # RESIDUOS INORGÁNICOS
    else:
        r = pedir_si_no("Q2: ¿Es de plástico?")
        if r == "s":
            
            # desechos de plástico
            r = pedir_si_no("Q3: ¿Era un envase?")
            if r == "s":
                r = pedir_si_no("Q4: ¿Era para bebidas?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Es transparente?")
                    if r == "s":
                        print("Botella de agua/refresco (usado/inservible)")
                    else:
                        print("Botella de leche/jugo (usado/inservible)")
                else:
                    r = pedir_si_no("Q5: ¿Era para comida?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Es rígido?")
                        if r == "s":
                            print("Envase de yogurt/margarina (usado/inservible)")
                        else:
                            print("Bolsa de pan/snacks (usado/inservible)")
                    else:
                        r = pedir_si_no("Q6: ¿Era para productos de limpieza?")
                        if r == "s":
                            print("Envase de detergente/shampoo (usado/inservible)")
                        else:
                            print("Envase de medicinas (usado/inservible)")
            else:
                r = pedir_si_no("Q4: ¿Es pequeño?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Es una tapa?")
                    if r == "s":
                        print("Tapa de botella/frasco")
                    else:
                        r = pedir_si_no("Q6: ¿Es envoltura?")
                        if r == "s":
                            print("Envoltura de dulce/producto (usado/inservible)")
                        else:
                            print("Juguete pequeño roto")
                else:
                    r = pedir_si_no("Q5: ¿Era un objeto de uso diario?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Era para la cocina?")
                        if r == "s":
                            print("Utensilio de cocina roto")
                        else:
                            print("Objeto de plástico roto")
                    else:
                        print("Mueble de plástico roto")
        else:
            r = pedir_si_no("Q3: ¿Es de vidrio?")
            if r == "s":
                
                # desechos de vidrio
                r = pedir_si_no("Q4: ¿Era un envase?")
                if r == "s":
                    r = pedir_si_no("Q5: ¿Era para bebidas?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Era de cerveza/refresco?")
                        if r == "s":
                            print("Botella de cerveza/refresco (usado/inservible)")
                        else:
                            print("Botella de vino/licor (usado/inservible)")
                    else:
                        r = pedir_si_no("Q6: ¿Era para comida?")
                        if r == "s":
                            print("Frasco de mermelada (usado/inservible)")
                        else:
                            print("Frasco de medicinas/cosméticos (usado/inservible)")
                else:
                    r = pedir_si_no("Q5: ¿Está roto?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Era ventana/espejo?")
                        if r == "s":
                            print("Vidrio de ventana/espejo")
                        else:
                            print("Vaso/plato de vidrio roto")
                    else:
                        print("Objeto de vidrio desechado")
            else:
                r = pedir_si_no("Q4: ¿Es de metal?")
                if r == "s":
                    
                    # desechos de metal
                    r = pedir_si_no("Q5: ¿Era un envase?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Era lata de comida?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Era grande?")
                            if r == "s":
                                print("Lata de atún (usado/inservible)")
                            else:
                                print("Lata pequeña (usado/inservible)")
                        else:
                            r = pedir_si_no("Q7: ¿Era de bebida?")
                            if r == "s":
                                print("Lata de refresco/cerveza (usado/inservible)")
                            else:
                                print("Envase metálico/aerosol (usado/inservible)")
                    else:
                        r = pedir_si_no("Q6: ¿Es pequeño?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Son clavos/tornillos?")
                            if r == "s":
                                print("Clavos/tornillos oxidados")
                            else:
                                print("Alambre/metal pequeño")
                        else:
                            r = pedir_si_no("Q7: ¿Era electrodoméstico?")
                            if r == "s":
                                print("Electrodoméstico descompuesto")
                            else:
                                print("Chatarra/metal grande")
                else:
                    
                    # otros materiales inorgánicos
                    r = pedir_si_no("Q5: ¿Es de papel/cartón?")
                    if r == "s":
                        r = pedir_si_no("Q6: ¿Es periódico/revista?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Está mojado?")
                            if r == "s":
                                print("Papel mojado/inservible")
                            else:
                                print("Periódico/revista vieja")
                        else:
                            r = pedir_si_no("Q7: ¿Es cartón?")
                            if r == "s":
                                r = pedir_si_no("Q8: ¿Era caja?")
                                if r == "s":
                                    print("Caja de cartón")
                                else:
                                    print("Cartón corrugado")
                            else:
                                print("Papel usado/documentos")
                    else:
                        r = pedir_si_no("Q6: ¿Es de tela?")
                        if r == "s":
                            r = pedir_si_no("Q7: ¿Era ropa?")
                            if r == "s":
                                print("Ropa vieja/rota")
                            else:
                                print("Trapos/telas desechadas")
                        else:
                            r = pedir_si_no("Q7: ¿Es escombro de construcción?")
                            if r == "s":
                                r = pedir_si_no("Q8: ¿Es de concreto/cemento?")
                                if r == "s":
                                    print("Escombro de concreto")
                                else:
                                    print("Ladrillos/blocks rotos")
                            else:
                                r = pedir_si_no("Q8: ¿Es electrónico?")
                                if r == "s":
                                    r = pedir_si_no("Q9: ¿Es pequeño?")
                                    if r == "s":
                                        print("Celular/dispositivo (usado/inservible)")
                                    else:
                                        print("Computadora/TV descompuesta")
                                else:
                                    print("Otro desecho inorgánico")

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
    r = pedir_si_no("Q2: ¿Es un organismo vivo o un producto directamente derivado de uno (como plantas o frutas)?")
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
    r = pedir_si_no("Q5: ¿Es un fenómeno natural, un cuerpo celeste o una forma de energía (por ejemplo: lluvia, sol, luz, terremoto)?")
    if r == "s":
        # Agotar rama Fenómenos / Cuerpos celestes / Energía
        rama_fenomeno()
        # Entraste en: Fenómeno/Cuerpo celeste/Energía -> (aquí agotar preguntas de esa categoría).
        return

    # Q5
    r = pedir_si_no("Q6: ¿Es un objeto inanimado o cosa tangible (sea natural o fabricada por humanos)?")
    if r == "s":
        # Agotar rama Objetos inanimados
        rama_objeto()
        # Entraste en: Objeto inanimado -> (aquí agotar preguntas de esa categoría).
        return

    # Si todas las raíces son 'n'
    print("Pensaste en nada")


if __name__ == "__main__":
    main()
