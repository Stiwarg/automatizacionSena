<?php

namespace App\Http\Controllers;

use App\Models\aprendice;
use Illuminate\Http\Request;

class AprController extends Controller
{
    //
    public function index()
    {

        $apr = aprendice::all();

        return view('tables.index_apr', compact('apr'));
        

    }
}
