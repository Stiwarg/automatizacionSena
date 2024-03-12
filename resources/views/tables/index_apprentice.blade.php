@extends('layouts.main_template')
@section('contenido')

<h1>Tabla de aprendices</h1>
<table class="table table-bordered" id="Table">
    <thead>
      <tr>
        <th scope="col">Identificacion</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Estado Formacion</th>
        <th scope="col">Competencia</th>
        <th scope="col">Resultado</th>
        <th scope="col">Juicio Evaluativo</th>
      </tr>
    </thead>
    <tbody>
        @foreach ($aprendices as $aprendiz)
            <tr>
                <td>{{$aprendiz->identificacion_aprendiz}}</td>
                <td>{{$aprendiz->nombre_aprendiz}}</td>
                <td>{{$aprendiz->apellidos_aprendiz}}</td>
                <td>{{$aprendiz->estado_formacion}}</td>
                <td>{{$aprendiz->competencias}}</td>
                <td>{{$aprendiz->resultado}}</td>
                <td>{{$aprendiz->juicio_evaluativo}}</td>
            </tr>
        @endforeach
    </tbody>
  </table>

@endsection

@section('js')
    <script>
      $(document).ready(function () { $('#Table').DataTable(); });
    </script>
@endsection
