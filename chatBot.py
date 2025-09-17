# -*- coding: utf-8 -*-
import re
from datetime import datetime

# Subcategorías de sucursal
sucursal_ubicacion_RE = r"(sucursal(es)?|oficina(s)?|tienda(s)?|centro(s)?( de servicio)?|branch|store|ubicaci[oó]n|direcci[oó]n|domicilio|mapa|localizar|d[oó]nde|queda|cercan[ao]s?)"
sucursal_horario_RE   = r"(horario(s)?|hora(s)?|abre(n)?|cierran?|apertura|cierre|atenci[oó]n)"
sucursal_servicios_RE = r"(servicio(s)?|disponible(s)?|ofrecen|puedo hacer|hay en la sucursal|tr[aá]mites)"
sucursal_apertura_RE  = r"(apertura|cierre|abrir|cerrar|a qu[eé] hora)"
sucursal_acciones_RE  = r"(pagar|recoger|enviar|tramite|permiten|que se puede|hacer en la sucursal)"

# Regex con más variaciones y frases coloquiales
tracking_RE   = rastreo_RE = r"(rastreo|tracking|seguimiento|localiza(?:r|ción)|dónde (está|anda)|ver.*paquete|saber.*paquete|donde va mi paquete|ubicaci[oó]n.*paquete|mi paquete|seguir.*paquete|cuando.*entregan.*paquete|paq(?:u|ue)te|mi pedido|estado.*pedido|estado.*env[ií]o|c[oó]mo va.*(pedido|env[ií]o)|progreso.*(pedido|env[ií]o)|actualizaci[oó]n.*(pedido|env[ií]o)|ya (sal[ií]o|viene|lo enviaron)|a[uú]n no llega|todav[ií]a no llega|me urge saber)"
pickup_RE     = r"(recogida|pickup|agendar (recogida|env[ií]o)|programar (env[ií]o|paquete)|quiero que lo recojan|pasen por mi paquete)"
tarifa_RE     = r"(cotiza(r|ción)|precio|tarifa|costo|cuánto vale|cuánto cuesta|cuánto sale|quiero saber.*(cuesta|precio)|promociones|costos)"
sucursal_RE = (sucursal_ubicacion_RE + "|" +sucursal_horario_RE   + "|" +sucursal_servicios_RE + "|" +sucursal_apertura_RE  + "|" +sucursal_acciones_RE)
aduana_RE     = r"(aduana|aduna|impuesto|tax|documentaci[oó]n|pago pendiente|retenci[oó]n|servicio de aduana)"
fallida_RE    = r"(entrega fallida|no lleg[oó]|no entregado|no lo recib[ií]|no recibi|no lleg[oó] mi paquete|no tengo mi paquete|porque no.*(recib|tengo|llego).*paquete|reprogramar|devoluci[oó]n|reclamo|incidente|por qu[eé] no)"
crear_RE      = r"(crear env[ií]o|nuevo env[ií]o|enviar paquete|quiero enviar|generar gu[ií]a|mandar un paquete|hacer un env[ií]o|como (hago|crear|realizo) un env[ií]o)"
agente_RE     = r"(hablar con humano|agente|soporte real|asesor|supervisor|empleado real|persona real|pasame (un|a) (humano|gerente|persona)|necesito (hablar|ayuda) con (alguien|una persona)|quiero hablar con un asistente)"
salir_RE      = r"(salir|adi[oó]s|terminar|gracias|ya no|bye|nos vemos)"


