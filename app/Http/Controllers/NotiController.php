<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Noti;

class NotiController extends Controller
{
    //
        /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // Obtener todas las notificaciones
        $notifications = Noti::all();
        
        // Pasar las notificaciones a la vista
        return view('notifications.index', compact('notifications'));
    }
}
