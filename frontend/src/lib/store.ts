import { create } from 'zustand';
// Optimized obstacle 2D grid matrix representation

interface MissionState {
  depot: [number, number];
  targets: [number, number][];
  buildings: [number, number][];
  setDepot: (p: [number, number]) => void;
}

export const useMissionStore = create<MissionState>((set) => ({
  depot: [0, 0],
  targets: [[35, 35]],
  buildings: [],
  activeRoute: [] as [number, number][],
  astarPath: [] as [number, number][],
  metrics: { distance: 0, time_seconds: 0 },
  setDepot: (p) => set({ depot: p }),
  toggleBuilding: (p: [number, number]) => set((s) => ({ buildings: [...s.buildings, p] })),
}));
