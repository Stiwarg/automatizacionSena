<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Laravel</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Figtree', sans-serif;
            background-color: #797979;
        }
        .btn-primary {
            background-color: #3b82f6;
        }
        .btn-primary:hover {
            background-color: #2563eb;
        }
        .btn-secondary {
            background-color: #646464;
        }
        .btn-secondary:hover {
            background-color: #4b5563;
        }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen">
    <div class="max-w-md w-full bg-white p-8 rounded-lg shadow-lg">
        <h2 class="text-3xl font-semibold text-center mb-6">Welcome</h2>
        <div class="flex flex-col gap-4">
            @auth
                <a href="{{ url('/home') }}" class="btn-primary py-2 rounded-lg text-center text-white hover:bg-blue-600 transition duration-300">Home</a>
            @else
                <a href="{{ route('login') }}" class="btn-primary py-2 rounded-lg text-center text-white hover:bg-blue-600 transition duration-300">Log in</a>
                @if (Route::has('register'))
                    <a href="{{ route('register') }}" class="btn-secondary py-2 rounded-lg text-center text-white hover:bg-gray-600 transition duration-300">Register</a>
                @endif
            @endauth
            <main class="py-4">
                @yield('content')
            </main>
        </div>
    </div>
</body>
</html>
