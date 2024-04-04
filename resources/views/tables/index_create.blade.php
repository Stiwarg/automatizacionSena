@extends('layouts.main_template')

@section('contenido')

<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">Agregar Nuevo Instructor</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <form action="{{ route('Create.store') }}" method="POST">
                    @csrf
                    <div class="form-group">
                        <label for="nombre">Nombre</label>
                        <input type="text" id="nombre" name="nombre" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="correo">Correo Electrónico</label>
                        <input type="email" id="correo" name="correo" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="telefono">Teléfono</label>
                        <input type="text" id="telefono" name="telefono" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="identificacion">Identificacion</label>
                        <input type="text" id="identificacion" name="identificacion" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="tipo_contratos_id">tipo_contratos_id</label>
                        <input type="text" id="tipo_contratos_id" name="tipo_contratos_id" class="form-control">
                    </div>
                    {{-- <div class="form-group">
                        <label for="identificacion">Identificacion</label>
                        <input type="text" id="identificacion" name="identificacion" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="identificacion">Identificacion</label>
                        <input type="text" id="identificacion" name="identificacion" class="form-control">
                    </div> --}}
                    <div class="form-group">
                        <label for="habilitacion">abilitacion</label>
                        <input type="text" id="habilitacion" name="habilitacion" class="form-control">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Guardar</button>
                    </div>
                </form>
            </div>
            <!-- /.card-body -->
        </div>
        <!-- /.card -->
    </div>
    <!-- /.col -->
</div>
<!-- /.row -->

@endsection
