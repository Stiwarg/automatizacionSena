<?php

namespace App\Http\Controllers;

use App\Models\plantillacorreo;
use Illuminate\Http\Request;

class PemailController extends Controller
{
    //
    public function index()
    {

        $email = plantillacorreo::all();
        return view('first_email.blade', compact('horas'));
        
    }
}
