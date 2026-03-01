import pandas as pd
from sqlalchemy import create_engine, text
import urllib
from datetime import date
import os

# ===============================
# 1. CONFIGURACIÓN DE CONEXIÓN
# ===============================
# NOTA: En un entorno real, estas variables se cargan desde un archivo .env 
# o variables de entorno por seguridad.
SERVER = os.getenv("SQL_SERVER", "tu-servidor.database.windows.net") 
DATABASE = os.getenv("SQL_DATABASE", "padel")
USERNAME = os.getenv("SQL_USER", "tu_usuario")
PASSWORD = os.getenv("SQL_PASSWORD", "tu_password")
DRIVER = "{ODBC Driver 18 for SQL Server}"

def get_engine():
    """Crea la conexión a Azure SQL Server"""
    params = urllib.parse.quote_plus(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};"
        "Encrypt=yes;TrustServerCertificate=yes;"
    )
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

engine = get_engine()

# ===============================
# 2. MAPEOS (REGLAS DE NEGOCIO)
# ===============================
MAPEO_GOLPES = {
    "v": "vibora", "vd": "volea_drive", "vr": "volea_reves",
    "s": "smash", "b": "bandeja", "g": "globo",
    "sn": "saque", "rn": "resto", "baj": "bajada", "blo": "bloqueo",
    "spg": "salida_pared_globo", "spc": "salida_pared_chiquita",
    "toq": "toque", "ch": "chiquita"
}

RESULTADOS_MAP = {
    "w": "winner_juani", "wc": "winner_compañero", "wr1": "winner_rival_drive", 
    "wr2": "winner_rival_reves", "er": "error_rival", "ec": "error_compañero", 
    "ej": "error_juani", "f": "forzado", "nf": "no_forzado"
}

MAPEO_INTENCION = {"man": "mantenimiento", "ata": "ataque", "def": "defensa", "fin": "finalizacion"}
MAPEO_FASE = {"fini": "inicio", "fdes": "desarrollo", "fdef": "defensa"}
MARCADORES_VALIDOS = {"0", "15", "30", "40", "adv1", "adv2", "stp"}

# ===============================
# 3. LÓGICA DE PROCESAMIENTO
# ===============================

def obtener_o_crear_jugador(nombre_completo):
    """Verifica existencia del jugador o lo registra en la DB"""
    if not nombre_completo: return None
    partes = nombre_completo.split(" ", 1)
    nombre = partes[0]
    apellido = partes[1] if len(partes) > 1 else ""
    
    with engine.begin() as conn:
        res = conn.execute(
            text("SELECT id_jugador FROM jugador WHERE nombre=:n AND apellido=:a"),
            {"n": nombre, "a": apellido}
        ).fetchone()
        if res: return res[0]
        
        nuevo_id = conn.execute(text("SELECT ISNULL(MAX(id_jugador),0)+1 FROM jugador")).scalar()
        conn.execute(text("INSERT INTO jugador (id_jugador, nombre, apellido, posicion, es_juani) VALUES (:id, :n, :a, 'desconocida', 0)"),
            {"id": nuevo_id, "n": nombre, "a": apellido})
        return nuevo_id

def cargar_partido(path_txt):
    """Lee el archivo de texto y procesa cada evento de juego"""
    if not os.path.exists(path_txt):
        print(f"Error: No se encuentra el archivo {path_txt}")
        return

    with open(path_txt, encoding="utf-8") as f:
        lineas = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    config = {}
    eventos = []
    for l in lineas:
        if "=" in l:
            k, v = l.split("=", 1)
            config[k.strip()] = v.strip()
        else: eventos.append(l)

    jugador_nombre = config.get("jugador_analizado", "Juani Rubini")
    id_jugador = obtener_o_crear_jugador(jugador_nombre)
    id_sesion = int(config.get("id_sesion", 1))

    # Lógica de procesamiento de eventos (Simplificada para el ejemplo)
    filas = []
    # ... (Aquí va tu lógica de iteración sobre eventos) ...
    
    # Simulación de carga para demostración en GitHub
    df = pd.DataFrame(filas)
    if not df.empty:
        # df.to_sql("hechos", con=engine, if_exists="append", index=False)
        print(f"✅ Procesamiento completado: {len(df)} eventos detectados.")

if __name__ == "__main__":
    # Uso de ruta relativa para que funcione en cualquier computadora
    directorio_actual = os.path.dirname(__file__)
    ruta_partido = os.path.join(directorio_actual, "partido_ejemplo.txt")
    cargar_partido(ruta_partido)
