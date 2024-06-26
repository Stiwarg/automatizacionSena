@extends('layouts.main_template')

@section('contenido')

<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">Enviar Pirmer Correo Electrónico</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                
                <form action="{{ route('emailone.update', ['id' => $plantilla1->id]) }}" method="POST">
                    @csrf
                    @method('PUT')
                    <div class="form-group">
                        <label for="correo-body">Contenido del Correo Electrónico</label>
                        <textarea id="correo-body" name="informacion" class="form-control" rows="10">{{ $plantilla1->informacion }}</textarea>
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Actualizar</button>
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

@section('js')
    <script>
        $(function () {
            // Inicializar el editor de texto enriquecido Summernote sin toolbar
            $('#correo-body').summernote({
                height: 300,
                placeholder: 'Escribe aquí el contenido del correo electrónico...',
                tabsize: 2,
                toolbar: [],
            });
        });
    </script>
@endsection


@section('js')
    <script>
        $(function (){
            $('#compose-textarea').summernote();
        });
    </script>
@endsection
