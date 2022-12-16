class Transaccion:
  def __init__(self, fecha, cantidad, descripcion):
    self.fecha = fecha
    self.cantidad = cantidad
    self.descripcion = descripcion
  def mostrar_transaccion(self):
    print(f"Fecha de transacción: {self.fecha}")
    print(f"Cantidad: {self.cantidad}")
    print(f"Descripción: {self.descripcion}\n")

t = Transaccion("05-12-2022", 250, "Compra en el MediaMarkt")
t2 = Transaccion("06-12-2022", 150, "Compra en el supermercado")
t.mostrar_transaccion()
t2.mostrar_transaccion()

class ListaTransacciones:
  def __init__(self):
    self.transacciones = []
 
  def agregar_transaccion(self, transaccion):
    self.transacciones.append(transaccion)
    
  def eliminar_transaccion(self, transaccion):
    self.transacciones.remove(transaccion)

  def obtener_ingresos_totales(self, fecha_inicio, fecha_fin):
    ingresos = 0
    for transaccion in self.transacciones:
      if transaccion.fecha >= fecha_inicio and transaccion.fecha <= fecha_fin:
        ingresos += transaccion.cantidad
    return ingresos

  def obtener_gastos_totales(self, fecha_inicio, fecha_fin):
    gastos = 0
    for transaccion in self.transacciones:
      if transaccion.fecha >= fecha_inicio and transaccion.fecha <= fecha_fin:
        gastos -= transaccion.cantidad
    return gastos

  def obtener_ingreso_neto(self, fecha_inicio, fecha_fin):
    ingresos = self.obtener_ingresos_totales(fecha_inicio, fecha_fin)
    gastos = self.obtener_gastos_totales(fecha_inicio, fecha_fin)
    return ingresos + gastos

# ListaTransacciones() crea una lista vacía de transacciones.
# Sería como inicializar la lista y a continuación añadirle (t)
lista_t = ListaTransacciones()
lista_t2 = ListaTransacciones()
lista_t.agregar_transaccion(t)
lista_t2.agregar_transaccion(t2)

class Reporte:
  def __init__(self, lista_transacciones):
    self.lista_transacciones = lista_transacciones

  def generar_reporte(self, fecha_inicio, fecha_fin):
    ingresos = self.lista_transacciones.obtener_ingresos_totales(fecha_inicio, fecha_fin)
    gastos = self.lista_transacciones.obtener_gastos_totales(fecha_inicio, fecha_fin)
    ingreso_neto = self.lista_transacciones.obtener_ingreso_neto(fecha_inicio, fecha_fin)
    print(f"Ingresos totales: {ingresos}")
    print(f"Gastos totales: {gastos}")
    print(f"Ingreso neto: {ingreso_neto}\n")

reporte = Reporte(lista_t)
reporte2 = Reporte(lista_t2)
reporte.generar_reporte("05-12-2022", "10-12-2022")
reporte2.generar_reporte("05-12-2022", "10-12-2022")