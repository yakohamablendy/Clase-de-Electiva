const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Ruta principal
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hola Mundo - DevOps</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background: rgba(255,255,255,0.1);
                    border-radius: 15px;
                    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
                }
                h1 {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                }
                p {
                    font-size: 1.2rem;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>¡Hola Mundo!</h1>
                <p>Aplicación DevOps con Node.js</p>
                <p>Puerto: ${PORT}</p>
                <p>Servidor funcionando correctamente ✅</p>
            </div>
        </body>
        </html>
    `);
});

// Ruta de salud para verificar que la app funciona
app.get('/health', (req, res) => {
    res.json({
        status: 'OK',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

app.listen(PORT, () => {
    console.log(`🚀 Servidor ejecutándose en http://localhost:${PORT}`);
    console.log(`📊 Health check disponible en http://localhost:${PORT}/health`);
});