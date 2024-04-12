@extends('layouts.main_template')

@section('contenido')

<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">Agregar Nuevo Aprendiz</h3>
            </div>
            <div class="card-body">
                <div class="row">
                    <!-- Segunda columna -->
                    <div class="col-md-7">
                        <form action="{{ route('subir.archivo.excelapr') }}" method="post" enctype="multipart/form-data">
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