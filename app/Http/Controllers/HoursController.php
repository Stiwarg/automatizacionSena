<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Hour;


class HoursController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // $instructores = Instructore::all();
        // return view('tables.index_plant', compact('instructores'));

        $horas = Hour::all();
        return view('tables.index_hours', compact('horas', 'noti'));
        
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
        // Validar los datos recibidos del formulario
        $request->validate([
            'fecha_inicio' => 'required|date',
            'fecha_fin' => 'required|date',
        ]);
    
        // Crear una nueva instancia de Hour (Vacaciones) y asignar los valores
        $hour = new Hour();
        $hour->fecha_inicio = $request->input('fecha_inicio');
        $hour->fecha_fin = $request->input('fecha_fin');
    
        // Guardar el objeto en la base de datos
        $hour->save();
    
        // Redirigir de vuelta a la vista con un mensaje de éxito
        return redirect()->route('hours.index')->with('success', 'Fechas guardadas correctamente');
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
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
