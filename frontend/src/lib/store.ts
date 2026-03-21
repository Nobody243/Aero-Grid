import { create } from 'zustand';

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
  setDepot: (p) => set({ depot: p }),
  toggleBuilding: (p: [number, number]) => set((s) => ({ buildings: [...s.buildings, p] })),
}));
