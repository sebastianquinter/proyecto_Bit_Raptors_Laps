document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value.trim();
    const email = document.getElementById('email').value.trim();
    const asunto = document.getElementById('asunto').value.trim() || 'Sin asunto';
    const mensaje = document.getElementById('mensaje').value.trim();

    const numeroDestino = '573125260493'; // ← Reemplaza con TU número (sin +, sin espacios)
    
    const texto = `Hola, soy ${nombre}.
    Mi correo es: ${email}.
    Asunto: ${asunto}
    Mensaje: ${mensaje}`;

    const url = `https://wa.me/${numeroDestino}?text=${encodeURIComponent(texto)}`;
    window.open(url, '_blank');
  });