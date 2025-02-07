import json
from django.db import connection
from django.shortcuts import render
from decimal import Decimal
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "home.html")

def ejecutar_consulta(sql):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()
    return resultados


TRADUCCION_MESES = {
    "January": "Enero", "February": "Febrero", "March": "Marzo", "April": "Abril",
    "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto",
    "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"
}

def obtener_recaudacion_por_mes():
    """1. Recaudación por mes del año anterior"""
    sql = """
        SELECT 
                YEAR(r.fecha_emision_rec) AS anio,
                MONTHNAME(r.fecha_emision_rec) AS mes_nombre,
                SUM(d.subtotal_det + d.iva_det) AS total_ingresos
            FROM recaudacion r
            JOIN detalle d ON r.id_rec = d.fk_id_rec
            WHERE YEAR(r.fecha_emision_rec) = 2024 
            GROUP BY anio, mes_nombre
            ORDER BY anio DESC, FIELD(mes_nombre, 'January', 'February', 'March', 'April', 
                'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');
    """
    return [{"mes": TRADUCCION_MESES.get(row[1], row[1]), "total_ingresos": float(row[2])} for row in ejecutar_consulta(sql)]

def obtener_recaudacion_anual():
    """2. Recaudación total por año"""
    sql = """
        SELECT 
            YEAR(r.fecha_emision_rec) AS anio,
            SUM(d.subtotal_det + d.iva_det) AS total_recaudacion
        FROM recaudacion r
        JOIN detalle d ON r.id_rec = d.fk_id_rec
        GROUP BY anio
        ORDER BY anio DESC;
    """
    return [{"anio": row[0], "total_recaudacion": float(row[1])} for row in ejecutar_consulta(sql)]

def obtener_facturacion_por_socio():
    """3. Facturación por socio (Top 10)"""
    sql = """
        SELECT 
            s.id_soc,
            CONCAT(s.nombres_soc, ' ', s.primer_apellido_soc) AS nombre,
            SUM(d.subtotal_det + d.iva_det) AS total_facturado
        FROM recaudacion r
        JOIN socio s ON r.fk_id_soc = s.id_soc
        JOIN detalle d ON r.id_rec = d.fk_id_rec
        GROUP BY s.id_soc, nombre
        ORDER BY total_facturado DESC
        LIMIT 10;
    """
    return [{"nombre": row[1], "total_facturado": float(row[2])} for row in ejecutar_consulta(sql)]

def obtener_tipos_de_socios():
    """4. Tipos de socios"""
    sql = """
        SELECT 
            tipo_soc,
            COUNT(*) AS total_socios
        FROM socio
        GROUP BY tipo_soc
        ORDER BY total_socios DESC;
    """
    return [{"tipo": row[0], "total_socios": row[1]} for row in ejecutar_consulta(sql)]

def obtener_clientes_mayor_consumo():
    """5. Clientes con mayor consumo"""
    sql = """
        SELECT 
            s.nombres_soc, 
            SUM(l.lectura_actual_lec - l.lectura_anterior_lec) AS consumo_total
        FROM lectura l
        JOIN historial_propietario h ON l.fk_id_his = h.id_his
        JOIN socio s ON h.fk_id_soc = s.id_soc
        GROUP BY s.nombres_soc
        ORDER BY consumo_total DESC
        LIMIT 10;
    """
    return [{"nombre": row[0], "consumo_total": float(row[1])} for row in ejecutar_consulta(sql)]

def obtener_medidores_mayor_consumo():
    """6. Medidores con mayor consumo"""
    sql = """
        SELECT 
            m.numero_med,
            SUM(l.lectura_actual_lec - l.lectura_anterior_lec) AS consumo_total
        FROM lectura l
        JOIN medidor m ON l.fk_id_his = m.id_med
        GROUP BY m.numero_med
        ORDER BY consumo_total DESC
        LIMIT 10;
    """
    return [{"medidor": row[0], "consumo_total": float(row[1])} for row in ejecutar_consulta(sql)]

def obtener_dia_mas_asistencias():
    """7. Día de la semana con más asistencias"""
    sql = """
        SELECT 
            DAYNAME(e.fecha_hora_eve) AS dia_semana,
            COUNT(a.id_asi) AS total_asistencias
        FROM asistencia a
        JOIN evento e ON a.fk_id_eve = e.id_eve
        GROUP BY dia_semana
        ORDER BY total_asistencias DESC
        LIMIT 2;
    """
    return [{"dia": row[0], "total_asistencias": row[1]} for row in ejecutar_consulta(sql)]

def obtener_crecimiento_facturacion():
    """8. Crecimiento de facturación anual"""
    sql = """
        SELECT 
            YEAR(r.fecha_emision_rec) AS anio,
            SUM(d.subtotal_det + d.iva_det) AS total_facturado
        FROM recaudacion r
        JOIN detalle d ON r.id_rec = d.fk_id_rec
        GROUP BY anio
        ORDER BY anio DESC;
    """
    return [{"anio": row[0], "total_facturado": float(row[1])} for row in ejecutar_consulta(sql)]

def obtener_socios_menos_participativos():
    """9. Socios con menor porcentaje de participación (Top 5)"""
    sql = """
        SELECT 
            s.nombres_soc,
            COUNT(a.id_asi) / (SELECT COUNT(*) FROM evento) * 100 AS porcentaje_participacion
        FROM socio s
        LEFT JOIN asistencia a ON s.id_soc = a.fk_id_soc
        GROUP BY s.nombres_soc
        ORDER BY porcentaje_participacion
        LIMIT 5;
    """
    return [{"nombre": row[0], "porcentaje": float(row[1])} for row in ejecutar_consulta(sql)]

def obtener_socios_mayor_recaudacion():
    """10. Socios con mayor recaudación (Top 5)"""
    sql = """
        SELECT 
            s.nombres_soc,
            AVG(d.subtotal_det + d.iva_det) AS facturacion_promedio
        FROM recaudacion r
        JOIN socio s ON r.fk_id_soc = s.id_soc
        JOIN detalle d ON r.id_rec = d.fk_id_rec
        GROUP BY s.nombres_soc
        ORDER BY facturacion_promedio DESC
        LIMIT 5;
    """
    return [{"nombre": row[0], "facturacion_promedio": float(row[1])} for row in ejecutar_consulta(sql)]


@login_required
def viewDashboards(request):
    """Carga los KPIs y los envía a la plantilla"""
    context = {
        "recaudacion_por_mes": json.dumps(obtener_recaudacion_por_mes()),
        "recaudacion_anual": json.dumps(obtener_recaudacion_anual()),
        "facturacion_por_socio": json.dumps(obtener_facturacion_por_socio()),
        "tipos_socios": json.dumps(obtener_tipos_de_socios()),
        "clientes_mayor_consumo": json.dumps(obtener_clientes_mayor_consumo()),
        "medidores_mayor_consumo": json.dumps(obtener_medidores_mayor_consumo()),
        "dia_mas_asistencias": json.dumps(obtener_dia_mas_asistencias()),
        "crecimiento_facturacion": json.dumps(obtener_crecimiento_facturacion()),
        "socios_menos_participativos": json.dumps(obtener_socios_menos_participativos()),
        "socios_mayor_recaudacion": json.dumps(obtener_socios_mayor_recaudacion()),
    }

    return render(request, "dashboards.html", context)
