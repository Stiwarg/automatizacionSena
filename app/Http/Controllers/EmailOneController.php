<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\PlantillasCorreo;

class EmailOneController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $plantilla1 = PlantillasCorreo::select('pc.id', 'pc.informacion_plantilla')
                        ->from('plantillascorreos as pc')
                        ->where('pc.id', 1)
                        ->first();

        return view('email.first_email', compact('plantilla1'));
    }
    
    public function secondEmail()
    {
        $plantilla2 = PlantillasCorreo::select('pc.id', 'pc.informacion_plantilla')
                        ->from('plantillascorreos as pc')
                        ->where('pc.id', 2)
                        ->first();
    
        return view('email.second_email', compact('plantilla2'));
    }
    
    public function thirdEmail()
    {
        $plantilla3 = PlantillasCorreo::select('pc.id', 'pc.informacion_plantilla')
                        ->from('plantillascorreos as pc')
                        ->where('pc.id', 3)
                        ->first();
    
        return view('email.third_email', compact('plantilla3'));
    }
    

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request)
    {
        //Se obtine el identificador de la primera plantilla
        $plantilla1 = PlantillasCorreo::find(1);
        
        //Se actualiza los campos necesarios
        $plantilla1->informacion_plantilla = $request->input('informacion_plantilla');
        
        //Se guardan los cambios en la base de datos
        $plantilla1->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('email.first_email'));

    }

    
    public function updateSecondEmail(Request $request)
    {
        //Se obtine el identificador de la segunda plantilla
        $plantilla2 = PlantillasCorreo::find(2);
        
        //Se actualiza los campos necesarios
        $plantilla2->informacion_plantilla = $request->input('informacion_plantilla');
        
        //Se guardan los cambios en la base de datos
        $plantilla2->save();
        
        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('email.second_email'));
    }

    public function updateThirdEmail(Request $request)
    {
        //Se obtine el identificador de la tercera plantilla
        $plantilla3 = PlantillasCorreo::find(3);
        
        //Se actualiza los campos necesarios
        $plantilla3->informacion_plantilla = $request->input('informacion_plantilla');
        
        //Se guardan los cambios en la base de datos
        $plantilla3->save();
        
        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('email.second_email'));

    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
