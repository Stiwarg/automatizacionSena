<?php

namespace App\Http\Controllers;

use App\Models\aprendice;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;


class AprController extends Controller
{
    //
    public function index()
    {

        $apr = aprendice::all();

        return view('tables.index_apr', compact('apr'));
        
        

    }

    public function uploadFileToProjectPython_apr(Request $request)
    {
        // Verificar si se ha subido un archivo
        if ($request->hasFile('archivo_excel')) {
            $excelFile = $request->file('archivo_excel');

            // Obtener el nombre del archivo
            $nameFile = $excelFile->getClientOriginalName();

            // Definir las condiciones para determinar la carpeta de destino en Python
            if (
<<<<<<< Updated upstream
                // strpos($nameFile, 'CONTRATISTAS_2024_BD') !== false ||
                // strpos($nameFile, 'INSTRUCTORES_AREA_CONTRATISTA') !== false ||
                // strpos($nameFile, 'Instructores_AREA') !== false ||
                // strpos($nameFile, 'PLANTA_2024_BD') !== false
                strpos($nameFile, 'ReportedeJuiciosEvaluativos') !== false
            ) {
=======

                strpos($nameFile, 'ReportedeJuiciosEvaluativos_') !== false

                ) 

            {
>>>>>>> Stashed changes
                // Guardar el archivo Excel en una carpeta temporal
                $excelFile->storeAs('temp', $nameFile);

                // Ejecutar el script Python para mover el archivo a la carpeta de documentos
                $rutaFile = storage_path('app/temp/' . $nameFile);

                //Aqui no esta llamando
                //La ruta es del computador de estiven
<<<<<<< Updated upstream
                $output = shell_exec("python C:\\xampp\\htdocs\\automatizacionSena\\bots\\excels.py $rutaFile");
=======
                $output = shell_exec("python C:\\xampp\\htdocs\\bots\\excels.py $rutaFile");
                
>>>>>>> Stashed changes
                // La ruta es del computador de jheniffer
                #$output = shell_exec("python C:\\Users\\SENA\\Desktop\\bot\\bots\\excels.py $rutaFile");

                // Eliminar el archivo temporal después de procesarlo
                Storage::disk('local')->delete('temp/' . $nameFile);

                return redirect()->back()->with('success', 'Archivo Excel subido y procesado con éxito.');
            } else {
                // Guardar un mensaje de error en la sesión flash
                return redirect()->back()->with('error', 'El nombre del archivo no coincide con ninguno de los nombres permitidos.');
            }
        } else {
            // Guardar un mensaje de error en la sesión flash
            return redirect()->back()->with('error', 'No se ha seleccionado ningún archivo para subir.');
        }
    }
}
