<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\plantillas_correo;


class PlantillasCorreosController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
      
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
        switch($id){
            
            case 1:

                $correo = plantillas_correo::findOrFail(1);
                return view('email.first_name', compact('correo'));
                break;
            
            case 2:

                $correo = plantillas_correo::findOrFail(2);
                return view('email.second_email', compact('correo'));
                break;
            
            case 3:

                $correo = plantillas_correo::findOrFail(3);
                return view('email.third_email', compact('correo'));
                break;

            default:
                abort(404);
        }
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
