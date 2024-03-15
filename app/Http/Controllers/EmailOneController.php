<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\plantillacorreo;

class EmailOneController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $plantilla1 = plantillacorreo::select('pc.id', 'pc.informacion')
                        ->from('plantilla_correos as pc')
                        ->where('pc.id', 1)
                        ->first();

        return view('email.first_email', compact('plantilla1'));
    }

    public function secondEmail()
    {
        $plantilla2 = plantillacorreo::select('pc.id', 'pc.informacion')
                        ->from('plantilla_correos as pc')
                        ->where('pc.id', 2)
                        ->first();

        return view('email.second_email', compact('plantilla2'));
    }

    public function thirdEmail()
    {
        $plantilla3 = plantillacorreo::select('pc.id', 'pc.informacion')
                        ->from('plantilla_correos as pc')
                        ->where('pc.id', 3)
                        ->first();

        return view('email.third_email', compact('plantilla3'));
    }


    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, $id)
    {
        // Obtener la plantilla de correo por su ID
        $plantilla1 = PlantillaCorreo::find($id);
    
        // Validar los datos recibidos del formulario
        $request->validate([
            'informacion' => 'required|string', // Ajusta las reglas de validación según sea necesario
        ]);
    
        // Actualizar la información de la plantilla con los datos del formulario
        $plantilla1->informacion = $request->input('informacion');
    
        // Guardar los cambios en la base de datos
        $plantilla1->save();
    
        // Redirigir de vuelta a la vista de edición con un mensaje de éxito
        return redirect()->route('emailone.index')->with('success', 'La plantilla de correo se actualizó correctamente.');
    }
    


    public function updateSecondEmail(Request $request, $id)
    {
        //Se obtine el identificador de la segunda plantilla
        $plantilla2 = plantillaCorreo::find($id);


        $request->validate([
            'informacion' => 'required|string',
        ]);

        //Se actualiza los campos necesarios
        $plantilla2->informacion = $request->input('informacion');

        //Se guardan los cambios en la base de datos
        $plantilla2->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect()->route('emailone.secondEmail')->with('success', 'La plantilla de correo se actulizo correctamente.');
    }



    public function updateThirdEmail(Request $request, $id)
    {
        //Se obtine el identificador de la tercera plantilla
        $plantilla3 = plantillaCorreo::find($id);


        $request->validate([
            'informacion' => 'required|string',
        ]);

        //Se actualiza los campos necesarios
        $plantilla3->informacion = $request->input('informacion');

        //Se guardan los cambios en la base de datos
        $plantilla3->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect()->route('emailone.thirdEmail')->with('success', 'La plantilla de correo se actualizó correctamente.');

    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
