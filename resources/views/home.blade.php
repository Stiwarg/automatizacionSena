@extends('layouts.main_template')
@section('contenido')

<div class="container-fluid">
    <style>
        h1{
            text-align: center;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 50px;
        }
    </style>
    <h2>Bienvenido a la pagina de automatizacion SENA</h2>
    <img src="{{asset('img/2.png')}}" alt="sena">

</div><!--/. container-fluid                         Aqui-->  

@endsection
