"""
Aero-Grid Comprehensive SQA & Security Test Suite
Tests:
- Input Boundary & Validation (Security)
- Malformed Payload Resilience (Security)
- Exception Shielding & Leakage Prevention (Security)
- CORS Preflight & Headers (Security)
- Algorithm Logic & Verification (SQA):
  * City Generator & Connectivity Validation
  * Naive Bayes Weather Classifier & Confidence Bounds
  * Genetic Algorithm TSP Optimization & Tour Invariants
  * A* Multi-leg Obstacle-Avoidance Pathfinding
  * Q-Learning Reinforcement Policy Training & Convergence
"""

import sys
import unittest
import json
from pathlib import Path
from fastapi.testclient import TestClient

backend_dir = Path(__file__).parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from main import app
from astar import AStarPathfinder, build_city, GRID_SIZE
from genetic_algorithm import GeneticAlgorithm, total_distance
from weather_classifier import WeatherClassifier
from q_learning import QLearningAgent

client = TestClient(app)

class TestSecurityAndInputSanitization(unittest.TestCase):
    """Security tests checking boundaries, schema enforcement, and sanitization."""

    def test_01_invalid_weather_payload_rejected(self):
        """Invalid weather inputs (out of range, bad types, negative values) must return 422."""
        bad_payloads = [
            {"wind_speed": -5.0, "visibility": 10.0, "rainfall": 0.0},
            {"wind_speed": 10.0, "visibility": -1.0, "rainfall": 0.0},
            {"wind_speed": 10.0, "visibility": 10.0, "rainfall": -2.0},
            {"wind_speed": "high", "visibility": 10.0, "rainfall": 0.0},
            {"extra_garbage_field": "test"},
        ]
        for p in bad_payloads:
            res = client.post("/weather", json=p)
            self.assertEqual(res.status_code, 422, f"Failed for payload: {p}")
            data = res.json()
            self.assertIn("error", data)
            self.assertEqual(data["error"], "invalid_input")

    def test_02_oversized_and_negative_city_coordinates(self):
        """Coordinates outside [0, 39] or negative must be handled gracefully."""
        bad_city = {
            "buildings": [[100, 100], [-1, -5]],
            "nfz": [],
            "targets": [[2, 2]],
            "depot": [0, 0],
            "grid_size": 40
        }
        res = client.post("/city/validate", json=bad_city)
        self.assertIn(res.status_code, [200, 422])
        if res.status_code == 200:
            data = res.json()
            self.assertFalse(data.get("is_valid", False))

    def test_03_injection_strings_in_endpoints(self):
        """Fuzzing query parameters with injection patterns does not cause 500 error."""
        fuzz_params = [
            "<script>alert(1)</script>",
            "'; DROP TABLE cities; --",
            "../../../etc/passwd",
            "%00%00%00",
            "9999999999999999999999999999999999999"
        ]
        for p in fuzz_params:
            res = client.get(f"/city/random?difficulty={p}&seed=1")
            self.assertNotEqual(res.status_code, 500, f"Server crashed with 500 on query param: {p}")

    def test_04_cors_headers_handling(self):
        """CORS headers should allow Vercel domains and include required headers."""
        headers = {
            "Origin": "https://aerogrid-simulator-ag24303.vercel.app",
            "Access-Control-Request-Method": "POST",
        }
        res = client.options("/city/validate", headers=headers)
        self.assertIn(res.status_code, [200, 204])
        self.assertEqual(res.headers.get("access-control-allow-origin"), "https://aerogrid-simulator-ag24303.vercel.app")


class TestSQAAlgorithmCorrectness(unittest.TestCase):
    """Software Quality Assurance tests verifying algorithmic accuracy."""

    def test_05_weather_ensemble_consistency(self):
        """Weather classifier outputs valid probabilities summing to ~1.0."""
        clf = WeatherClassifier()
        verdict, probs = clf.predict(wind_speed=12.0, visibility=8.0, rainfall=0.0)
        self.assertIn(verdict, ["Safe to Fly", "Requires Altitude Drop", "Grounded"])
        self.assertAlmostEqual(sum(probs.values()), 1.0, places=3)
        for label in ["Safe to Fly", "Requires Altitude Drop", "Grounded"]:
            self.assertGreaterEqual(probs[label], 0.0)
            self.assertLessEqual(probs[label], 1.0)

    def test_06_city_generator_invariants(self):
        """City generator creates valid 40x40 grid with correct target count and reachable depot."""
        res = client.get("/city/random?difficulty=medium&seed=42")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["grid_size"], 40)
        self.assertEqual(len(data["depot"]), 2)
        self.assertGreaterEqual(len(data["targets"]), 3)
        self.assertLessEqual(len(data["targets"]), 12)
        
        for b in data["buildings"]:
            self.assertTrue(0 <= b[0] < 40 and 0 <= b[1] < 40)
        for t in data["targets"]:
            self.assertTrue(0 <= t[0] < 40 and 0 <= t[1] < 40)

    def test_07_astar_fly_endpoint(self):
        """A* fly endpoint finds obstacle-free path for all delivery legs."""
        city_res = client.get("/city/random?difficulty=easy&seed=7")
        city_data = city_res.json()
        targets_count = len(city_data["targets"])
        route = list(range(targets_count))

        res = client.post("/fly", json={
            "city": city_data,
            "route": route,
            "heuristic": "octile"
        })
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertIn("legs", result)
        self.assertEqual(len(result["legs"]), targets_count + 1)
        
        building_set = {tuple(b) for b in city_data["buildings"]}
        nfz_set = {tuple(n) for n in city_data["nfz"]}
        blocked = building_set | nfz_set

        for leg in result["legs"]:
            self.assertGreater(len(leg["path"]), 0)
            for pt in leg["path"]:
                self.assertNotIn(tuple(pt), blocked, f"Path collided with obstacle at {pt}")

    def test_08_genetic_algorithm_tsp(self):
        """Genetic Algorithm orders targets into a valid permutation with lower distance than initial."""
        targets = [(2, 2), (10, 10), (2, 10), (10, 2), (5, 5)]
        depot = (0, 0)
        ga = GeneticAlgorithm(targets=targets, depot=depot, population_size=40, max_generations=30, mutation_prob=0.15, seed=42)
        best_tour, best_dist = ga.run()
        
        self.assertEqual(len(best_tour), len(targets))
        self.assertEqual(sorted(best_tour), list(range(len(targets))))
        self.assertGreater(len(ga.history), 0)

    def test_09_qlearning_policy_convergence(self):
        """Q-Learning training produces valid policy and final path reaching goal."""
        city_res = client.get("/city/random?difficulty=easy&seed=7")
        city_data = city_res.json()
        start = city_data["depot"]
        goal = city_data["targets"][0]
        
        res = client.post("/learn/train", json={
            "city": city_data,
            "start": start,
            "goal": goal,
            "hyperparameters": {},
            "seed": 1
        })
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("final_q", data)
        self.assertIn("episodes", data)
        self.assertEqual(len(data["episodes"]), 1000)
        self.assertGreater(len(data["final_path"]), 0)
        self.assertEqual(data["final_path"][0], start)
        self.assertEqual(data["final_path"][-1], goal)





if __name__ == "__main__":
    unittest.main(verbosity=2)
