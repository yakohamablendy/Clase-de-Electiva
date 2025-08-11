# Usar imagen base oficial de Node.js (versión LTS)
FROM node:18-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar package.json y package-lock.json (si existe)
COPY package*.json ./

# Instalar dependencias
RUN npm install --only=production

# Copiar el código de la aplicación
COPY . .

# Crear un usuario no-root para ejecutar la aplicación (seguridad)
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Cambiar la propiedad de los archivos al usuario nodejs
RUN chown -R nextjs:nodejs /app
USER nextjs

# Exponer el puerto que usa la aplicación
EXPOSE 3000

# Definir variables de entorno
ENV NODE_ENV=production
ENV PORT=3000

# Comando de salud para verificar que el contenedor funciona
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (res) => { process.exit(res.statusCode === 200 ? 0 : 1) })"

# Comando para ejecutar la aplicación
CMD ["npm", "start"]