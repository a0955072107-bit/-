# Guía de instalación

¡Gracias por su compra! Con esta guía podrá personalizar su sitio y publicarlo en unos 30 minutos. No necesita saber programar.

---

## 1. Qué incluye

```
index.html           ← entrada de idiomas: lleva a cada visitante a su idioma
es/index.html        ← versión en español (todo el sitio es este único archivo)
en/index.html        ← versión en inglés
zh-TW/index.html     ← versión en chino tradicional
zh-CN/index.html     ← versión en chino simplificado
ja/index.html        ← versión en japonés (en algunas plantillas)
*/images/            ← fotos, una carpeta por idioma
GUIA.md              ← esta guía (GUIDE.md es la guía en inglés)
LICENCIA.md          ← lo que puede y no puede hacer
PRIVACIDAD-PLANTILLA.md ← plantilla de aviso de privacidad
```

Cada página tiene un selector de idioma en el encabezado (EN / 繁 / 简 / ES). ¿Quiere todos los idiomas? Suba la carpeta completa. ¿Solo necesita español? Suba la carpeta `es/` y quite del selector los enlaces que no use (busque `lang-switch`; también hay un grupo igual en el pie de página, busque `foot-lang`).

**Si cambia un texto en un idioma, recuerde actualizar también los demás.**

## 2. Herramientas que necesita (todas gratuitas)

