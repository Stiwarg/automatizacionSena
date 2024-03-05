@extends('layouts.main_template')

@section('contenido')
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <link rel="stylesheet" href="../../plugins/summernote/summernote-bs4.min.css">


    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card card-outline card-info">
                <div class="card-header">
                    <h2 class="card-title">Formulario del Primer Correo Electrónico</h2>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <form action="{{ route('emailone.update', ['id' =>  $plantilla1->id]) }}" method="POST">
                        @csrf
                        @method('PUT')
                        <div class="form-group">
                            <textarea id="compose-textarea" name="informacion_plantilla" class="form-control" style="height: 300px;">{{ $plantilla1->informacion_plantilla }}</textarea>
                        </div>
                        <div class="form-group">
                            <button type="submit" class="btn btn-primary">Enviar Correo</button>
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
        $(function (){
            $('#compose-textarea').summernote();
        });
    </script>
@endsection
