from fastapi import APIRouter, HTTPException
from app.models import (
    Cliente, ClienteCreate, Productor, ProductorCreate,
    Inventario, InventarioCreate, Venta, VentaCreate,
    Transporte, TransporteCreate, Pago, PagoCreate
)
from app.DB_connection import get_db_connection
from typing import List

router = APIRouter()

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
def bulk_insert_clientes(clientes: List[ClienteCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO clientes (nombre, apellido, direccion, telefono, email) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono, cliente.email) 
                for cliente in clientes]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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
def bulk_insert_productores(productores: List[ProductorCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO productores (nombre, apellido, direccion, correo, telefono, fecha_ingreso, area_cultivo, tipo_cultivo) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = [(productor.nombre, productor.apellido, productor.direccion, productor.correo, productor.telefono, 
                productor.fecha_ingreso, productor.area_cultivo, productor.tipo_cultivo) 
                for productor in productores]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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

@router.post("/inventario/", response_model=dict)
def bulk_insert_inventario(inventarios: List[InventarioCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO inventario (id_productor, fecha_actualizacion, cantidad_kilos_disponible) 
        VALUES (%s, %s, %s)
        """
        values = [(inventario.id_productor, inventario.fecha_actualizacion, inventario.cantidad_kilos_disponible) 
                for inventario in inventarios]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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
def bulk_insert_ventas(ventas: List[VentaCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO ventas (id_productor, fecha_venta, cantidad_kilos, precio_por_kilo, total_venta, id_cliente) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = [(venta.id_productor, venta.fecha_venta, venta.cantidad_kilos, venta.precio_por_kilo, 
                venta.total_venta, venta.id_cliente) 
                for venta in ventas]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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
def bulk_insert_transportes(transportes: List[TransporteCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO transportes (id_venta, fecha_envio, empresa_transporte, costo_envio) 
        VALUES (%s, %s, %s, %s)
        """
        values = [(transporte.id_venta, transporte.fecha_envio, transporte.empresa_transporte, transporte.costo_envio) 
                for transporte in transportes]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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
def bulk_insert_pagos(pagos: List[PagoCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO pagos (id_venta, fecha_pago, monto, estado) 
        VALUES (%s, %s, %s, %s)
        """
        values = [(pago.id_venta, pago.fecha_pago, pago.monto, pago.estado) 
                for pago in pagos]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/max_kilos_productor/")
def max_kilos_productor():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT p.nombre, p.apellido, MAX(v.cantidad_kilos) AS max_kilos
        FROM productores p
        INNER JOIN ventas v ON p.id_productor = v.id_productor
        GROUP BY p.nombre, p.apellido
        ORDER BY max_kilos DESC
        LIMIT 1
        """
        cursor.execute(query)
        row = cursor.fetchone()
        return {"nombre": row[0], "apellido": row[1], "max_kilos": row[2]}
    finally:
        cursor.close()
        conn.close()

@router.get("/avg_kilos_por_productor/")
def avg_kilos_por_productor():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT p.nombre, p.apellido, AVG(v.cantidad_kilos) AS avg_kilos
        FROM productores p
        LEFT JOIN ventas v ON p.id_productor = v.id_productor
        GROUP BY p.nombre, p.apellido
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"nombre": row[0], "apellido": row[1], "avg_kilos": row[2]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/cliente_max_compra/")
def cliente_max_compra():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT c.nombre, c.apellido, MAX(v.total_venta) AS max_compra
        FROM clientes c
        INNER JOIN ventas v ON c.id_cliente = v.id_cliente
        GROUP BY c.nombre, c.apellido
        ORDER BY max_compra DESC
        LIMIT 1
        """
        cursor.execute(query)
        row = cursor.fetchone()
        return {"nombre": row[0], "apellido": row[1], "max_compra": row[2]}
    finally:
        cursor.close()
        conn.close()

@router.get("/avg_costo_por_empresa/")
def avg_costo_por_empresa():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT t.empresa_transporte, AVG(t.costo_envio) AS avg_costo
        FROM transportes t
        GROUP BY t.empresa_transporte
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"empresa_transporte": row[0], "avg_costo": row[1]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/venta_min_transporte/")
def venta_min_transporte():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT v.id_venta, MIN(t.costo_envio) AS min_costo
        FROM ventas v
        INNER JOIN transportes t ON v.id_venta = t.id_venta
        GROUP BY v.id_venta
        ORDER BY min_costo
        LIMIT 1
        """
        cursor.execute(query)
        row = cursor.fetchone()
        return {"id_venta": row[0], "min_costo": row[1]}
    finally:
        cursor.close()
        conn.close()

@router.get("/total_ventas_por_cliente/")
def total_ventas_por_cliente():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT c.nombre, c.apellido, SUM(v.total_venta) AS total_ventas
        FROM clientes c
        LEFT JOIN ventas v ON c.id_cliente = v.id_cliente
        GROUP BY c.nombre, c.apellido
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"nombre": row[0], "apellido": row[1], "total_ventas": row[2]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/inventarios_mas_de_100_kilos/")
def inventarios_mas_de_100_kilos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT * FROM inventario
        WHERE cantidad_kilos_disponible > 100
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"id_inventario": row[0], "id_productor": row[1], "fecha_actualizacion": row[2], "cantidad_kilos_disponible": row[3]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/clientes_sin_compras/")
def clientes_sin_compras():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT c.nombre, c.apellido
        FROM clientes c
        LEFT JOIN ventas v ON c.id_cliente = v.id_cliente
        WHERE v.id_cliente IS NULL
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"nombre": row[0], "apellido": row[1]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/ventas_por_fecha/")
def ventas_por_fecha():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT v.fecha_venta, COUNT(*) AS num_ventas
        FROM ventas v
        GROUP BY v.fecha_venta
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"fecha_venta": row[0], "num_ventas": row[1]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/max_area_cultivo/")
def max_area_cultivo():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT nombre, apellido, MAX(area_cultivo) AS max_area
        FROM productores
        GROUP BY nombre, apellido
        ORDER BY max_area DESC
        LIMIT 1
        """
        cursor.execute(query)
        row = cursor.fetchone()
        return {"nombre": row[0], "apellido": row[1], "max_area": row[2]}
    finally:
        cursor.close()
        conn.close()

@router.get("/avg_monto_pagos/")
def avg_monto_pagos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT AVG(monto) AS avg_monto
        FROM pagos
        """
        cursor.execute(query)
        row = cursor.fetchone()
        return {"avg_monto": row[0]}
    finally:
        cursor.close()
        conn.close()

@router.get("/num_ventas_por_productor/")
def num_ventas_por_productor():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT p.nombre, p.apellido, COUNT(v.id_venta) AS num_ventas
        FROM productores p
        INNER JOIN ventas v ON p.id_productor = v.id_productor
        GROUP BY p.nombre, p.apellido
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"nombre": row[0], "apellido": row[1], "num_ventas": row[2]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/clientes_compras_sobre_promedio/")
def clientes_compras_sobre_promedio():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT c.nombre, c.apellido, SUM(v.total_venta) AS total_ventas
        FROM clientes c
        INNER JOIN ventas v ON c.id_cliente = v.id_cliente
        GROUP BY c.nombre, c.apellido
        HAVING SUM(v.total_venta) > (SELECT AVG(total_venta) FROM ventas)
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"nombre": row[0], "apellido": row[1], "total_ventas": row[2]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/kilos_por_tipo_cultivo/")
def kilos_por_tipo_cultivo():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT c.tipo_cultivo, SUM(v.cantidad_kilos) AS total_kilos
        FROM cultivo c
        INNER JOIN ventas v ON c.id_cultivo = v.id_cultivo
        GROUP BY c.tipo_cultivo
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"tipo_cultivo": row[0], "total_kilos": row[1]} for row in rows]
    finally:
        cursor.close()
        conn.close()

@router.get("/num_transportes_por_empresa/")
def num_transportes_por_empresa():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        SELECT empresa_transporte, COUNT(*) AS num_transportes
        FROM transportes
        GROUP BY empresa_transporte
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [{"empresa_transporte": row[0], "num_transportes": row[1]} for row in rows]
    finally:
        cursor.close()
        conn.close()
