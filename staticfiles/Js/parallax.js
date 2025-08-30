// Este es el js de todo el menú principal 
window.addEventListener('scroll', () => {
    const bg = document.querySelector('.parallax-bg');
    const speed = parseFloat(bg.getAttribute('data-speed')) || 0.3;
    const yPos = window.scrollY * speed;
    bg.style.transform = `translateY(${yPos}px)`;
  });

  // Parpadeo cada pocos segundos
setInterval(() => {
    const robot = document.querySelector('.robot');
    robot.style.filter = 'brightness(0.7)';
    setTimeout(() => {
      robot.style.filter = 'brightness(1)';
    }, 100); // Duración del parpadeo
  }, 4000); // Cada 4 segundos

  const canvas = document.getElementById('letterGlitchCanvas');
  const ctx = canvas.getContext('2d');
  const fontSize = 15;
  const charWidth = 10;
  const charHeight = 20;
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:<>?,'.split('');
  let letters = [];
  let columns, rows;

  function resizeCanvas() {
    const rect = canvas.parentElement.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    canvas.style.width = rect.width + 'px';
    canvas.style.height = rect.height + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    columns = Math.floor(rect.width / charWidth);
    rows = Math.floor(rect.height / charHeight);
    letters = Array.from({ length: columns * rows }, () => ({
      char: getRandomChar(),
      color: getRandomColor()
    }));
  }

  function getRandomChar() {
    return chars[Math.floor(Math.random() * chars.length)];
  }

  function getRandomColor() {
    const palette = ['#2b4539', '#61dca3', '#61b3dc'];
    return palette[Math.floor(Math.random() * palette.length)];
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = fontSize + 'px monospace';
    ctx.textBaseline = 'top';

    letters.forEach((letter, i) => {
      const x = (i % columns) * charWidth;
      const y = Math.floor(i / columns) * charHeight;
      ctx.fillStyle = letter.color;
      ctx.fillText(letter.char, x, y);

      if (Math.random() < 0.05) {
        letter.char = getRandomChar();
        letter.color = getRandomColor();
      }
    });

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', () => {
    resizeCanvas();
  });

  resizeCanvas();
  draw();

// fondo de las cartas 
document.addEventListener("DOMContentLoaded", function () {
  tsParticles.load("tsparticles", {
    fullScreen: { enable: false },
    particles: {
      number: { value: 500 },
      color: { value: "#ffffff" },
      shape: { type: "circle" },
      opacity: { value: 0.7 },
      size: { value: 2 },
      move: {
        enable: true,
        speed: 0.6, //aumenta la velocidad de los circulos 
        direction: "none",
        outModes: { default: "out" }
      },
      links: { enable: false }
    },
    interactivity: {
      events: {
        onHover: { enable: false, mode: "repulse" },
        resize: true
      }
    },
    background: { color: "transparent" }
  });
});

window.addEventListener('load', () => {
  const particles = document.getElementById('tsparticles');
  const section = document.querySelector('section');
  particles.style.height = section.scrollHeight + 'px';
});





