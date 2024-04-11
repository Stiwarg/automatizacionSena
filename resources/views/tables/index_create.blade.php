@extends('layouts.main_template')

@section('contenido')

<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">Agregar Nuevo Instructor</h3>
            </div>
            <div class="card-body">
                <div class="row">
                    <!-- Primera columna -->
                    <div class="col-md-6">
                        <div class="form-group">
                            <h3 class="card-title">Planilla de Excel de Planta:</h3>
                            <br>
                            <a href="{{ route('descargar.excel_planta') }}" class="btn btn-primary">Descargar</a>
                        </div>
                    </div>
                    <!-- Segunda columna -->
                    <div class="col-md-6">
                        <div class="form-group">
                            <h3 class="card-title">Planilla de Excel de Contratistas:</h3>
                            <br>
                            <a href="{{ route('descargar.excel_contratista') }}" class="btn btn-primary">Descargar</a>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <!-- Primera columna -->
                    <div class="col-md-6">
                        <div class="form-group">
                            <h3 class="card-title">Planilla de Excel de Instructores de Area de Planta:</h3>
                            <br>
                            <a href="{{ route('descargar.excel_area_planta') }}" class="btn btn-primary">Descargar</a>
                        </div>
                    </div>
                    <!-- Segunda columna -->
                    <div class="col-md-6">
                        <div class="form-group">
                            <h3 class="card-title">Planilla de Excel de Instructores de Area Contratistas:</h3>
                            <br>
                            <a href="{{ route('descargar.excel_area_contratista') }}" class="btn btn-primary">Descargar</a>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <!-- Segunda columna -->
                    <div class="col-md-7">
                        <form action="{{ route('subir.archivo.excel') }}" method="post" enctype="multipart/form-data">
                            @csrf
                            <div class="form-group mr-2">
                                <label for="archivo_excel" class="mr-2">Subir Archivo de Excel (Nota: El archivo de excel tiene que tener el mismo nombre con el que fue descargado para poder subirlo)</label>
                                <input type="file" class="form-control-file" name="archivo_excel" accept=".xlsx" onchange="checkFileCount(this)" multiple>
                                <button type="submit" class="btn btn-primary mt-2">Subir Excel</button>
                            </div>
                        </form>
                               <!-- Mostrar mensaje de error -->
                        @if (session('error'))
                            <div class="alert alert-danger mt-2">
                                {{ session('error') }}
                            </div>
                        @endif
                    </div>
                </div>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <form action="{{ route('create.store') }}" method="POST">
                    @csrf
                    <div class="form-group">
                        <label for="nombre">Nombre</label>
                        <input type="text" id="nombre" name="nombre" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="apellidos">Apellidos</label>
                        <input type="text" id="apellidos" name="apellidos" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="identificacion">Identificacion</label>
                        <input type="text" id="identificacion" name="identificacion" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="programa">Programa</label>
                        <input type="text" id="programa" name="programa" class="form-control">
                    </div>

                    <div class="form-group">
                        <label for="supervisor">Supervisor</label>
                        <input type="text" id="supervisor" name="supervisor" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="correo">Correo</label>
                        <input type="text" id="correo" name="correo" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="telefono">Telefono</label>
                        <input type="text" id="telefono" name="telefono" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="celular">Celular</label>
                        <input type="text" id="celular" name="celular" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="direccion">Direccion</label>
                        <input type="text" id="direccion" name="direccion" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="habilitacion">Habilitación</label>
                        <select class="form-control" id="habilitacion" name="habilitacion">
                            <option value="0" >Activo</option>
                            <option value="1" >Inactivo</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="tipo_contratos_id">Tipo de Contrato</label>
                        <select class="form-control" id="tipo_contratos_id" name="tipo_contratos_id">
                            <option value="1" >Contrastista</option>
                            <option value="2" >Planta</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="instructores_area_id">Área de Instructores</label>
                        <select id="instructores_area_id" name="instructores_area_id" class="form-control">
                            @foreach($areas as $area)
                                <option value="{{ $area->id }}">{{ $area->nombre }} - {{ $area->area}}</option>
                            @endforeach
                        </select>
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
<script>
    // Función para verificar la cantidad de archivos seleccionados
    function checkFileCount(input) {
        // Verificar si se seleccionaron más de un archivo
        if (input.files.length > 1) {
            // Mostrar un mensaje de alerta al usuario
            alert("Por favor, seleccione solo un archivo.");
            // Limpiar la selección de archivos
            input.value = '';
        }
    }
</script>

@endsection
