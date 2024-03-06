@extends('layouts.main_template')
@section('contenido')

<h1>Organizacion De Fechas</h1>

    <table class="table table-bordered" id="Table">
        <h3>VACACIONES Y CONTRATACIONES</h3>

        <form method="POST" action="{{ route('hours.store') }}">
            @csrf
        
            <div class="row">
                <div class="col-sm-6">
                    <!-- Fecha de Inicio -->
                    <div class="form-group">
                        <label>Fecha de Inicio</label>
                        <input type="date" class="form-control" name="fecha_inicio"> <!-- Corregido -->
                    </div>
                </div>
                <div class="col-sm-6">
                    <!-- Fecha de Fin -->
                    <div class="form-group">
                        <label>Fecha de Fin</label>
                        <input type="date" class="form-control" name="fecha_fin"> <!-- Corregido -->
                    </div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Guardar</button>

        </form>

    </table>


<table class="table table-bordered" id="Table">
    <form method="POST" action="{{ route('hoursT.store') }}">
        @csrf
        <div class="row">
            <div class="col-sm-6">
                <!-- Trimestre -->
                <div class="form-group">
                    <label>
                        <h3>TRIMESTRES</h3>
                    </label>
                    <select class="form-control" name="trimestres_id">
                        <option value="1">Trimestre 1</option>
                        <option value="2">Trimestre 2</option>
                        <option value="3">Trimestre 3</option>
                        <option value="4">Trimestre 4</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-sm-6">
                <!-- Fecha de Inicio -->
                <div class="form-group">
                    <label>Inicio de Trimestre</label>
                    <input type="date" class="form-control" name="fecha_inicio">
                </div>
            </div>
            <div class="col-sm-6">
                <!-- Fecha de Fin -->
                <div class="form-group">
                    <label>Fin De Trimestre</label>
                    <input type="date" class="form-control" name="fecha_fin">
                </div>
            </div>
        </div>

        <button type="submit" class="btn btn-primary">Guardar</button>

    </form>
</table>


@endsection

{{-- @section('js')
    <script>
      $(document).ready(function () { $('#Table').DataTable(); });
    </script>
@endsection --}}

