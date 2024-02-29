@extends('layouts.main_template')
@section('contenido')

<h1>Organizacion De Fechas</h1>
<table class="table table-bordered" id="Table">
    <h3>VACACIONES Y CONTRATACIONES</h3>

    <div class="row">
        <div class="col-sm-6">
            <!-- Fecha de Inicio -->
            <div class="form-group">
                <label>Fecha de Inicio</label>
                <input type="date" class="form-control" name="start_date">
            </div>
        </div>
        <div class="col-sm-6">
            <!-- Fecha de Fin -->
            <div class="form-group">
                <label>Fecha de Fin</label>
                <input type="date" class="form-control" name="end_date">
            </div>
        </div>
    </div>
    
    <div class="row">
        <div class="col-sm-6">
            <!-- Trimestre -->
            <div class="form-group">
                <label>Trimestre</label>
                <select class="form-control" name="trimestre">
                    <option value="1">Trimestre 1</option>
                    <option value="2">Trimestre 2</option>
                    <option value="3">Trimestre 3</option>
                    <option value="4">Trimestre 4</option>
                </select>
            </div>
        </div>
        <div class="col-sm-6">
            <!-- Acciones -->
            <div class="form-group">
                <label>Acciones</label>
                {{-- <input type="hidden" name="instructor_id" value="{{$hora->id}}"> --}}
            </div>
        </div>
    </div>
</table>
<table class="table table-bordered" id="Table">
    <div class="row">
        <div class="col-sm-6">
            <!-- Fecha de Inicio -->
            <div class="form-group">
                <label>Inicio de Trimestre</label>
                <input type="date" class="form-control" name="start_date">
            </div>
        </div>
        <div class="col-sm-6">
            <!-- Fecha de Fin -->
            <div class="form-group">
                <label>Fin De Trimestre</label>
                <input type="date" class="form-control" name="end_date">
            </div>
        </div>
    </div>
</table>


@endsection

{{-- @section('js')
    <script>
      $(document).ready(function () { $('#Table').DataTable(); });
    </script>
@endsection --}}

