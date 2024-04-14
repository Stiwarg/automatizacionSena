<?php

namespace App\Http\Controllers;
use Illuminate\Http\RedirectResponse;
use Illuminate\Support\Facades\Session;


use Illuminate\Http\Request;

class PythonController extends Controller
{
    public function accionPython(Request $request, $accion)
    {
        if ($accion == 'ejecutar') {
            return $this->ejecutarPython();
        } elseif ($accion == 'reenviar') {
            return $this->reenviar($request);
        } else {
            // Acción no válida
            return redirect()->back()->with('error', 'Acción no válida.');
        }
    }
    
    public function ejecutarPython()
    {
        // Ruta al archivo Python
        // $rutaArchivoPython = 'C:/xampp/htdocs/automatizacionSena/bots/prueba.py';
        // $rutaArchivoPython = 'bots/prueba.py';
        $rutaArchivoPython = 'C:/xamppTC/htdocs/laravelapp/automatizacionSena/bots/prueba.py';


        // Ejecutar el script Python y capturar la salida completa
        exec("python {$rutaArchivoPython} 2>&1", $output, $returnCode);

        // Combinar la salida en una cadena
        $salidaCompleta = implode(PHP_EOL, $output);

        // Pasar la salida completa a la vista
        return view('layouts.main_template', ['output' => $salidaCompleta]);
    }


    public function reenviar()
    {
        $rutaArchivoPython = 'C:/xamppTC/htdocs/laravelapp/automatizacionSena/bots/TercerCorreo.py';
        
        // Ejecutar el script Python y capturar la salida completa
        exec("python {$rutaArchivoPython} 2>&1", $output1, $returnCode);
        
        // Combinar la salida en una cadena
        $salidaCompleta = implode(PHP_EOL, $output1);

        // Redireccionar a la ruta actual
        return redirect()->back()->with('success', 'Correo reenviado exitosamente.');

    }
}
