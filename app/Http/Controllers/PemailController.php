<?php

namespace App\Http\Controllers;

use App\Models\plantillacorreo;
use Illuminate\Http\Request;

class PemailController extends Controller
{
    //
    public function index()
    {
        // $instructores = Instructore::all();
        // return view('tables.index_plant', compact('instructores'));

        $email = plantillacorreo::all();
        return view('first_email.blade', compact('horas'));
        
    }
}
