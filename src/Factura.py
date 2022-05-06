from dataclasses import dataclass
from productos.Productos import Productos
from facturas.LineaFactura import LineaFactura


@dataclass
class Factura:
    def __init__(self):
        self.lineasFactura: list[LineaFactura]=[]

    def recuperarLineasFactura(self) -> list[LineaFactura]:
        return self.lineaFacturas


    def añadirLineaFactura(self,lineaFactura:LineaFactura) ->None:
        self.lineasFactura.append(lineaFactura)


    def establecerProductos(self, productos:Productos) ->None:
        self.productos=productos


    def __repr__(self) -> str:
        cadena= 'LINEAS'
        total: float=0
        for lineaFactura in self.lineasFactura:
            producto=self.productos.recuperar(lineaFactura.producto)
            cadena += f'\n\t{lineaFactura.cantidad} unidades de {producto.nombre}: '
            cadena += f'{lineaFactura.cantidad*producto.precio} euros '
            total += f'\n\t TOTAL: {total}'
            return cadena