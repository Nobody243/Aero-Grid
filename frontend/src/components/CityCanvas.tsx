'use client';

import React, { useEffect, useRef } from 'react';

export default function CityCanvas() {
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

  return <canvas ref={canvasRef} width={600} height={600} className="border border-slate-800 rounded shadow-2xl" />;
}
