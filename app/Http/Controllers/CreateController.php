<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\instructore;
use App\Models\Area;


class CreateController extends Controller
{
    public function index()
    {

        $agregar = instructore::all();
        $areas = Area::all();

        return view('tables.index_create', compact('agregar', 'areas'));
        

    }

    public function store(Request $request)
    {
        // Validar los datos recibidos del formulario
        $request->validate([
            'nombre' => 'required|string',
            'apellidos' => 'required|string',
            'identificacion' => 'required|string',
            'programa' => 'required|string',
            'supervisor' => 'required|string',
            'correo' => 'required|string',
            'telefono' => 'required|string',
            'celular' => 'required|string',
            'direccion' => 'required|string',
            'habilitacion' => 'required|boolean',
            'tipo_contratos_id' => 'required|integer',
            'instructores_area_id' => 'required|integer',
            // Otras validaciones...
        ]);

        // Obtener los datos del formulario
        $nombre = $request->nombre;
        $apellidos = $request->apellidos;
        $identificacion = $request->identificacion;
        $programa = $request->programa;
        $supervisor = $request->supervisor;
        $correo = $request->correo;
        $telefono = $request->telefono;
        $celular = $request->celular;
        $direccion = $request->direccion;
        $habilitacion = $request->habilitacion;
        $tipo_contratos_id = $request->tipo_contratos_id;
        $instructores_area_id = $request->instructores_area_id;

        // Crear un nuevo instructore con los datos proporcionados
        $instructore = new Instructore();
        $instructore->nombre = $nombre;
        $instructore->apellidos = $apellidos;
        $instructore->identificacion = $identificacion;
        $instructore->programa = $programa;
        $instructore->supervisor = $supervisor;
        $instructore->correo = $correo;
        $instructore->telefono = $telefono;
        $instructore->celular = $celular;
        $instructore->direccion = $direccion;
        $instructore->habilitacion = $habilitacion;
        $instructore->tipo_contratos_id = $tipo_contratos_id;
        $instructore->instructores_area_id = $instructores_area_id;
        $instructore->save();

        // Redirigir de vuelta a la vista con un mensaje de éxito
        return redirect()->route('create.index')->with('success', 'Nuevo instructor creado correctamente');
    }

}

