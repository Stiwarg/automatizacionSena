<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\PlantController;
use App\Http\Controllers\ContractorController;
use App\Http\Controllers\ApprenticeController;
use App\Http\Controllers\EmailOneController;
use App\Http\Controllers\EmailTwoController;
use App\Http\Controllers\EmailThreeController;
use App\Http\Controllers\HomeController;



/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [HomeController::class, 'index'])->name('home');
Route::resource('planta', PlantController::class)->names('plant');
Route::resource('contratistas',ContractorController::class)->names('contractor');
Route::resource('aprendices',ApprenticeController::class)->names('apprentice');
Route::resource('primer correo',EmailOneController::class)->names('emailone');
Route::resource('segundo correo',EmailTwoController::class)->names('emailtwo');
Route::resource('tercer correo',EmailThreeController::class)->names('emailthree');