@extends('layouts.main_template')
@section('contenido')
   <div class="row">
        <div class="col-md-12">
            <div class="card card-outline card-info">
                <div class="card-header">
                    <h3 class="card-title">
                    Summernote
                    </h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <textarea id="summernote" style="width: 100%; height: 50vh;">
                    hola como estas
                    </textarea>
                </div>
                <div class="card-footer">
                    Visit <a href="https://github.com/summernote/summernote/">Summernote</a> documentation for more examples and information about the plugin.
                </div>
            </div>
        </div>
    </div>
@endsection