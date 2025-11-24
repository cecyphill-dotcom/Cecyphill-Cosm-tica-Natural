
import http.server
import socketserver
import webbrowser

html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cecyphill Cosmética Natural</title>

    <style>
        :root {
            --verde-oscuro: #2e7d32;
            --verde-medio: #4caf50;
            --verde-suave: #dcedc8;
            --beige: #f5f5dc;
            --crema: #faf9f6;
            --gris-suave: #e0e0e0;
        }

        /* ANIMACIONES */
        @keyframes aparecerZoom {
            0% { opacity: 0; transform: scale(0.7); }
            100% { opacity: 1; transform: scale(1); }
        }

        @keyframes flotar {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }

        body {
            margin: 0;
            font-family: "Segoe UI", Arial, sans-serif;
            background-color: var(--crema);
            color: #333;
        }

        nav {
            background-color: var(--verde-oscuro);
            padding: 15px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        }

        nav .logo-text {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
            margin: 0;
            padding: 0;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-size: 1rem;
            padding: 8px 12px;
            border-radius: 5px;
        }

        nav ul li a:hover {
            background-color: var(--verde-medio);
        }

        header {
            background: url('productos.png') center/cover no-repeat;
            height: 70vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            border-bottom: 8px solid var(--verde-oscuro);
        }

        header img {
            width: 130px;
            position: absolute;
            top: 20px;
            left: 20px;
        }

        header h1 {
            background: rgba(46, 125, 50, 0.75);
            color: white;
            padding: 20px 50px;
            border-radius: 10px;
            font-size: 2.6rem;
            text-align: center;
            animation: aparecerZoom 2s ease-out forwards; 
        }

        section {
            padding: 50px 10%;
            border-bottom: 1px solid var(--gris-suave);
        }

        h2 {
            color: var(--verde-oscuro);
            margin-bottom: 10px;
            border-left: 6px solid var(--verde-medio);
            padding-left: 10px;
        }

        p {
            font-size: 1.1rem;
            line-height: 1.6;
        }

        /* --- ESTILOS FICHAS TÉCNICAS MODIFICADOS --- */
        .imagenes {
            display: flex;
            gap: 30px;
            justify-content: center;
            flex-wrap: wrap; /* Permite que bajen si no caben */
            flex-direction: row; /* Por defecto en fila (PC) */
        }

        .imagen-item {
            text-align: center;
            margin-bottom: 20px;
            flex: 1; /* Intenta ocupar espacio igual */
            min-width: 250px; /* Ancho mínimo antes de hacer salto de línea */
            max-width: 350px; /* Ancho máximo para que no se vean gigantes */
        }

        .imagen-item p {
            margin-top: 10px;
            font-weight: bold;
            color: var(--verde-oscuro);
            font-size: 1.1rem;
        }

        .imagenes img {
            width: 100%; /* Ocupa el ancho del contenedor (.imagen-item) */
            height: auto; /* Mantiene la proporción */
            border-radius: 10px;
            border: 3px solid var(--verde-medio);
            animation: flotar 3s ease-in-out infinite;
            object-fit: cover;
        }

        /* MEDIA QUERY: Solo aplica en pantallas pequeñas (Celulares/Tablets) */
        @media (max-width: 768px) {
            .imagenes {
                flex-direction: column; /* Cambia a columna vertical */
                align-items: center;    /* Centra todo verticalmente */
            }
            
            .imagen-item {
                width: 80%; /* En celular ocupan el 80% del ancho */
                max-width: none;
            }

            header h1 {
                font-size: 1.8rem; /* Título más pequeño en celular */
                padding: 15px 20px;
            }
            
            nav {
                flex-direction: column;
                gap: 10px;
            }
            
            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }
        }
        /* ----------------------------------------- */

        .contacto-box {
            text-align: center;
            padding: 40px 10%;
        }

        .contacto-btn {
            background-color: var(--verde-oscuro);
            color: white;
            padding: 15px 30px;
            font-size: 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            display: inline-block; /* Mejora el botón */
            margin-top: 20px;
        }

        footer {
            background-color: var(--verde-oscuro);
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            font-size: 1.1rem;
        }
    </style>
</head>

<body>
    <nav>
        <div class="logo-text">Cecyphill Cosmética Natural</div>
        <ul>
            <li><a href="#vision">Visión</a></li>
            <li><a href="#mision">Misión</a></li>
            <li><a href="#valores">Valores</a></li>
            <li><a href="#equipo">Equipo</a></li>
            <li><a href="#fichas tecnicas">Fichas técnicas</a></li>
            <li><a href="#Síguenos">Síguenos</a></li>
        </ul>
    </nav>

    <header>
        <img src="logo.png" alt="logo">
        <h1>Cecyphill Cosmética Natural</h1>
    </header>

    <section id="vision">
        <h2>Visión</h2>
        <p>Tener productos amigables con el medioambiente y con la piel.</p>
    </section>

    <section id="mision">
        <h2>Misión</h2>
        <p>Visibilizar la herbolaria ancestral mexicana.</p>
    </section>

    <section id="valores">
        <h2>Valores</h2>
        <ul>
            <li>Cuidado del medioambiente</li>
            <li>Respeto a las tradiciones</li>
        </ul>
    </section>

    <section id="equipo">
        <h2>Nuestro equipo</h2>
        <p><strong>Biotecnología:</strong> Creación de recetas y control de calidad.</p>
        <p><strong>PGA:</strong> Costos, etiquetas, marketing y cotizaciones.</p>
        <p><strong>Mecatrónica AMBI:</strong> Envasado y llenado de órdenes de producción.</p>
        <p><strong>Mecatrónica B y AV:</strong> Creación de maquinaria, envases y empaques.</p>
        <p><strong>Logística:</strong> Materia prima, almacenamiento y cronograma.</p>
        <p><strong>Programación:</strong> Página web, órdenes de producción, fichas técnicas, códigos QR y aplicación.</p>
    </section>

    <section id="fichas tecnicas">
        <h2>Fichas técnicas</h2>
        <div class="imagenes">
            <div class="imagen-item">
                <img src="codigo_malva.jpeg" alt="ficha_malva">
                <p>Malva</p>
            </div>
            <div class="imagen-item">
                <img src="codigo_nopal.jpeg" alt="ficha_nopal">
                <p>Nopal</p>
            </div>
            <div class="imagen-item">
                <img src="codigo_menta.jpeg" alt="ficha_menta">
                <p>Menta</p>
            </div>
        </div>
    </section>

    <section id="Síguenos" class="contacto-box">
        <h2>Síguenos</h2>
        <p>Si deseas más información, ¡síguenos en nuestra página de Instagram!</p>
        <a href="https://www.instagram.com/cecyphill" class="contacto-btn" target="_blank">Síguenos</a>
    </section>

    <footer>
        © 2025 Cecyphill Cosmética Natural
    </footer>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

print(f"Servidor iniciado en: http://localhost:{PORT}")
# Nota: Si la pestaña no se abre automáticamente, copia el link de arriba en tu navegador
webbrowser.open(f"http://localhost:{PORT}/index.html")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
