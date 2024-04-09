<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\PlantController;
use App\Http\Controllers\ContractorController;
use App\Http\Controllers\ApprenticeController;
use App\Http\Controllers\CreateController;
use App\Http\Controllers\HoursController;
use App\Http\Controllers\EmailOneController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\NotiController;


Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [HomeController::class, 'index'])->name('home');
Route::resource('planta', PlantController::class)->names('plant');
Route::resource('contratistas',ContractorController::class)->names('contractor');
Route::resource('aprendices',ApprenticeController::class)->names('apprentice');
Route::resource('horas',HoursController::class)->names('hours');
Route::resource('agregar',CreateController::class)->names('create');
Route::resource('primer correo',EmailOneController::class)->names('emailone');
Route::resource('instructors', CreateController::class);


// RUTA PARA EL EDIT
Route::resource('contractors', 'ContractorController');
Route::get('tables/{id}/edit', 'ContractorController@edit')->name('tables.index_edit');


// BOTON DE ACTIVAR Y DESACTIVAR
Route::post('/update-contractor-status', 'ContractorController@updateStatus')->name('update-contractor-status');

// PARA GUARDAR LAS FECHAS
Route::post('/hours', 'App\Http\Controllers\HoursTController@store')->name('hoursT.store');

Route::get('/create', [CreateController::class, 'index'])->name('create.index');
Route::post('/create', [CreateController::class, 'store'])->name('create.store');

Route::get('/primer-correo', [EmailOneController::class, 'index'])->name('emailone.index');
Route::get('/segundo-correo', [EmailOneController::class, 'secondEmail'])->name('emailone.secondEmail');
Route::get('/tercer-correo', [EmailOneController::class, 'thirdEmail'])->name('emailone.thirdEmail');

Route::get('/home', [NotiController::class, 'index'])->name('layouts.main_template');


Route::put('/actualizacion-primer-correo/{id}', [EmailOneController::class, 'update'])->name('emailone.update');
Route::put('/actualizacion-segundo-correo/{id}', [EmailOneController::class, 'updateSecondEmail'])->name('emailtwo.update');
Route::put('/actualizacion-tercer-correo/{id}', [EmailOneController::class, 'updateThirdEmail'])->name('emailthird.update');
