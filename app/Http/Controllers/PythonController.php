<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PythonController extends Controller
{
    //
        /**
     * Ejecutar el script Python.
     *
     * @return string
     */
    // public function ejecutarPython()
    // {
    //     // Ruta al archivo Python
    //     $rutaArchivoPython = public_path('bots\prueba.py');

    //     // Comando para ejecutar el archivo Python
    //     $comando = "python {$rutaArchivoPython}";

    //     // Ejecutar el comando y capturar la salida
    //     $salida = exec($comando);

    //     return view('layouts.main_template', ['output' => $salida]);
    // }
    public function ejecutarPython()
    {
        // Ruta al archivo Python
        // Ruta al archivo Python
        $rutaArchivoPython = base_path('automatizacionSena/bots/prueba.py');



        // Ejecutar el script Python y capturar la salida completa
        exec("python {$rutaArchivoPython} 2>&1", $output, $returnCode);

        // Combinar la salida en una cadena
        $salidaCompleta = implode(PHP_EOL, $output);

        // Pasar la salida completa a la vista
        return view('layouts.main_template', ['output' => $salidaCompleta]);
    }
}
