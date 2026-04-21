import bpy
import random

class Scenario:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.agents = []

    def cleanup(self):
        # clear previous agents
        for obj in bpy.data.objects:
            if obj.name.startswith("agent_"):
                bpy.data.objects.remove(obj, do_unlink=True)
        self.agents = []

    def spawn_agents(self, n=100, spread=5.0):
        self.cleanup()
        for i in range(n):
            x = random.uniform(-spread, spread)
            y = random.uniform(-spread, spread)
            z = random.uniform(-spread, spread)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.2, location=(x, y, z))
            obj = bpy.context.object
            obj.name = f"agent_{i}"
            self.agents.append(obj)

    def run(self):
        print(f"Running scenario: {self.name}")
        self.spawn_agents()
