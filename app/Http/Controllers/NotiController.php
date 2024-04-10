<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\View;
use App\Models\Noti;


class NotiController extends Controller
{



    public function index()
    {
        // Obtener todas las notificaciones y pasarlas a todas las vistas
        // $agregar = instructore::all();
        // $areas = Area::all();
        $noti = Noti::all();

        // return view('tables.index_create', compact('noti'));
        // return view('layouts.main_template', compact('noti', $noti));
        return view('layouts.main_template') ->with('noti', $noti);
    }

}
