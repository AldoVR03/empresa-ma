from django.db import models

class Administrador(models.Model):
    idAdministrador = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    correo = models.EmailField()

class Capacitacion(models.Model):
    idCapacitacion = models.AutoField(primary_key=True)
    nombreCapacitacion = models.CharField(max_length=100)
    fechaDeEmicion = models.CharField(max_length=50)

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=50)
    rutEmpresa = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)
    celular_Telefono = models.IntegerField(null=True, blank=True)
    correo = models.EmailField()
    password = models.CharField(max_length=50)

class Cotizacion(models.Model):
    idServicio = models.ForeignKey('Servicio', on_delete=models.RESTRICT)
    idCotizacion = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    nombreProyecto = models.CharField(max_length=1)
    costoTotal = models.IntegerField()
    descripcion = models.CharField(max_length=1)
    fecha = models.CharField(max_length=1)

class Empleados(models.Model):
    idEmpleados = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.IntegerField(null=True, blank=True)
    correo = models.EmailField()
    capacitacion = models.CharField(max_length=50)

class GerenteAdmin(models.Model):
    idGerenteAdmin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    correo = models.EmailField()

class GestionNomina(models.Model):
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.RESTRICT)
    idGestionNomina = models.AutoField(primary_key=True)
    sueldo = models.IntegerField()
    horasTrabajadas = models.IntegerField()
    descansos = models.CharField(max_length=50)
    tipoPago = models.CharField(max_length=50)

class HistorialLaboral(models.Model):
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.RESTRICT)
    idHistoriaLab = models.AutoField(primary_key=True)
    permisos = models.CharField(max_length=50)
    licenciasMedicas = models.CharField(max_length=50)
    fallas = models.CharField(max_length=50)
    comportamiento = models.CharField(max_length=50)
    despido_Renuncia = models.BooleanField()

class Inventario(models.Model):
    idArticulo = models.AutoField(primary_key=True)
    nombreArticulo = models.CharField(max_length=50)
    estadoArticulo = models.CharField(max_length=50)
    catindad = models.IntegerField()

class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombreServicio = models.CharField(max_length=50)
    costo = models.IntegerField()

class Association5(models.Model):
    idCapacitacion = models.ForeignKey(Capacitacion, on_delete=models.RESTRICT)
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.RESTRICT)
