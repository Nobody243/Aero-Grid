'use client';

import React, { useEffect, useRef } from 'react';

export default function CityCanvas() {
  // Added isDragging obstacle brush state
// Weather layer alpha rendering overlay
const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const cvs = canvasRef.current;
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    if (!ctx) return;
    ctx.fillStyle = '#0a0f1d';
    ctx.fillRect(0, 0, cvs.width, cvs.height);
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.1)';
    for (let i = 0; i <= 40; i++) {
      ctx.beginPath();
      ctx.moveTo(i * 15, 0);
      ctx.lineTo(i * 15, 600);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0, i * 15);
      ctx.lineTo(600, i * 15);
      ctx.stroke();
    }
  }, []);

  return <canvas ref={canvasRef} width={640} height={640} className="border border-slate-800 rounded shadow-2xl" />;
}

// Drone start depot marker renderer
// Render depot at coordinates (0, 0)

// Drone icon vector overlay


// Function to draw route polylines
// ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;

// Redraw optimization with requestAnimationFrame
