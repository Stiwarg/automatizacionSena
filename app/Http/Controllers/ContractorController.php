<?php

namespace App\Http\Controllers;

use App\Models\instructore;
use Illuminate\Http\Request;

class ContractorController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $contractors = instructore::where('tipo_contratos_id', 1)
                                  ->where('habilitacion', 0)
                                  ->get();
                           
        return view('tables.index_contractor', compact('contractors'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
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
        // // Validar los datos recibidos del formulario
        // $request->validate([
        //     'nombre' => 'required|string|max:255',
        //     'correo' => 'required|email|max:255',
        //     'telefono' => 'required|string|max:255',
        //     'identificacion' => 'required|string|max:255',
        //     'habilitacion' => 'required|boolean|max:2',
        //     'tipo_contratos_id' => 'required|boolean|max:2',


        // ]);
    
        // // Crear un nuevo contratista con los datos proporcionados
        // $contractor = new instructore();
        // $contractor->nombre = $request->nombre;
        // // $contractor->apellidos = $request->apellidos;
        // $contractor->identificacion = $request->identificacion;
        // // $contractor->programa = $request->programa;
        // // $contractor->supervisor = $request->supervisor;
        // $contractor->correo = $request->correo;
        // $contractor->telefono = $request->telefono;
        // // $contractor->celular = $request->celular;
        // // $contractor->direccion = $request->direccion;
        // $contractor->habilitacion = $request->habilitacion;
        // $contractor->tipo_contratos_id = $request->tipo_contratos_id;



    
        // // Guardar el nuevo contratista en la base de datos
        // $contractor->save();
    
        // // Redirigir de vuelta a la lista de contratistas con un mensaje de éxito
        // return redirect($request->input('previous_url'))->with('success', '¡Contratista creado correctamente!');
    }
    

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        $contractor = instructore::findOrFail($id);
        return view('tables.index_edit', compact('contractor'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        // Validar los datos recibidos del formulario
        $request->validate([
            'identificacion' => 'required|string|max:255',
            'nombre' => 'required|string|max:255',
            'correo' => 'required|email|max:255',
            'telefono' => 'required|string|max:255',
            'habilitacion' => 'required|boolean|max:2',
        ]);
    
        // Obtener el contratista a actualizar
        $contractor = instructore::findOrFail($id);
    
        // Actualizar los atributos del contratista
        $contractor->identificacion = $request->identificacion;
        $contractor->nombre = $request->nombre;
        $contractor->correo = $request->correo;
        $contractor->telefono = $request->telefono;
        $contractor->habilitacion = $request->habilitacion;
    
        // Guardar los cambios en la base de datos
        $contractor->save();
    
        // Redirigir de vuelta a la lista de contratistas con un mensaje de éxito
        return redirect($request->input('previous_url'));

    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
