<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\View;
use App\Models\Noti;


class NotiController extends Controller
{



    public function __construct()
    {
        // Obtener todas las notificaciones y pasarlas a todas las vistas
        $notificaciones = Noti::all();
        View::share('notificaciones', $notificaciones);
    }
    //
        /**
     * Display a listing of the resource.
     */
    // public function index()
    // {
    //     // Obtener todas las notificaciones
    //     $notifications = Noti::all();
        
    //     // Pasar las notificaciones a la vista
    //     return view('notifications.index', compact('notifications'));
    // }
}
