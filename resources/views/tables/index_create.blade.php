@extends('layouts.main_template')
@section('contenido')

<h1>Nuevo Intructor</h1>

<form method="POST" action="{{ route('create.store') }}">
    @csrf
    
    <!-- Agrega un campo oculto para almacenar la URL de origen -->
    <input type="hidden" name="previous_url" value="{{ URL::previous() }}">
    
    
    <div class="form-group">
        <label for="nombre">Nombre</label>
        <input type="text" class="form-control" id="nombre" name="nombre" >
    </div>

    <div class="form-group">
        <label for="apellido">Apellido</label>
        <input type="text" class="form-control" id="apellido" name="apellido" >
    </div>

    <div class="form-group">
        <label for="identificacion">Identificación</label>
        <input type="text" class="form-control" id="identificacion" name="identificacion" >
    </div>

    <div class="form-group">
        <label for="programa">Programa</label>
        <input type="text" class="form-control" id="programa" name="programa" >
    </div>
    <div class="form-group">
        <label for="supervisor">Supervisor</label>
        <input type="text" class="form-control" id="supervisor" name="supervisor" >
    </div>

    <div class="form-group">
        <label for="correo">Correo</label>
        <input type="email" class="form-control" id="correo" name="correo" >
    </div>

    <div class="form-group">
        <label for="telefono">Teléfono</label>
        <input type="text" class="form-control" id="telefono" name="telefono">
    </div>
    <div class="form-group">
        <label for="celular">Celular</label>
        <input type="text" class="form-control" id="celular" name="celular" >
    </div>
    <div class="form-group">
        <label for="direccion">Direccion</label>
        <input type="text" class="form-control" id="direccion" name="direccion" >
    </div>
    {{-- <div class="form-group">
        <label for="habilitacion">Estado</label>
        <select class="form-control" id="habilitacion" name="habilitacion">
            <option value="0" >Activo</option>
            <option value="1" >Inactivo</option>
        </select>
    </div> --}}

    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
</form>

@endsection
