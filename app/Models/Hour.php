<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Hour extends Model
{
    protected $table = 'vacaciones'; // Nombre de la tabla en la base de datos
    protected $fillable = ['fecha_inicio', 'fecha_fin'];

    
    public $timestamps = false;


    use HasFactory;
}