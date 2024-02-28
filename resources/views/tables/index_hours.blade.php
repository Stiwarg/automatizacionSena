@extends('layouts.main_template')
@section('contenido')

<h1>Organizacion De Fechas</h1>
<table class="table table-bordered" id="Table">
    <thead>
        <tr>
            <th scope="col">Fecha de Inicio</th>
            <th scope="col">Fecha de Fin</th>
            <th scope="col">Trimestre</th>
            <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        @foreach ($horas as $hora)
        <tr>
            <td><input type="date" name="start_date"></td>
            <td><input type="date" name="end_date"></td>
            <td>
                <select name="trimestre">
                    <option value="1">Trimestre 1</option>
                    <option value="2">Trimestre 2</option>
                    <option value="3">Trimestre 3</option>
                    <option value="4">Trimestre 4</option>
                </select>
            </td>
            <td>
                <input type="hidden" name="instructor_id" value="{{$hora->id}}">
                {{-- <button class="btn btn-primary btn-sm mr3">Enviar Correo</button> --}}
            </td>
        </tr>
        @endforeach
    </tbody>
</table>

@endsection

{{-- @section('js')
    <script>
      $(document).ready(function () { $('#Table').DataTable(); });
    </script>
@endsection --}}

