<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PythonController extends Controller
{
    // public function ejecutarPython()
    // {
    //     // Ruta al archivo Python
    //     // $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/areaPlanta.py';
    //     // $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/prueba.py';
    //     // $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/contratistasBaseD.py';
    //     $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/asignacionResultados.py';


    //     // Ejecutar el script Python y capturar la salida completa
    //     exec("python {$rutaArchivoPython} 2>&1", $output, $returnCode);

    //     // Combinar la salida en una cadena
    //     $salidaCompleta = implode(PHP_EOL, $output);

    //     // Pasar la salida completa a la vista
    //     return view('layouts.main_template', ['output' => $salidaCompleta]);
    // }


    public function reenviar(Request $request)
    {
        // $rutaArchivoPython = 'C:/xamppTC/htdocs/laravelapp/automatizacionSena/bots/prueba.py';
        // $rutaArchivoPython = 'C:/xamppTC/htdocs/laravelapp/automatizacionSena/bots/prueba.py';
        $rutaArchivoPython = 'C:/xamppTC/htdocs/laravelapp/automatizacionSena/bots/TercerCorreo.py';

        // Ejecutar el script Python y capturar la salida completa
        exec("python {$rutaArchivoPython} 2>&1", $output1, $returnCode);

        // Combinar la salida en una cadena
        $salidaCompleta = implode(PHP_EOL, $output1);

        // Pasar la salida completa a la vista
        // return view('email.reen_email', ['output1' => $salidaCompleta]);
        // return view('tables.index_contractor', compact('contractor'));
        // return view('tables.index_edit', compact('contractor'));
        return redirect($request->input('hours'));

    }
}
