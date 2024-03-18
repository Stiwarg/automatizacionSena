<!-- resources/views/instructores/create.blade.php -->

@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Crear Nuevo Instructor</div>

                    <div class="card-body">
                        <form method="POST" action="{{ route('contractor.store') }}">
                            @csrf

                            <div class="form-group">
                                <label for="nombre">Nombre</label>
                                <input type="text" id="nombre" name="nombre" class="form-control" required>
                            </div>

                            <div class="form-group">
                                <label for="apellidos">Apellidos</label>
                                <input type="text" id="apellidos" name="apellidos" class="form-control" required>
                            </div>

                            <div class="form-group">
                                <label for="identificacion">Identificación</label>
                                <input type="number" id="identificacion" name="identificacion" class="form-control" required>
                            </div>

                            <div class="form-group">
                                <label for="programa">Programa</label>
                                <input type="text" id="programa" name="programa" class="form-control" >
                            </div>

                            <div class="form-group">
                                <label for="supervisor">Supervisor</label>
                                <input type="text" id="supervisor" name="supervisor" class="form-control">
                            </div>

                            <div class="form-group">
                                <label for="correo">Correo</label>
                                <input type="email" id="correo" name="correo" class="form-control" required>
                            </div>

                            <div class="form-group">
                                <label for="telefono">Teléfono</label>
                                <input type="number" id="telefono" name="telefono" class="form-control">
                            </div>

                            <div class="form-group">
                                <label for="celular">Celular</label>
                                <input type="number" id="celular" name="celular" class="form-control" required>
                            </div>

                            <div class="form-group">
                                <label for="direccion">Dirección</label>
                                <input type="text" id="direccion" name="direccion" class="form-control">
                            </div>

                            <div class="form-group">
                                <label for="habilitacion">Habilitación</label>
                                <select id="habilitacion" name="habilitacion" class="form-control" required>
                                    <option value="0">Activo</option>
                                    <option value="1">Inactivo</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label for="tipo_contratos_id">Tipo de Contrato</label>
                                <select id="tipo_contratos_id" name="tipo_contratos_id" class="form-control" required>
                                    @foreach($contractorTypes as $contractorType)
                                        <option value="{{ $contractorType->id }}">{{ $contractorType->nombre }}</option>
                                    @endforeach
                                </select>
                            </div>
                            
                            <div class="form-group">
                                <label for="instructores_area_id">Área de Instructores</label>
                                <select id="instructores_area_id" name="instructores_area_id" class="form-control" required>
                                    @foreach($instructorAreas as $instructorArea)
                                        <option value="{{ $instructorArea->id }}">{{ $instructorArea->nombre }}</option>
                                    @endforeach
                                </select>
                            </div>

                            <button type="submit" class="btn btn-primary">Crear Instructor</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
@endsection
