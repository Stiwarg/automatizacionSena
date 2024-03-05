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
        $contractors = instructore::where('tipo_contratos_id',1)->get();
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
        //
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
        //
        $contractor = instructore::findOrFail($id);
        return view('tables.index_edit', compact('contractor'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
        $request->validate([
            'nombre' => 'required|string|max:255',
            'correo' => 'required|email|max:255',
            'telefono' => 'required|string|max:255',
        ]);
    
        // Obtener el contratista a actualizar
        $contractor = instructore::findOrFail($id);
    
        // Actualizar los atributos del contratista
        $contractor->nombre = $request->nombre;
        $contractor->correo = $request->correo;
        $contractor->telefono = $request->telefono;
    
        // Guardar los cambios en la base de datos
        $contractor->save();
    
        // Redirigir de vuelta a la lista de contratistas con un mensaje de éxito
        return redirect()->route('contractors.index')->with('success', 'Contratista actualizado correctamente');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
