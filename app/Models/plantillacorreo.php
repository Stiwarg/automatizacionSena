<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class plantillacorreo extends Model
{
    use HasFactory;
    public $timestamps = false;

    protected $table = 'plantilla_correos';
}
