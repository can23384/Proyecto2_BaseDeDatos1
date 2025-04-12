import threading
import psycopg2
from time import time, sleep
from random import randint, choice

# Configuracion de la base de datos
CONFIG_BD = {
    'dbname': 'Proyecto_2',
    'user': 'postgres',
    'password': 'hola12345',
    'host': 'localhost',
    'port': 5432
}

# Niveles de aislamiento
niveles_aislamiento = {
    'READ COMMITTED': 'READ COMMITTED',
    'REPEATABLE READ': 'REPEATABLE READ',
    'SERIALIZABLE': 'SERIALIZABLE'
}

# Variables globales
tiempos_reservas = []
reservas_exitosas = 0
reservas_fallidas = 0
lock = threading.Lock()


def limpiar_reservas(asiento_ids):
    try:
        conexion = psycopg2.connect(**CONFIG_BD)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM reservas WHERE id_asiento = ANY(%s);", (asiento_ids,))
        conexion.commit()
        print(f" Se eliminaron reservas previas para los asientos: {asiento_ids}")
    except Exception as error:
        print(f" Error al limpiar reservas: {error}")
    finally:
        cursor.close()
        conexion.close()


def reservar_asiento(id_usuario, id_asiento, nivel_aislamiento):
    global reservas_exitosas, reservas_fallidas
    inicio = time()

    try:
        conexion = psycopg2.connect(**CONFIG_BD)
        conexion.set_session(isolation_level=nivel_aislamiento)
        cursor = conexion.cursor()

        cursor.execute("BEGIN;")
        cursor.execute("SELECT 1 FROM reservas WHERE id_asiento = %s FOR UPDATE;", (id_asiento,))
        ya_reservado = cursor.fetchone()

        if ya_reservado:
            conexion.rollback()
            with lock:
                reservas_fallidas += 1
            print(f"[Usuario {id_usuario}] ❌ Asiento {id_asiento} ya reservado.")
        else:
            cursor.execute("""
                INSERT INTO reservas (id_usuario, id_asiento, fecha_reserva, estado)
                VALUES (%s, %s, now(), 'Pagada');
            """, (id_usuario, id_asiento))
            conexion.commit()
            with lock:
                reservas_exitosas += 1
            print(f"[Usuario {id_usuario}] ✅ Reservó asiento {id_asiento}")

    except Exception as error:
        print(f"[Usuario {id_usuario}] ❌ Error: {error}")
        conexion.rollback()
        with lock:
            reservas_fallidas += 1
    finally:
        duracion = time() - inicio
        with lock:
            tiempos_reservas.append(duracion)

        cursor.close()
        conexion.close()


def ejecutar_simulacion(numero_usuarios, aislamiento, asiento_ids):
    global reservas_exitosas, reservas_fallidas, tiempos_reservas
    print(f"\n=== Simulación con {numero_usuarios} usuarios / Aislamiento: {aislamiento} ===")
    tiempos_reservas = []
    reservas_exitosas = 0
    reservas_fallidas = 0

    limpiar_reservas(asiento_ids)

    hilos = []

    
    asientos_asignados = [choice(asiento_ids) for _ in range(numero_usuarios)]

    for i in range(numero_usuarios):
        id_usuario = randint(1, 3)
        id_asiento = asientos_asignados[i]

        hilo = threading.Thread(
            target=reservar_asiento,
            args=(id_usuario, id_asiento, niveles_aislamiento[aislamiento])
        )
        hilos.append(hilo)
        hilo.start()
        sleep(0.05)  

    for hilo in hilos:
        hilo.join()

    # Resultados
    if tiempos_reservas:
        promedio = (sum(tiempos_reservas) / len(tiempos_reservas)) * 1000  
        print(f"\n📊 Resultados de la simulación:")
        print(f"🧑‍🤝‍🧑 Usuarios concurrentes: {numero_usuarios}")
        print(f"🔒 Nivel de aislamiento: {aislamiento}")
        print(f"✅ Reservas exitosas: {reservas_exitosas}")
        print(f"❌ Reservas fallidas: {reservas_fallidas}")
        print(f"⏱️ Tiempo promedio por reserva: {promedio:.2f} ms\n")


#Menu
if __name__ == "__main__":
    print("🎛️ Simulador de Reservas Concurrentes\n")

    print("Selecciona el nivel de aislamiento:")
    print("1. READ COMMITTED")
    print("2. REPEATABLE READ")
    print("3. SERIALIZABLE")

    opciones_aislamiento = {
        '1': 'READ COMMITTED',
        '2': 'REPEATABLE READ',
        '3': 'SERIALIZABLE'
    }

    seleccion = input("Opción [1-3]: ").strip()
    while seleccion not in opciones_aislamiento:
        seleccion = input("❌ Opción inválida. Elige 1, 2 o 3: ").strip()

    aislamiento = opciones_aislamiento[seleccion]

    while True:
        try:
            numero_usuarios = int(input("Cantidad de usuarios a simular: "))
            if numero_usuarios > 0:
                break
            else:
                print("❌ Ingresa un número mayor que 0.")
        except ValueError:
            print("❌ Ingresa un número válido.")


    asientos_disponibles = list(range(1, 21))  

    ejecutar_simulacion(
        numero_usuarios=numero_usuarios,
        aislamiento=aislamiento,
        asiento_ids=asientos_disponibles
    )
