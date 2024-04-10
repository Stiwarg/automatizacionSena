<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class ExcelController extends Controller
{
    public function descargar_contratista(){

        $file = public_path('excels/CONTRATISTAS_2024_BD.xlsx');

        return response()->download($file, 'CONTRATISTAS_2024_BD.xlsx');
    }

    public function descargar_planta(){

        $file = public_path('excels/PLANTA_2024_BD.xlsx');

        return response()->download($file, 'PLANTA_2024_BD.xlsx');
    }

    public function descargar_area_planta(){

        $file = public_path('excels/Instructores_AREA.xlsx');

        return response()->download($file, 'Instructores_AREA.xlsx');
    }

    public function descargar_area_contratista(){

        $file = public_path('excels/INSTRUCTORES_AREA_CONTRATISTA.xlsx');

        return response()->download($file, 'INSTRUCTORES_AREA_CONTRATISTA.xlsx');
    }

    public function uploadFileToProjectPython(Request $request)
    {
        // Verificar si se ha subido un archivo
        if ($request->hasFile('archivo_excel')) {
            $excelFile = $request->file('archivo_excel');

            // Obtener el nombre del archivo
            $nameFile = $excelFile->getClientOriginalName();

            // Definir las condiciones para determinar la carpeta de destino en Python
            if (
                strpos($nameFile, 'CONTRATISTAS_2024_BD') !== false ||
                strpos($nameFile, 'INSTRUCTORES_AREA_CONTRATISTA') !== false ||
                strpos($nameFile, 'Instructores_AREA') !== false ||
                strpos($nameFile, 'PLANTA_2024_BD') !== false
            ) {
                // Guardar el archivo Excel en una carpeta temporal
                $excelFile->storeAs('temp', $nameFile);

                // Ejecutar el script Python para mover el archivo a la carpeta de documentos
                $rutaFile = storage_path('app/temp/' . $nameFile);

                //Aqui no esta llamando 
                //La ruta es del computador de estiven
                //$output = shell_exec("python C:\\xampp\\htdocs\\bots\\excels.py$rutaFile");

                // La ruta es del computador de jheniffer
                $output = shell_exec("python C:\\Users\\SENA\\Desktop\\bot\\bots\\excels.py $rutaFile");

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