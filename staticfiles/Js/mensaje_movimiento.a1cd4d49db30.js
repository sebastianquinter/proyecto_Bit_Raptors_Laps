// mesaje con movimiento 

document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.getElementById("fuzzyCanvas");
    const ctx = canvas.getContext("2d");
  
    const text = "¿Por qué nos eligen?";
    const fontSize = 70;
    const fontFamily = "calibri";
    const baseIntensity = 0.0;
    const hoverIntensity = 0.5;
    const fuzzRange = 30;
  
    canvas.width = 600;
    canvas.height = 150;
  
    const offCanvas = document.createElement("canvas");
    const offCtx = offCanvas.getContext("2d");
  
    offCanvas.width = canvas.width;
    offCanvas.height = canvas.height;
  
    offCtx.font = `bold ${fontSize}px ${fontFamily}`;
    offCtx.fillStyle = "#fff";
    offCtx.textAlign = "center";
    offCtx.textBaseline = "middle";
    offCtx.fillText(text, offCanvas.width / 2, offCanvas.height / 2);
  
    let isHovering = false;
  
    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const intensity = isHovering ? hoverIntensity : baseIntensity;
  
      for (let y = 0; y < canvas.height; y++) {
        const dx = Math.floor(intensity * (Math.random() - 0.5) * fuzzRange);
        ctx.drawImage(offCanvas, 0, y, canvas.width, 1, dx, y, canvas.width, 1);
      }
  
      requestAnimationFrame(render);
    }
  
    canvas.addEventListener("mousemove", () => {
      isHovering = true;
    });
  
    canvas.addEventListener("mouseleave", () => {
      isHovering = false;
    });
  
    render();
  });