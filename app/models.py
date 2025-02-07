# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistencia(models.Model):
    id_asi = models.AutoField(primary_key=True)
    fk_id_eve = models.ForeignKey('Evento', models.DO_NOTHING, db_column='fk_id_eve', blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    tipo_asi = models.CharField(max_length=100, blank=True, null=True)
    valor_asi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    atraso_asi = models.CharField(max_length=25)
    valor_atraso_asi = models.DecimalField(max_digits=10, decimal_places=2)
    creacion_asi = models.DateTimeField(blank=True, null=True)
    actualizacion_asi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'

    def __str__(self):
        return f"{self.id_asi} - {self.fk_id_eve} - {self.tipo_asi} - {self.valor_asi} - {self.atraso_asi} - {self.valor_asi}"
    


class Comunicado(models.Model):
    id_com = models.AutoField(primary_key=True)
    fecha_com = models.DateField()
    mensaje_com = models.CharField(max_length=200)
    actualizacion_com = models.DateTimeField(blank=True, null=True)
    creacion_com = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicado'

    def __str__(self):
        return f"{self.id_com} - {self.fecha_com} - {self.mensaje_com} - {self.actualizacion_com} - {self.creacion_com}"


class Configuracion(models.Model):
    id_con = models.AutoField(primary_key=True)
    nombre_con = models.CharField(max_length=250)
    ruc_con = models.CharField(max_length=13)
    logo_con = models.CharField(max_length=200, blank=True, null=True)
    telefono_con = models.CharField(max_length=50)
    direccion_con = models.CharField(max_length=50)
    email_con = models.CharField(max_length=50)
    servidor_con = models.CharField(max_length=50)
    puerto_con = models.CharField(max_length=50)
    password_con = models.CharField(max_length=50)
    creacion_con = models.DateTimeField(blank=True, null=True)
    actualizacion_con = models.DateTimeField(blank=True, null=True)
    anio_inicial_con = models.CharField(max_length=15, blank=True, null=True)
    mes_inicial_con = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracion'

    def __str__(self):
        return f"{self.id_con} - {self.nombre_con}"


class Consumo(models.Model):
    id_consumo = models.AutoField(primary_key=True)
    anio_consumo = models.IntegerField(blank=True, null=True)
    mes_consumo = models.CharField(max_length=25, blank=True, null=True)
    estado_consumo = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_consumo = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_consumo = models.DateTimeField(blank=True, null=True)
    numero_mes_consumo = models.IntegerField(blank=True, null=True)
    fecha_vencimiento_consumo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumo'

    def __str__(self):
        return f"{self.id_consumo} - {self.anio_consumo} - {self.mes_consumo}"


class Detalle(models.Model):
    id_det = models.AutoField(primary_key=True)
    fk_id_lec = models.ForeignKey('Lectura', models.DO_NOTHING, db_column='fk_id_lec', blank=True, null=True)
    fk_id_rec = models.ForeignKey('Recaudacion', models.DO_NOTHING, db_column='fk_id_rec', blank=True, null=True)
    cantidad_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    detalle_det = models.CharField(max_length=1500, blank=True, null=True)
    valor_unitario_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle'


class Evento(models.Model):
    id_eve = models.AutoField(primary_key=True)
    descripcion_eve = models.TextField(blank=True, null=True)
    fecha_hora_eve = models.DateTimeField(blank=True, null=True)
    lugar_eve = models.CharField(max_length=250, blank=True, null=True)
    fk_id_te = models.ForeignKey('TipoEvento', models.DO_NOTHING, db_column='fk_id_te', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class Excedente(models.Model):
    id_ex = models.AutoField(primary_key=True)
    id_tar = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='id_tar', blank=True, null=True)
    limite_minimo_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    limite_maximo_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion_ex = models.DateTimeField(blank=True, null=True)
    fecha_creacion_ex = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excedente'


class HistorialPropietario(models.Model):
    id_his = models.AutoField(primary_key=True)
    fk_id_med = models.ForeignKey('Medidor', models.DO_NOTHING, db_column='fk_id_med', blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    actualizacion_his = models.DateTimeField(blank=True, null=True)
    estado_his = models.CharField(max_length=50, blank=True, null=True)
    observacion_his = models.TextField(blank=True, null=True)
    fecha_cambio_his = models.DateTimeField(blank=True, null=True)
    creacion_his = models.DateTimeField(blank=True, null=True)
    propietario_actual_his = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_propietario'


class Impuesto(models.Model):
    id_imp = models.AutoField(primary_key=True)
    nombre_imp = models.CharField(max_length=100, blank=True, null=True)
    descripcion_imp = models.TextField(blank=True, null=True)
    porcentaje_imp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    retencion_imp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado_imp = models.CharField(max_length=50, blank=True, null=True)
    creacion_imp = models.DateTimeField(blank=True, null=True)
    actualizacion_imp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impuesto'


class Lectura(models.Model):
    id_lec = models.AutoField(primary_key=True)
    anio_lec = models.IntegerField(blank=True, null=True)
    mes_lec = models.CharField(max_length=25, blank=True, null=True)
    estado_lec = models.CharField(max_length=50, blank=True, null=True)
    lectura_anterior_lec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lectura_actual_lec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_creacion_lec = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_lec = models.DateTimeField(blank=True, null=True)
    fk_id_his = models.ForeignKey(HistorialPropietario, models.DO_NOTHING, db_column='fk_id_his', blank=True, null=True)
    fk_id_consumo = models.ForeignKey(Consumo, models.DO_NOTHING, db_column='fk_id_consumo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectura'


class Medidor(models.Model):
    id_med = models.AutoField(primary_key=True)
    fk_id_rut = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='fk_id_rut', blank=True, null=True)
    fk_id_tar = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='fk_id_tar', blank=True, null=True)
    numero_med = models.CharField(max_length=50, blank=True, null=True)
    serie_med = models.CharField(max_length=100, blank=True, null=True)
    marca_med = models.CharField(max_length=100, blank=True, null=True)
    observacion_med = models.TextField(blank=True, null=True)
    estado_med = models.CharField(max_length=25, blank=True, null=True)
    foto_med = models.CharField(max_length=500, blank=True, null=True)
    creacion_med = models.DateTimeField(blank=True, null=True)
    actualizacion_med = models.DateTimeField(blank=True, null=True)
    lectura_inicial_med = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medidor'


class Perfil(models.Model):
    id_per = models.AutoField(primary_key=True)
    nombre_per = models.CharField(max_length=50, blank=True, null=True)
    descripcion_per = models.TextField(blank=True, null=True)
    estado_per = models.CharField(max_length=25, blank=True, null=True)
    creacion_per = models.DateTimeField(blank=True, null=True)
    actualizacion_per = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'


class Recaudacion(models.Model):
    id_rec = models.AutoField(primary_key=True)
    numero_factura_rec = models.CharField(max_length=250, blank=True, null=True)
    numero_autorizacion_rec = models.CharField(max_length=500, blank=True, null=True)
    fecha_hora_autorizacion_rec = models.DateTimeField(blank=True, null=True)
    ambiente_rec = models.CharField(max_length=50, blank=True, null=True)
    emision_rev = models.CharField(max_length=50, blank=True, null=True)
    clave_acceso_rec = models.CharField(max_length=500, blank=True, null=True)
    email_rec = models.CharField(max_length=500, blank=True, null=True)
    observacion_rec = models.CharField(max_length=500, blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    nombre_rec = models.CharField(max_length=500, blank=True, null=True)
    identificacion_rec = models.CharField(max_length=15, blank=True, null=True)
    direccion_rec = models.CharField(max_length=500, blank=True, null=True)
    estado_rec = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision_rec = models.DateTimeField(blank=True, null=True)
    fecha_creacion_rec = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_rec = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recaudacion'


class Ruta(models.Model):
    id_rut = models.AutoField(primary_key=True)
    nombre_rut = models.CharField(max_length=500, blank=True, null=True)
    descripcion_rut = models.TextField(blank=True, null=True)
    estado_rut = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'


class Socio(models.Model):
    id_soc = models.AutoField(primary_key=True)
    tipo_soc = models.CharField(max_length=25, blank=True, null=True)
    identificacion_soc = models.CharField(max_length=13, blank=True, null=True)
    primer_apellido_soc = models.CharField(max_length=500, blank=True, null=True)
    segundo_apellido_soc = models.CharField(max_length=500, blank=True, null=True)
    nombres_soc = models.CharField(max_length=500, blank=True, null=True)
    email_soc = models.CharField(max_length=500, blank=True, null=True)
    foto_soc = models.CharField(max_length=500, blank=True, null=True)
    telefono_soc = models.CharField(max_length=15, blank=True, null=True)
    direccion_soc = models.CharField(max_length=500, blank=True, null=True)
    fecha_nacimiento_soc = models.DateField(blank=True, null=True)
    discapacidad_soc = models.CharField(max_length=25, blank=True, null=True)
    fk_id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usu', blank=True, null=True)
    estado_soc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socio'


class Tarifa(models.Model):
    id_tar = models.AutoField(primary_key=True)
    nombre_tar = models.CharField(max_length=500, blank=True, null=True)
    descripcion_tar = models.TextField(blank=True, null=True)
    estado_tar = models.CharField(max_length=25, blank=True, null=True)
    m3_maximo_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_basica_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_excedente_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_mora_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarifa'


class TipoEvento(models.Model):
    id_te = models.AutoField(primary_key=True)
    nombre_te = models.CharField(max_length=150, blank=True, null=True)
    estado_te = models.CharField(max_length=50, blank=True, null=True)
    creacion_te = models.DateTimeField(blank=True, null=True)
    actualizacion_te = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True)
    apellido_usu = models.CharField(max_length=150, blank=True, null=True)
    nombre_usu = models.CharField(max_length=150, blank=True, null=True)
    email_usu = models.CharField(max_length=150, blank=True, null=True)
    password_usu = models.CharField(max_length=500, blank=True, null=True)
    estado_usu = models.CharField(max_length=25, blank=True, null=True)
    fk_id_per = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='fk_id_per', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
