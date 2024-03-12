<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Instructore;


class PlantController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // $instructores = Instructore::all();
        // $instructores = instructore::where('tipo_contratos_id',2)->get();
        // $instructores = instructore::where('habilitacion',0)->get();

        $instructores = instructore::where('tipo_contratos_id', 2)
                                    ->Where('habilitacion', 0)
                                    ->get();


        return view('tables.index_plant', compact('instructores'));
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
