from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Venta
from django.http import HttpResponse

# Vista de inicio
def inicio_videojuegos(request):
    return render(request, 'cliente/inicio.html')

# Agregar Cliente
def agregar_cliente(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        empleado_obj = None
        if empleado_id:
            try:
                empleado_obj = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                empleado_obj = None

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion,
            empleado_asignado=empleado_obj,
            producto_interes=producto_interes,
            imagen=imagen
        )
        return redirect('ver_clientes')

    return render(request, 'cliente/agregar_cliente.html', {'empleados': empleados})

# Ver Clientes
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# Actualizar Cliente
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        cliente.producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        if empleado_id:
            try:
                cliente.empleado_asignado = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                cliente.empleado_asignado = None
        else:
            cliente.empleado_asignado = None

        if imagen:
            cliente.imagen = imagen

        cliente.save()
        return redirect('ver_clientes')

    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente, 'empleados': empleados})

# Borrar Cliente
def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# Agregar Empleado
def agregar_empleado(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        cliente_id = request.POST.get('cliente_referido')
        producto_asignado = request.POST.get('producto_asignado')
        imagen = request.FILES.get('imagen')

        cliente_obj = None
        if cliente_id:
            try:
                cliente_obj = Cliente.objects.get(id=cliente_id)
            except Cliente.DoesNotExist:
                cliente_obj = None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            cliente_referido=cliente_obj,
            producto_asignado=producto_asignado,
            imagen=imagen
        )
        return redirect('ver_empleados')

    return render(request, 'cliente/agregar_empleado.html', {'clientes': clientes})

# Ver Empleados
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'cliente/ver_empleados.html', {'empleados': empleados})

# Actualizar Empleado
def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        cliente_id = request.POST.get('cliente_referido')
        empleado.producto_asignado = request.POST.get('producto_asignado')
        imagen = request.FILES.get('imagen')

        if cliente_id:
            try:
                empleado.cliente_referido = Cliente.objects.get(id=cliente_id)
            except Cliente.DoesNotExist:
                empleado.cliente_referido = None
        else:
            empleado.cliente_referido = None

        if imagen:
            empleado.imagen = imagen

        empleado.save()
        return redirect('ver_empleados')

    return render(request, 'cliente/actualizar_empleado.html', {'empleado': empleado, 'clientes': clientes})

# Borrar Empleado
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'cliente/borrar_empleado.html', {'empleado': empleado})
