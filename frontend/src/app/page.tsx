'use client';

import React from 'react';
import CityCanvas from '@/components/CityCanvas';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-[#06090f] text-white p-6">
      <h1 className="text-2xl font-bold tracking-wider">AERO-GRID // Autonomous Drone Routing</h1>
      <div className="mt-6 grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="md:col-span-3 border border-slate-800 rounded-lg h-[600px] flex items-center justify-center">
          <CityCanvas />
        </div>
        <div className="border border-slate-800 rounded-lg p-4">
          <h2 className="text-lg font-semibold">Mission Parameters</h2>
        </div>
      </div>
    </main>
  );
}
