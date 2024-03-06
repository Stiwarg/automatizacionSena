@extends('layouts.main_template')
@section('contenido')

<h1>Editar Informacion</h1>

<form method="POST" action="{{ route('contractors.update', $contractor->id) }}">
    @csrf
    @method('PUT')
    
    <!-- Agrega un campo oculto para almacenar la URL de origen -->
    <input type="hidden" name="previous_url" value="{{ URL::previous() }}">

    <div class="form-group">
        <label for="identificacion">Identificación</label>
        <input type="text" class="form-control" id="identificacion" name="identificacion" value="{{ $contractor->identificacion }}">
    </div>

    <div class="form-group">
        <label for="nombre">Nombre</label>
        <input type="text" class="form-control" id="nombre" name="nombre" value="{{ $contractor->nombre }}">
    </div>

    <div class="form-group">
        <label for="correo">Correo</label>
        <input type="email" class="form-control" id="correo" name="correo" value="{{ $contractor->correo }}">
    </div>

    <div class="form-group">
        <label for="telefono">Teléfono</label>
        <input type="text" class="form-control" id="telefono" name="telefono" value="{{ $contractor->telefono }}">
    </div>

    <div class="form-group">
        <label for="habilitacion">Estado</label>
        <select class="form-control" id="habilitacion" name="habilitacion">
            <option value="0" {{ $contractor->habilitacion == 0 ? 'selected' : '' }}>Activo</option>
            <option value="1" {{ $contractor->habilitacion == 1 ? 'selected' : '' }}>Inactivo</option>
        </select>
    </div>

    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
</form>

@endsection
