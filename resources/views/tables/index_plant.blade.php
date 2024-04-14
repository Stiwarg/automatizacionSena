@extends('layouts.main_template')
@section('contenido')
<style>
  h1 {
    text-align: center;
    font-weight: bold;
  }
  th {
    text-align: center;
  }
</style>
<h1>Instructores de  Planta</h1>
<table class="table table-bordered" id="Table">
    <thead>
      <tr>
        <th scope="col">Identificacion</th>
        <th scope="col">Nombre</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
        <th scope="col">Habilitación</th>
        <th scope="col">Enviar Reporte</th>
      </tr>
    </thead>
    <tbody>
      @foreach ($instructores as $plant)
        <tr>
          <td>{{$plant->identificacion}}</td>
          <td>{{$plant->nombre}}</td>
          <td>{{$plant->correo}}</td>
          <td>{{$plant->telefono}}</td>
          <td>
            @if ($plant->habilitacion == 0)
                Activo
            @elseif ($plant->habilitacion == 1)
                Inactivo
            @endif
          
          </td>
          <td class="project-actions text-right">
            <input type="hidden" name="" value="{{$plant->id}}">
            <a class="btn btn-primary btn-sm" href="{{ route('tables.index_edit', $plant->id) }}">Editar</a>
            <form action="{{ route('tables.index_contractor') }}" method="POST">
              @csrf
              <button type="submit" class="btn btn-primary">Reenviar Correo
              </button>
            </form>
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