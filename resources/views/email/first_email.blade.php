@extends('layouts.main_template')
@section('contenido')
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">

   <div class="row">
        <div class="col-md-12">
            <div class="card card-outline card-info">
                <div class="card-header">
                    <h1 class="card-title">
                        Formulario del Primer Correo Electronico
                    </h1>
                </div>
                <!-- /.card-header -->
                <div class="form-group">
                    <form action="{{ route('emailone.update', ['id' =>  $plantilla1->id]) }}" method="POST">
                        @csrf
                        @method('PUT')
                        <textarea id="compose-textarea" name="informacion_plantilla" class="form-control"
                        style="height: 300px;">{{ $plantilla1->informacion_plantilla }}
                        </textarea>
                        <input type="submit" value="Enviar Correo" class="btn btn-primary btn-lg mr6">
                    </form>
                </div>
                <div class="card-footer">
                    Visit <a href="https://github.com/summernote/summernote/">Summernote</a> documentation for more examples and information about the plugin.
                </div>
            </div>
        </div>
    </div>
@endsection

@section('js')
    <script>
        $(function (){
            $('#compose-textarea').summernote()
        })
    </script>
@endsection
