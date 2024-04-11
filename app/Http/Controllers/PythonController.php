<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PythonController extends Controller
{
    public function ejecutarPython()
    {
        // Ruta al archivo Python
        $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/EjecucionScripts.py';

        // Ejecutar el script Python y capturar la salida completa
        exec("python {$rutaArchivoPython} 2>&1", $output, $returnCode);

        // Combinar la salida en una cadena
        $salidaCompleta = implode(PHP_EOL, $output);

        // Pasar la salida completa a la vista
        return view('layouts.main_template', ['output' => $salidaCompleta]);
    }
}
