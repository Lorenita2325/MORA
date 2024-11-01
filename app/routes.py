from fastapi import APIRouter, HTTPException
from app.models import (
    Cliente, ClienteCreate, Productor, ProductorCreate,
    Inventario, InventarioCreate, Venta, VentaCreate,
    Transporte, TransporteCreate, Pago, PagoCreate
)
from app.DB_connection import get_db_connection
from typing import List

router = APIRouter()

# Endpoints para clientes
@router.get("/clientes/", response_model=List[Cliente])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        return [Cliente(id_cliente=row[0], nombre=row[1], apellido=row[2], direccion=row[3], telefono=row[4], email=row[5]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/clientes/", response_model=dict)
def create_cliente(cliente: ClienteCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO clientes (nombre, apellido, direccion, telefono, email) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono, cliente.email)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Cliente creado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para productores
@router.get("/productores/", response_model=List[Productor])
def get_productores():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM productores")
        rows = cursor.fetchall()
        return [Productor(id_productor=row[0], nombre=row[1], apellido=row[2], direccion=row[3], correo=row[4],
                        telefono=row[5], fecha_ingreso=row[6], area_cultivo=row[7], tipo_cultivo=row[8]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/productores/", response_model=dict)
def create_productor(productor: ProductorCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO productores (nombre, apellido, direccion, correo, telefono, fecha_ingreso, area_cultivo, tipo_cultivo) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (productor.nombre, productor.apellido, productor.direccion, productor.correo, productor.telefono,
                productor.fecha_ingreso, productor.area_cultivo, productor.tipo_cultivo)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Productor creado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para inventarios
@router.get("/inventarios/", response_model=List[Inventario])
def get_inventarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM inventario")
        rows = cursor.fetchall()
        return [Inventario(id_inventario=row[0], id_productor=row[1], fecha_actualizacion=row[2], cantidad_kilos_disponible=row[3]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/inventarios/", response_model=dict)
def create_inventario(inventario: InventarioCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO inventario (id_productor, fecha_actualizacion, cantidad_kilos_disponible) 
        VALUES (%s, %s, %s)
        """
        values = (inventario.id_productor, inventario.fecha_actualizacion, inventario.cantidad_kilos_disponible)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Inventario creado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para ventas
@router.get("/ventas/", response_model=List[Venta])
def get_ventas():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM ventas")
        rows = cursor.fetchall()
        return [Venta(id_venta=row[0], id_productor=row[1], fecha_venta=row[2], cantidad_kilos=row[3], 
                    precio_por_kilo=row[4], total_venta=row[5], id_cliente=row[6]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/ventas/", response_model=dict)
def create_venta(venta: VentaCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO ventas (id_productor, fecha_venta, cantidad_kilos, precio_por_kilo, total_venta, id_cliente) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (venta.id_productor, venta.fecha_venta, venta.cantidad_kilos, venta.precio_por_kilo, 
                venta.total_venta, venta.id_cliente)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Venta creada exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para transportes
@router.get("/transportes/", response_model=List[Transporte])
def get_transportes():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM transportes")
        rows = cursor.fetchall()
        return [Transporte(id_transporte=row[0], id_venta=row[1], fecha_envio=row[2], empresa_transporte=row[3], costo_envio=row[4]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/transportes/", response_model=dict)
def create_transporte(transporte: TransporteCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO transportes (id_venta, fecha_envio, empresa_transporte, costo_envio) 
        VALUES (%s, %s, %s, %s)
        """
        values = (transporte.id_venta, transporte.fecha_envio, transporte.empresa_transporte, transporte.costo_envio)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Transporte creado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para pagos
@router.get("/pagos/", response_model=List[Pago])
def get_pagos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM pagos")
        rows = cursor.fetchall()
        return [Pago(id_pago=row[0], id_venta=row[1], fecha_pago=row[2], monto=row[3], estado=row[4]) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/pagos/", response_model=dict)
def create_pago(pago: PagoCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO pagos (id_venta, fecha_pago, monto, estado) 
        VALUES (%s, %s, %s, %s)
        """
        values = (pago.id_venta, pago.fecha_pago, pago.monto, pago.estado)
        
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Pago creado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

