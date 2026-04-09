  // Este el el js del mouse que da color al muve en el menú principal
  const splashArea = document.getElementById("splash-area");

  splashArea.addEventListener("mousemove", (e) => {
    const splash = document.createElement("div");
    splash.classList.add("cursor-splash");

    // Generar un color aleatorio
    const hue = Math.floor(Math.random() * 360);
    splash.style.backgroundColor = `hsl(${hue}, 100%, 70%)`;

    // Posición relativa al contenedor
    const rect = splashArea.getBoundingClientRect();
    splash.style.left = (e.clientX - rect.left - 6) + "px";
    splash.style.top = (e.clientY - rect.top - 6) + "px";

    splashArea.appendChild(splash);
    setTimeout(() => splash.remove(), 600);
  });

