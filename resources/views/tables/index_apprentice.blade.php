@extends('layouts.main_template')
@section('contenido')

<h1>Tabla de aprendices</h1>
<table class="table table-bordered" id="Table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Identificacion</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Estado Formacion</th>
      </tr>
    </thead>
    <tbody>

    </tbody>
  </table>

@endsection

@section('js')
    <script>
      $(document).ready(function () { $('#Table').DataTable(); });
    </script>
@endsection