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
    public function ejecutarPython()
    {
        // Ruta al archivo Python
        $rutaArchivoPython = public_path('bots\prueba.py');

        // Comando para ejecutar el archivo Python
        $comando = "python {$rutaArchivoPython}";

        // Ejecutar el comando y capturar la salida
        $salida = exec($comando);

        // Pasar la salida a la vista
        // return view('tables.resultado_python', ['output' => $salida]);
        return view('layouts.main_template', ['output' => $salida]);
    }
}
