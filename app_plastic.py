import os
# --------------- variables -------------
op_menu = ""          # Selección menú principal
op_producto = ""      # Selección menú productos
nombre_producto = ""  # Nombre del producto
op_tipo_cliente = ""  # Selección General/Socio
tipo_cliente = ""     # General / Socio
valor_producto = 0    # valor por 1 producto
cantidad = 0          # Cantidad a compra
en_efectivo = "N"     # S/N -> Paga en efectivo o NO
monto_descuento = 0   # monto del dscto aplicado
subtotal = 0          # Precio X Cantidad
total_pagar = 0       # monto final a pagar
mensaje = ""            # mensaje para el ticket
# --- estadísticas --
recaudacion_total = 0   # acumulador!!!
cant_prod_vendidos = 0  # acumulador!!!
# ---------- Código Principal ----------------

while True:
    mensaje=""  #---> se reinicia la variable
    os.system("cls")
    op_menu = str(input('''
    ============ APP PLASTIC ===================
    1. Realizar venta
    2. Ver estadísticas
    3. Salir
    \n Elija opción:  '''))

    if op_menu == "1":
        os.system("cls")
        print("\n-------- REALIZAR VENTA -----")
        op_producto = str(input('''
        Producto \t\t Valor General \t Valor Socio
        1.- Tazón \t\t $800 \t\t $500
        2.- Llavero \t\t $500 \t\t $300
        3.- Polera estampada \t $5.000 \t $3.000
        \n ELija opción:       '''))

        if op_producto == "1":
            nombre_producto = "Tazón"
            op_tipo_cliente = str(input(f'''
            Selección {nombre_producto}
            Ingrese el tipo de cliente
            (1)General \t (2)Socio

            Ingrese opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 800
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 500

        if op_producto == "2":
            nombre_producto = "LLavero"
            op_tipo_cliente = str(input(f'''
            Selección {nombre_producto}
            Ingrese el tipo de cliente
            (1)General \t (2)Socio

            Ingrese opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 500
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 300

        if op_producto == "3":
            nombre_producto = "Polera estampada"
            op_tipo_cliente = str(input(f'''
            Selección {nombre_producto}
            Ingrese el tipo de cliente
            (1)General \t (2)Socio

            Ingrese opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 5000
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 3000

        cantidad = int(input(f'''
        Esta comprando {nombre_producto}
        A un valor de {valor_producto} c/u

        Ingrese la cantidad: '''))

        while not cantidad > 0:
            print("Error, mínimo 1 producto")
            cantidad = int(input(f'''
            Esta comprando {nombre_producto}
            A un valor de {valor_producto} c/u

            Ingrese la cantidad: '''))

        subtotal = cantidad*valor_producto

        en_efectivo = str(input(f'''
        Subtotal ${subtotal}

        Si paga en efectivo tendrá 20% dscto.

        ¿Paga en efectivo? S/N  ''')).strip().upper()

        if en_efectivo == "S":
            monto_descuento = subtotal*0.20
            mensaje= f"Descuento pago efectivo 20% ${monto_descuento}"

        total_pagar = subtotal-monto_descuento
        
        #----- imprimir ticket ----
        os.system("cls")
        print(f'''
        ------- TICKET COMPRA -----
        Producto: {nombre_producto}
        Cantidad de entradas: {cantidad}	
        Tipo cliente: {tipo_cliente} 
        Subtotal ${subtotal}
        {mensaje}
        Total pagar ${total_pagar}  ''')        

        os.system("pause")
