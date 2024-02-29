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
    public function update(Request $request)
    {
        //Se obtine el identificador de la primera plantilla
        $plantilla1 = plantillacorreo::find(1);

        //Se actualiza los campos necesarios
        $plantilla1->informacion_plantilla = $request->input('informacion');

        //Se guardan los cambios en la base de datos
        $plantilla1->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('emailone.index'));

    }


    public function updateSecondEmail(Request $request)
    {
        //Se obtine el identificador de la segunda plantilla
        $plantilla2 = plantillacorreo::find(2);

        //Se actualiza los campos necesarios
        $plantilla2->informacion_plantilla = $request->input('informacion');

        //Se guardan los cambios en la base de datos
        $plantilla2->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('emailone.secondEmail'));
    }

    public function updateThirdEmail(Request $request)
    {
        //Se obtine el identificador de la tercera plantilla
        $plantilla3 = plantillacorreo::find(3);

        //Se actualiza los campos necesarios
        $plantilla3->informacion_plantilla = $request->input('informacion');

        //Se guardan los cambios en la base de datos
        $plantilla3->save();

        //Se retorna a la ruta indicada d la plantilla
        return redirect(route('emailone.thirdEmail'));

    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
