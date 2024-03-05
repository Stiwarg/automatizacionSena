@extends('layouts.main_template')
@section('contenido')

<h1>Editar Contratista</h1>

<form method="POST" action="{{ route('contractors.update', $contractor->id) }}">
    @csrf
    @method('PUT')

    <div class="form-group">
        <label for="identificacion">Identificación</label>
        <input type="text" class="form-control" id="identificacion" name="identificacion" value="{{ $contractor->identificacion }}" readonly>
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

    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
</form>

@endsection
