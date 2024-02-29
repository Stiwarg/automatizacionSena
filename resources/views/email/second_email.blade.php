@extends('layouts.main_template')
@section('contenido')

   <div class="row">
        <div class="col-md-12">
            <div class="card card-outline card-info">
                <div class="card-header">
                    <h3 class="card-title">
                    Formulario del Segundo Correo Electronico
                    </h3>
                </div>
                <!-- /.card-header -->
                <div class="form-group">
                    <form action="{{ route('emailtwo.update', ['id' =>  $plantilla2->id]) }}" method="POST">
                        @method('PUT')
                        @csrf
                        <textarea id="compose-textarea" name="informacion_plantilla" class="form-control"
                        style="height: 300px">{{ $plantilla2->informacion_plantilla }}
                        </textarea>
                        <input type="submit" value="Enviar Correo" class="btn btn-primary btn-lg mr6">
                    </form>
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
