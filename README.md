# Manual de Uso – Simulador de Reservas Concurrentes

## Requisitos Previos

1. PostgreSQL instalado  
2. pgAdmin 4 funcionando correctamente  
3. Python 3.8+ instalado  
4. Librerías necesarias:

   ```bash
   pip install psycopg2
   
##   
   
### Paso 1: Crear la base de datos en pgAdmin 4

1. PostgreSQL instalado  
2. pgAdmin 4 funcionando correctamente  
3. Python 3.8+ instalado  
4. Librerías necesarias:

   ```bash
   pip install psycopg2
   
### Paso 2: Ejecutar ddl.sql y data.sql

1. En pgAdmin, hacer clic en la base Proyecto_2.
2. Ir a la pestaña Query Tool.
3. Cargar el archivo ddl.sql y ejecutarlo.
4. Luego, cargar y ejecutar data.sql.

### Paso 3: Configurar el script de simulación en Python

1. Asegurarse de tener tu script proyecto2.py.
2. Abrir el archivo y editar esta sección si es necesario: 
    ```bash
    CONFIG_BD = {
    'dbname': 'Proyecto_2',
    'user': 'postgres',       # Cambiar si el usuario es otro
    'password': '123456',     # Coloca la contraseña real
    'host': 'localhost',
    'port': 5432
    }

### Paso 4: Ejecutar la simulación
Desde la terminal, ejecutar el archivo Python:
python proyecto2.py
    
Se verá una interfaz interactiva:
    
🎛️ Simulador de Reservas Concurrentes
Selecciona el nivel de aislamiento:
1. READ COMMITTED
2. REPEATABLE READ
3. SERIALIZABLE
Opción [1-3]:
##   
## Repetir simulaciones
Si se quiere repetir una simulación, simplemente vuelve a ejecutarlo.
Aumenta el número de usuarios o cambia el nivel de aislamiento para observar diferencias en los resultados.
