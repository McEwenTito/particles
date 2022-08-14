import sys
from simulation import Simulation



def run_sim(line_length, particle_positions):

    sim = Simulation(line_length, [position for position in particle_positions])
    print(sim.status)
    sim.start()
    print(sim.status)
    while sim.population != 0 :
        sim.step()
        print(sim.status)


if __name__ == '__main__':
    run_sim(sys.argv[1], sys.argv[2:])



