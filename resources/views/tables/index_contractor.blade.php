@extends('layouts.main_template')
@section('contenido')

<h1>Tabla de contratista</h1>
<table class="table table-bordered" id="Table">
    <thead>
      <tr>
        <th scope="col">Identificacion</th>
        <th scope="col">Nombre</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
        <th scope="col">Enviar Reporte</th>
      </tr>
    </thead>
    <tbody>
        @foreach ($contractors as $contra)
        <tr>
          <td>{{$contra->identificacion}}</td>
          <td>{{$contra->nombre}}</td>
          <td>{{$contra->correo}}</td>
          <td>{{$contra->telefono}}</td>
          <td>
              <input type="hidden" name="" value="{{$contra->id}}">
              <span class="btn btn-primary btn-sm mr3">Enviar Correo</span>
          </td>
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
