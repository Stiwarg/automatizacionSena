<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\instructore;
use App\Models\create;
use Illuminate\Support\Facades\DB;


class CreateController extends Controller
{
    //
    public function index()
    {
        // $instructores = instructore::all();
        // return view('tables.index_create', compact('instructores'));

        $agregar = Create::all();
        return view('tables.index_create', compact('agregar'));

    }
    



    public function store(Request $request)
    {
        // Validar los datos recibidos del formulario
        $request->validate([
            'nombre' => 'required|string',
            'correo' => 'required|email',
            'telefono' => 'required|string',
            'identificacion' => 'required|string',
            'habilitacion' => 'required|boolean',
            'tipo_contratos_id' => 'required|boolean',
            'instructores_area_id' => 'required|boolean',



        ]);
    
        // Crear un nuevo contratista con los datos proporcionados
        $create = new Create();
        $create->nombre = $request->nombre;
        $create->identificacion = $request->identificacion;
        $create->correo = $request->correo;
        $create->telefono = $request->telefono;
        $create->habilitacion = $request->habilitacion;
        $create->tipo_contratos_id = $request->tipo_contratos_id;
        $create->instructores_area_id = $request->instructores_area_id;



    
        // Guardar el nuevo contratista en la base de datos
        $create->save();
    
        // Redirigir de vuelta a la lista de contratistas con un mensaje de éxito
        return redirect()->route('create.index')->with('success', 'Nuevo registro creado correctamente');

                // // Validar los datos recibidos del formulario
                // $request->validate([
                //     'nombre' => 'required|string',
                //     'apellidos' => 'required|string',
                //     'identificacion' => 'nullable|string',
                //     'programa' => 'required|string',
                //     'supervisor' => 'required|string',
                //     'correo' => 'required|email',
                //     'telefono' => 'required|string',
                //     'celular' => 'required|string',
                //     'direccion' => 'required|string',
                // ]);
            
                // // Crear una nueva instancia del modelo Instructore y asignar los valores
                // $instructor = new create();
                // $instructor->nombre = $request->input('nombre');
                // $instructor->apellidos = $request->input('apellidos');
                // $instructor->identificacion = $request->input('identificacion');
                // $instructor->programa = $request->input('programa');
                // $instructor->supervisor = $request->input('supervisor');
                // $instructor->correo = $request->input('correo');
                // $instructor->telefono = $request->input('telefono');
                // $instructor->celular = $request->input('celular');
                // $instructor->direccion = $request->input('direccion');
            
                // // Guardar el nuevo registro en la base de datos
                // $instructor->save();
            
                // // Redirigir de vuelta a la vista con un mensaje de éxito
                // return redirect()->route('create.index')->with('success', 'Nuevo registro creado correctamente');
    }
    
    
}