# Dataset ficticio de sucursales por ciudad
sucursales = {
    "cdmx": {
        "alias": [r"\b(cdmx|ciudad de méxico|df|distrito federal|capital|méxico)\b"],
        "direccion": "Av. Paseo de la Reforma 123, Col. Juárez, CDMX",
        "horario": "Lunes a viernes 9:00 - 18:00, sábados 9:00 - 14:00",
        "servicios": "Envío y recolección de paquetes, pago de servicios, asesoría personalizada"
    },
    "monterrey": {
        "alias": [r"\b(monterrey|mty|nuevo le[oó]n|mtrey)\b"],
        "direccion": "Av. Constitución 456, Col. Centro, Monterrey, NL",
        "horario": "Lunes a viernes 8:30 - 17:30, sábados 9:00 - 13:00",
        "servicios": "Envío de paquetes, recolección y atención empresarial"
    },
    "guadalajara": {
        "alias": [r"\b(guadalajara|gdl|jal|jalisco|ciudad de guadalajara)\b"],
        "direccion": "Av. Vallarta 789, Col. Americana, Guadalajara, JAL",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales e internacionales, recolección y pagos"
    },
    "puebla": {
        "alias": [r"\b(puebla|pue|angelopolis)\b"],
        "direccion": "Blvd. Héroes 321, Col. Centro, Puebla, PUE",
        "horario": "Lunes a viernes 9:00 - 17:00",
        "servicios": "Atención general, envíos nacionales, pagos"
    },
    "tijuana": {
        "alias": [r"\b(tijuana|bc|baja california|tj)\b"],
        "direccion": "Av. Revolución 123, Zona Centro, Tijuana, BC",
        "horario": "Lunes a viernes 8:00 - 18:00, sábados 9:00 - 13:00",
        "servicios": "Envíos nacionales e internacionales, atención personalizada"
    },
    "leon": {
        "alias": [r"\b(le[oó]n|gto|guanajuato)\b"],
        "direccion": "Blvd. Adolfo López Mateos 456, Col. Centro, León, GTO",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y recolección de paquetes"
    },
    "queretaro": {
        "alias": [r"\b(querétaro|qro|queretaro capital)\b"],
        "direccion": "Av. Constituyentes 789, Col. Centro, Querétaro, QRO",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales, pagos y atención empresarial"
    },
    "cancun": {
        "alias": [r"\b(canc[uú]n|quintana roo|cancun)\b"],
        "direccion": "Av. Kukulcán 123, Zona Hotelera, Cancún, QROO",
        "horario": "Lunes a viernes 9:00 - 18:00, sábados 9:00 - 14:00",
        "servicios": "Envíos y recolección, pagos y asesoría"
    },
    "merida": {
        "alias": [r"\b(m[ée]rida|yucat[áa]n)\b"],
        "direccion": "Calle 60 456, Centro, Mérida, YUC",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales, pagos y recolección"
    },
    "toluca": {
        "alias": [r"\b(toluca|edomex|estado de m[eé]xico)\b"],
        "direccion": "Av. Lerdo 789, Col. Centro, Toluca, MEX",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y atención general"
    },
    "ciudad juarez": {
        "alias": [r"\b(ciudad juárez|juárez|chihuahua|cd juárez)\b"],
        "direccion": "Av. Tecnológico 123, Ciudad Juárez, CHIH",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales, pagos y recolección"
    },
    "mexicali": {
        "alias": [r"\b(mexicali|bc|baja california)\b"],
        "direccion": "Av. Reforma 456, Mexicali, BC",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales e internacionales"
    },
    "saltillo": {
        "alias": [r"\b(saltillo|coahuila)\b"],
        "direccion": "Blvd. Nazario 789, Saltillo, COA",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y recolección"
    },
    "veracruz": {
        "alias": [r"\b(veracruz|ver)\b"],
        "direccion": "Av. Independencia 123, Veracruz, VER",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y atención general"
    },
    "acapulco": {
        "alias": [r"\b(acapulco|gro|guerrero)\b"],
        "direccion": "Costera Miguel Alemán 123, Acapulco, GRO",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos y recolección, pagos y asesoría"
    },
    "tampico": {
        "alias": [r"\b(tampico|tamps|tamaulipas)\b"],
        "direccion": "Av. Hidalgo 456, Tampico, TAMPS",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales, pagos y atención general"
    },
    "cuernavaca": {
        "alias": [r"\b(cuernavaca|mor|morelos)\b"],
        "direccion": "Av. Morelos 123, Cuernavaca, MOR",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y recolección"
    },
    "chihuahua": {
        "alias": [r"\b(chihuahua|chih)\b"],
        "direccion": "Blvd. Universidad 456, Chihuahua, CHIH",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos, pagos y atención general"
    },
    "morelia": {
        "alias": [r"\b(morelia|mic|michoac[áa]n)\b"],
        "direccion": "Av. Madero 123, Morelia, MIC",
        "horario": "Lunes a viernes 9:00 - 18:00",
        "servicios": "Envíos nacionales, pagos y atención general"
    }
}


