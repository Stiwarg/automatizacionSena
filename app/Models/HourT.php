<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class HourT extends Model
{
    protected $table = 'fechas_trimestre'; // Nombre de la tabla en la base de datos
    protected $fillable = ['fecha_inicio', 'fecha_fin','trimestres_id'];

    
    public $timestamps = false;

    use HasFactory;
}
