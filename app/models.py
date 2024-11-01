from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class ClienteCreate(BaseModel):
    nombre: str = Field(..., max_length=50, description="Nombre del cliente (campo requerido)")
    apellido: str = Field(..., max_length=50, description="Apellido del cliente (campo requerido)")
    direccion: Optional[str] = Field(None, max_length=100, description="Dirección del cliente")
    telefono: Optional[str] = Field(None, max_length=20, description="Teléfono del cliente")
    email: Optional[EmailStr] = Field(None, max_length=100, description="Correo electrónico del cliente")

class Cliente(ClienteCreate):
    id_cliente: int

class ProductorCreate(BaseModel):
    nombre: str = Field(..., max_length=100, description="Nombre del productor (campo requerido)")
    apellido: str = Field(..., max_length=100, description="Apellido del productor (campo requerido)")
    direccion: Optional[str] = Field(None, max_length=255, description="Dirección del productor")
    correo: Optional[EmailStr] = Field(None, max_length=100, description="Correo electrónico del productor")
    telefono: Optional[str] = Field(None, max_length=20, description="Teléfono del productor")
    fecha_ingreso: date = Field(..., description="Fecha de ingreso del productor")
    area_cultivo: float = Field(..., description="Área de cultivo en hectáreas")
    tipo_cultivo: Optional[str] = Field(None, max_length=100, description="Tipo de cultivo")

class Productor(ProductorCreate):
    id_productor: int

class InventarioCreate(BaseModel):
    id_productor: int = Field(..., description="ID del productor asociado (campo requerido)")
    fecha_actualizacion: date = Field(..., description="Fecha de actualización del inventario")
    cantidad_kilos_disponible: float = Field(..., description="Cantidad de kilos disponibles")

class Inventario(InventarioCreate):
    id_inventario: int

class VentaCreate(BaseModel):
    id_productor: int = Field(..., description="ID del productor asociado (campo requerido)")
    fecha_venta: date = Field(..., description="Fecha de la venta")
    cantidad_kilos: float = Field(..., description="Cantidad de kilos vendidos")
    precio_por_kilo: float = Field(..., description="Precio por kilo")
    total_venta: float = Field(..., description="Total de la venta calculado")
    id_cliente: int = Field(..., description="ID del cliente asociado (campo requerido)")

class Venta(VentaCreate):
    id_venta: int

class TransporteCreate(BaseModel):
    id_venta: int = Field(..., description="ID de la venta asociada (campo requerido)")
    fecha_envio: date = Field(..., description="Fecha del envío")
    empresa_transporte: Optional[str] = Field(None, max_length=100, description="Nombre de la empresa de transporte")
    costo_envio: float = Field(..., description="Costo del envío")

class Transporte(TransporteCreate):
    id_transporte: int

class PagoCreate(BaseModel):
    id_venta: int = Field(..., description="ID de la venta asociada (campo requerido)")
    fecha_pago: date = Field(..., description="Fecha del pago")
    monto: float = Field(..., description="Monto del pago")
    estado: Optional[str] = Field(None, max_length=20, description="Estado del pago (por ejemplo: 'Completado', 'Pendiente')")

class Pago(PagoCreate):
    id_pago: int

