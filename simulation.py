import itertools
from particle import Particle


class Simulation():
    def __init__(self, line_length, particle_positions: list):
        self.line_length = int(line_length)
        self.particles = []
        self.particle_positions = particle_positions
        self.population = len(self.particle_positions)
        self.counter = 0


    @property
    def status(self):
        return (f"___STATUS___\n"
                f"population: {self.population} "
                 f"\nseconds:  {self.counter}"
                f"\nparticles: {[(particle.position, particle.direction_text) for particle in self.particles]}"
                f"\n__________STATUS__\n")

    def update_population(self, particles):
        for particle in particles:
            if particle.position <= 0 or particle.position > self.line_length:
                particles.remove(particle)
        self.particles = particles
        self.population = len(particles)



    def update_direction(self):
        for a, b in itertools.combinations(self.particles, 2):
            if a.position == b.position:
                print("Colided .. ... Reversing direction")
                a.reverse_direction()
                b.reverse_direction()


    def step(self):
        for particle in self.particles:
            particle.move()
        self.update_population(self.particles)
        self.update_direction()
        self.counter += 1



    def launch_particle(self, position):
        particle = Particle(self.line_length, position)
        return particle


    def start(self):
        print("starting")
        for position in self.particle_positions:
            particle = self.launch_particle(int(position))
            self.particles.append(particle)