- Un editor de texto: se recomienda [VS Code](https://code.visualstudio.com/). El Bloc de notas o TextEdit también sirven.
- Un navegador: Chrome, Edge, Safari o Firefox.

Abra `es/index.html` en su navegador para ver el sitio. Después de editar, guarde el archivo y actualice el navegador.

## 3. Cambiar los textos

Abra `es/index.html` en su editor, presione `Ctrl + F` (Mac: `⌘ + F`), busque el texto que quiere cambiar (nombre del negocio, teléfono…) y escriba encima.

Cada sección empieza con una marca como esta:

```html
<!-- ==================== Section: Menú ==================== -->
```

**¿No necesita una sección?** Borre desde su marca hasta la siguiente marca y quite su enlace del menú de navegación.

### Lo que debe cambiar sí o sí (busque esto)

| Busque | Cámbielo por |
|---|---|
| El nombre de negocio de ejemplo | El nombre de su negocio (use "Reemplazar todo") |
| Los teléfonos de ejemplo (`55 1234 5678`, `(305) 555-0152`, etc.) y los enlaces `tel:` | Su número de teléfono |
| `wa.me/` seguido del número de ejemplo | Su número de WhatsApp con código de país, solo dígitos (por ejemplo `wa.me/525512345678`), o un enlace de Messenger / Instagram / LINE |
| La dirección de ejemplo en `maps.google.com/?q=` | Su dirección |
| `your-form-id` | El ID de su formulario de Formspree (vea la sección 6) |
| `<title>` y `description` | Su nombre y una descripción de una línea (se muestran en los resultados de Google) |
| El bloque `application/ld+json` | Nombre, teléfono, dirección, horario y moneda (ayuda a que Google Maps y el buscador muestren bien sus datos) |
| Precios y moneda | Sus precios. Las plantillas usan MXN, COP o USD según el ejemplo; ajuste también `priceCurrency` / `currenciesAccepted` en el JSON-LD |

Las reseñas, cifras y testimonios de ejemplo están marcados con el comentario `Contenido de ejemplo`. Cámbielos por datos reales antes de publicar.

## 4. Cambiar colores y fuentes

Cerca del inicio de `index.html` encontrará la **CONFIGURACIÓN DEL TEMA**:

```css
:root {
  --brand: #b5532c;   /* color principal: botones, destacados */
  --bg: #f7f1e8;      /* fondo */
  --text: #2a211c;    /* color del texto */
  ...
}
```

Cambie estos valores y todo el sitio se actualiza. ¿Necesita una paleta? Pruebe [coolors.co](https://coolors.co/).

> Consejo: mantenga suficiente contraste entre el texto y el fondo. Puede revisarlo con el [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

## 5. Usar sus propias fotos

Las áreas de imagen vienen con ilustraciones hechas con degradados, así que no hay licencias de fotos de stock de las que preocuparse. Para usar fotos reales:

1. Ponga su foto en la carpeta `images/` junto a su `index.html`, por ejemplo `images/hero.jpg`.
2. En `index.html`, busque `Cambiar por una foto`. Encontrará comentarios como este:
   ```css
   /* Cambiar por una foto: .img-hero { background: url(images/hero.jpg) center/cover; } */
   ```
3. Copie esa línea (sin las marcas de comentario `/*` y `*/`) justo antes de `</style>` y cambie el nombre del archivo.

**Consejos para las fotos**
- Con 1600 a 2000 px de ancho es suficiente. Comprímalas con [Squoosh](https://squoosh.app/) para que el sitio cargue más rápido.
- Use solo fotos propias o con licencia de uso (por ejemplo, imágenes gratuitas para uso comercial de [Unsplash](https://unsplash.com/) o [Pexels](https://www.pexels.com/)).

## 6. Recibir el formulario por correo (Formspree, gratis)

1. Cree una cuenta en [formspree.io](https://formspree.io/) y haga clic en **New Form**.
2. Copie el ID que aparece al final de la URL del formulario, por ejemplo `xyzabcd`.
3. Busque `your-form-id` en `index.html` y cámbielo por su ID.

Desde ese momento los envíos le llegan a su correo. El plan gratuito incluye 50 envíos al mes. ¿Prefiere no usar formulario? Borre la sección del formulario y deje los botones de teléfono y WhatsApp.

## 7. Publicar el sitio (elija una opción, todas gratuitas)

### A. Netlify Drop (la más fácil, unos 3 minutos)
1. Entre a [app.netlify.com/drop](https://app.netlify.com/drop).
2. Arrastre la carpeta completa (se publican todos los idiomas) o solo la carpeta de un idioma.
3. Listo. Recibirá una dirección `xxx.netlify.app`; cree una cuenta gratuita para conservar el sitio y cambiarle el nombre.

### B. GitHub Pages
1. Cree una cuenta de GitHub y un repositorio nuevo.
2. Haga clic en **Add file → Upload files** y suba `index.html` y la carpeta `images/`.
3. Vaya a **Settings → Pages**, elija la rama `main` y haga clic en Save.
4. En uno o dos minutos su sitio estará en `https://su-usuario.github.io/nombre-del-repositorio/`.

### C. Cloudflare Pages
Entre a [pages.cloudflare.com](https://pages.cloudflare.com/), elija **Upload assets** y suba la carpeta.

### Usar su propio dominio (por ejemplo `www.sunegocio.com`)
Compre un dominio en un registrador (Cloudflare, Namecheap, Porkbun…) y siga los pasos de "Custom domain" en Netlify, GitHub o Cloudflare.

## 8. Aparecer en Google

1. Agregue y verifique su sitio en [Google Search Console](https://search.google.com/search-console).
2. Cree un [Perfil de Negocio de Google](https://business.google.com/) y agregue su sitio web. Para un negocio local, este es el paso más efectivo.

## 9. Privacidad y protección de datos

- **Mapas**: las plantillas enlazan a Google Maps en lugar de insertarlo, así que no se carga nada de Google hasta que el visitante hace clic.
- **Fuentes**: las fuentes se cargan desde Google Fonts. Si su negocio está en la Unión Europea (por ejemplo, en España) y quiere cumplir el RGPD de forma estricta, aloje las fuentes usted mismo:
  1. Entre a [gwfh.mranftl.com/fonts](https://gwfh.mranftl.com/fonts) (google-webfonts-helper) y elija las fuentes que aparecen en el enlace `fonts.googleapis.com` cerca del inicio de `index.html`.
  2. Descargue los archivos `woff2` en una carpeta `fonts/` junto a `index.html` y copie el CSS generado dentro del bloque `<style>`.
  3. Borre las etiquetas `<link>` que apuntan a `fonts.googleapis.com` y `fonts.gstatic.com`.
- **Aviso de privacidad**: adapte `PRIVACIDAD-PLANTILLA.md`, guárdelo como `privacidad.html` y enlácelo en el pie de página. Muchos países de habla hispana tienen leyes de datos personales (por ejemplo, la LFPDPPP en México, la Ley 1581 de 2012 en Colombia o el RGPD en España). En España también suele ser obligatorio un **Aviso legal** con los datos de la empresa.
- **Formularios**: Formspree guarda los envíos. Menciónelo en su aviso de privacidad.

## 10. Preguntas frecuentes

**Las fuentes se ven distintas en mi teléfono.**
La plantilla carga Google Fonts en línea. Con una conexión lenta, el navegador muestra primero una fuente del sistema; es normal.

**¿Puedo hacer un sitio de varias páginas?**
Sí. Copie `index.html`, por ejemplo como `nosotros.html`, borre las secciones que no necesite y apunte los enlaces del menú a `nosotros.html`.

**Rompí algo.**
Guarde una copia del original antes de editar, o vuelva a descargar su compra.

---

## ¿Quiere que lo personalicemos por usted?

¿No tiene tiempo de editarlo? Podemos convertir esta plantilla en un sitio listo para publicar para su negocio: sus textos, fotos, colores, enlaces de reserva y dominio, todo configurado. Escríbanos por Gumroad o vea nuestro **Servicio de personalización de sitios web**.
