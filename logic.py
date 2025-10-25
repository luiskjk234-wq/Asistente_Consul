def responder(mensaje):
    mensaje = mensaje.strip().lower()

    if mensaje in ["hola", "buenos días", "buenas"]:
        return (
            "👋 ¡Hola! Bienvenido al consultorio Torre Médica H.\n"
            "1️⃣ Agendar cita\n"
            "2️⃣ Cancelar cita\n"
            "3️⃣ Información del consultorio"
        )
    elif mensaje == "1":
        return "🗓️ Para agendar una cita, por favor indícanos tu nombre y especialidad."
    elif mensaje == "2":
        return "❌ Para cancelar una cita, por favor indícanos tu nombre y fecha de la cita."
    elif mensaje == "3":
        return "🏥 Estamos ubicados en Guacara, Carabobo. Horario: Lunes a Viernes de 8am a 4pm."
    else:
        return "🤖 No entendí tu mensaje. Por favor elige una opción del menú."