def detectar_ciudad(texto):
    for ciudad, data in sucursales.items():
        for patron in data["alias"]:
            if re.search(patron, texto, re.IGNORECASE):
                return ciudad
    return None

# Estado inicial
state = 0
Salida = True

print("Bienvenido al Chatbot de DHL. ¿En qué puedo ayudarte hoy?")
opcion = ""
while Salida:
    if state == 0:
        print("\nOpciones disponibles:")
        print("1. Rastreo de envíos")
        print("2. Agendar recogida")
        print("3. Cotización Envio")
        print("4. Localización de sucursales")
        print("5. Estado de aduanas")
        print("6. Entregas fallidas / reclamos")
        print("7. Crear un envío")
        print("8. Hablar con un agente humano")
        print("9. Salir")

        opcion = input("\nEscribe tu solicitud o número de opción: ").strip()

        # Si el usuario pone solo el número
        if opcion == "1":
            state = 1
        elif opcion == "2":
            state = 2
        elif opcion == "3":
            state = 3
        elif opcion == "4":
            state = 4
        elif opcion == "5":
            state = 5
        elif opcion == "6":
            state = 6
        elif opcion == "7":
            state = 7
        elif opcion == "8":
            state = 8
        elif opcion == "9":
            state = 9

        # Si escribe texto libre
        elif re.search(fallida_RE, opcion, flags=re.IGNORECASE):
            state = 6  # Prioridad sobre rastreo
        elif re.search(tracking_RE, opcion, flags=re.IGNORECASE):
            state = 1
        elif re.search(pickup_RE, opcion, flags=re.IGNORECASE):
            state = 2
        elif re.search(tarifa_RE, opcion, flags=re.IGNORECASE):
            state = 3
        elif re.search(sucursal_RE, opcion, flags=re.IGNORECASE):
            state = 4
        elif re.search(aduana_RE, opcion, flags=re.IGNORECASE):
            state = 5
        elif re.search(crear_RE, opcion, flags=re.IGNORECASE):
            state = 7
        elif re.search(agente_RE, opcion, flags=re.IGNORECASE):
            state = 8
        elif re.search(salir_RE, opcion, flags=re.IGNORECASE):
            state = 9
        else:
            print("Lo siento, no entendí tu solicitud. Intenta de nuevo.")
            state = 0

    # Opciones
    if state == 1:
        tracking = input("Ingresa tu número de guía: ")
        print(f"El envío con número {tracking} está en reparto y llegará en 2 días hábiles.")
        state = 0

        extra_info = input("¿Quieres saber más información sobre tu envío? (sí/no): ").strip().lower()

        if extra_info in ("si", "sí", "s","ok","Ok","OK","oK","Si","SI"):
              print("\nDetalles de seguimiento:")
              print("- Dejado en sucursal hace 24 hrs")
              print("- En tránsito en Cuautitlán Izcali hace 12 hrs")
              print("- Llegando a centro de reparto local")
              # después de dar más info, regresa al menú principal
              print("\n¿Algo más en lo que podamos ayudarte?")
              state = 0
        else:
              # si no quiere más info, simplemente regresa al menú principal
              print("\n¿Algo más en lo que podamos ayudarte?")
              state = 0

    if state == 2:
        fecha = input("Ingresa la fecha para la recogida (YYYY-MM-DD): ")
        print(f"Recogida programada para el {fecha}. Un mensajero irá a tu dirección registrada.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 3:
        origen = input("Origen: ")
        destino = input("Destino: ")
        peso = input("Peso (kg): ")
        print(f"El envío de {origen} a {destino}, {peso} kg, tiene un costo aproximado de $500 MXN y entrega en 3 días.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 4:
        consulta = opcion  # lo que el usuario escribió originalmente
        ciudad = detectar_ciudad(consulta)

        if ciudad:
            data = sucursales[ciudad]
            print(f"Sucursal en {ciudad.upper()}:")
            print(f"📍 Dirección: {data['direccion']}")
            print(f"🕒 Horario: {data['horario']}")
            print(f"🔧 Servicios: {data['servicios']}")
        else:
            # Si no se detecta ciudad, preguntar al usuario
            ciudad_usuario = input("Claro, ¿en qué ciudad te encuentras? (Ej: CDMX, Monterrey, Guadalajara, Puebla): ").strip().lower()
            ciudad = detectar_ciudad(ciudad_usuario)
            if ciudad:
                data = sucursales[ciudad]
                print(f"Sucursal en {ciudad.upper()}:")
                print(f"📍 Dirección: {data['direccion']}")
                print(f"🕒 Horario: {data['horario']}")
                print(f"🔧 Servicios: {data['servicios']}")
            else:
                #print("Lo siento, aún no tengo registrada esa ciudad. Intenta con CDMX, Monterrey, Guadalajara o Puebla.")
                print("Lo siento, no hay sucursales disponibles en esa ciudad.")
                state = 0
                continue  # vuelve al menú principal si la ciudad no se reconoce

        # Ahora responder según el tipo de consulta específica
        if re.search(sucursal_ubicacion_RE, consulta, re.IGNORECASE):
            print(f"Dirección: {data['direccion']}")
        if re.search(sucursal_horario_RE, consulta, re.IGNORECASE):
            print(f"Horario de atención: {data['horario']}")
        if re.search(sucursal_servicios_RE, consulta, re.IGNORECASE):
            print(f"Servicios: {data['servicios']}")
        if re.search(sucursal_apertura_RE, consulta, re.IGNORECASE):
            print("La sucursal abre a las 9:00 am y cierra a las 6:00 pm entre semana.")  # horario fijo
        if re.search(sucursal_acciones_RE, consulta, re.IGNORECASE):
            print("Puedes enviar y recoger paquetes, pagar servicios y realizar trámites relacionados con tus envíos.")

        # Si no se detectó ningún patrón de consulta, dar respuesta genérica
        if not (re.search(sucursal_ubicacion_RE, consulta, re.IGNORECASE) or
                re.search(sucursal_horario_RE, consulta, re.IGNORECASE) or
                re.search(sucursal_servicios_RE, consulta, re.IGNORECASE) or
                re.search(sucursal_apertura_RE, consulta, re.IGNORECASE) or
                re.search(sucursal_acciones_RE, consulta, re.IGNORECASE)):
            print("Lo siento, no entendí tu solicitud sobre sucursales. Puedes preguntar por ubicación, horarios, servicios o trámites.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 5:
        print("Tu envío está retenido en aduanas. Se requiere el pago de impuestos y documentación adicional.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 6:
        guia = input("Por favor ingresa tu número de guía: ")
        print(f"Detectamos un intento de entrega fallido para el envío {guia}.")
        print("Puedes reprogramar ingresando a tu portal DHL o llamando al 01-800-DHL.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 7:
        destino = input("Destino del paquete: ")
        peso = input("Peso (kg): ")
        print(f"Guía generada para envío a {destino}, peso {peso} kg. Código: DHL{datetime.now().strftime('%H%M%S')}")
        print("\n¿Algo más en lo que podamos ayudarte?")
        state = 0

    if state == 8:
        print("Te conectamos con un agente humano... por favor espera.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        Salida = False

    if state == 9:
        print("Gracias por usar el Chatbot DHL. Hasta pronto.")
        print("\n¿Algo más en lo que podamos ayudarte?")
        Salida = False