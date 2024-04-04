<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class create extends Model
{
    protected $table = 'instructores'; // Nombre de la tabla en la base de datos
    protected $fillable = ['nombre', 'correo', 'telefono', 'identificacion', 'habilitacion', 'tipo_contratos_id','instructores_area_id'];

    public $timestamps = false;

    use HasFactory;
}
