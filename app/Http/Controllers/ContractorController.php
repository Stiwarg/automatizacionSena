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
