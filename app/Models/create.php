<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class create extends Model
{
    // protected $table = 'vacaciones'; // Nombre de la tabla en la base de datos
    // protected $fillable = ['fecha_inicio', 'fecha_fin'];

    
    // public $timestamps = false;

    protected $table = 'instructores'; // Nombre de la tabla en la base de datos
    protected $fillable = ['nombre', 
                            'apellidos',
                            'idendificacion',
                            'programa',
                            'supervisor',
                            'correo',
                            'telefono',
                            'celular',
                            'direccion',
                            // 'habilitacion' 
                            ];

    
    public $timestamps = false;
    use HasFactory;
}
