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
        // $contractors = instructore::where('tipo_contratos_id',1)->get();
        // $contractors = instructore::where('habilitacion',0)->get();

        // $contractors = create::where('instructores', 1)->get();
        // return view('tables.index_create', compact('contractors'));

        $crear = create::all();
        return view('tables.index_create', compact('crear'));

    }


    public function store(Request $request)
    {
        // Validar los datos recibidos del formulario
        $request->validate([
            'nombre' => 'required|string',
            'apellido' => 'required|string',
            'numero' => 'required|string',
            'direccion' => 'required|string',
            // Agrega aquí las reglas de validación para otros campos del formulario
        ]);
    
        // Guardar los datos en la base de datos
        DB::table('instructores')->insert([
            'nombre' => $request->input('nombre'),
            'apellido' => $request->input('apellido'),
            'numero' => $request->input('numero'),
            'direccion' => $request->input('direccion'),
            // Agrega aquí otros campos del formulario
        ]);
    
        // Redirigir de vuelta a la vista con un mensaje de éxito
        return redirect()->route('create.index')->with('success', 'Instructor creado correctamente');
    }
}
