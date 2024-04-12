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
<h1>Instructores Contratistas</h1>

<table class="table table-bordered" id="Table">
    <thead>
      <tr>
        <th scope="col">Identificacion</th>
        <th scope="col">Nombre</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
        <th scope="col">habilitacion</th>
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
              @if ($contra->habilitacion == 0)
              Activo
              @elseif ($contra->habilitacion == 1)
                  Inactivo
              @endif
            </td>
            <td class="project-actions text-right">
                <input type="hidden" name="" value="{{$contra->id}}">
                <a class="btn btn-primary btn-sm" href="{{ route('tables.index_edit', $contra->id) }}">Editar</a>
                {{-- <form action="{{ route('tables.index_contractor') }}" method="POST"> --}}
                <form action="{{ route('python.reenviar') }}" method="POST">
                  @csrf
                  <button type="submit" class="btn btn-primary">Reenviar Correo
                  </button>
                </form>

                {{-- <span class="btn btn-primary btn-sm mr3">Reenviar Correo</span> --}}
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

