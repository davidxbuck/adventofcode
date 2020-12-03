# Advent of Code 2018 Day 15

import itertools
import queue
from collections import defaultdict, Counter

import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


class Creature(object):
    newid = itertools.count()

    def __init__(self, x, y, species, hit_points=200, attack_points=3):
        self.x = x
        self.y = y
        self.species = species
        self.hit_points = hit_points
        self.attack_points = attack_points
        self.last_turn = None
        self.alive = True
        self.neighbours = []

    # def __str__(self):
    #     return "Creature {}, position {}, direction {}, next turn is: {}".format(self.id, self.coords,
    #                                                                              self.direction, self.next_direction)

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    # def __lt__(self, other):
    #     return self.x * grid_size + self.y < other.x * grid_size + other.y

    @property
    def coords(self):
        return [self.x, self.y]

    def check_neighbours(self):
        self.neighbours = [(self.coords + direction).tolist() for direction in dir]
        self.neighbourcheck = [grid[coord[0], coord[1]] for coord in self.neighbours]
        for ix, creature_ in enumerate(creatures):
            if creature_.alive and creature_.coords in self.neighbours:
                self.neighbourcheck[self.neighbours.index(creature_.coords)] = creatures[ix].species[0]

    def attack(self):
        self.check_neighbours()
        if isinstance(self, Elf):
            oppo = "Goblin"
        else:
            oppo = "Elf"
        oppos = []
        oppocount = 0
        for ix, creature_ in enumerate(creatures):
            if creature_.species == oppo and creature_.alive and creature_.hit_points > 0:
                oppocount += 1
                if creature_.coords in self.neighbours:
                    oppos.append([creature_.hit_points, creature_.x, creature_.y, ix])

        if len(oppos) == 0:
            return
        attack = sorted(oppos)[0]
        creatures[attack[3]].hit_points -= self.attack_points
        if creatures[attack[3]].hit_points <= 0:
            creatures[attack[3]].hit_points = 0
            creatures[attack[3]].alive = False
        return


class Elf(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y, "Elf")
        self.id = next(self.__class__.newid)
        self.attack_points = 3


class Goblin(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y, "Goblin")
        self.id = next(self.__class__.newid)

def is_war_over(creatures):
    c = Counter(getattr(creature, 'species') for creature in creatures)
    return True if len(c) < 2 else False

def bring_out_your_dead():
    for ix, creature in enumerate(creatures
                                  ):
        if not creature.alive:
            creatures.pop(ix)


def search_grid(travelgrid, queue):
    distgrid = np.full([grid_size, grid_size], 999)
    traveldist = 0
    while queue.qsize() > 0:
        traveldist += 1
        for _ in range(queue.qsize()):
            checkx, checky = queue.get()
            for dirx, diry in dir:
                if travelgrid[checkx + dirx, checky + diry] == True or [checkx + dirx, checky + diry] in queue.queue:
                    continue
                travelgrid[checkx + dirx, checky + diry] = True
                distgrid[checkx + dirx, checky + diry] = traveldist
                queue.put([checkx + dirx, checky + diry])
    return distgrid


def visualise_grid(creatures):
    outgrid = np.copy(grid)
    grid_size = len(grid[0])
    print("  00000000001111111111222222222233"[:grid_size+2])
    print("  01234567890123456789012345678901"[:grid_size+2])
    for creature in creatures:
        if isinstance(creature, Elf):
            outgrid[creature.x, creature.y] = "E"
        elif isinstance(creature, Goblin):
            outgrid[creature.x, creature.y] = "G"

    for i in range(grid_size):
        print("{:02d}{}".format(i, "".join(outgrid[i])))

def main():
    global creatures, grid, dir, grid_size
    dir = np.array([[-1, 0], [0, -1], [0, 1], [1, 0]])
    # Read file and extract dependencies
    file = open("../inputs2018/Advent15", 'r')
    inputs = [row.strip("\n") for row in file]

    grid_size = len(inputs[0])
    grid = np.empty([grid_size, grid_size], dtype=str)
    basegrid = np.zeros([grid_size, grid_size], dtype=bool)
    creatures = []

    # populate grid extract creatures

    for x in range(grid_size):
        for y in range(len(inputs[x])):
            if inputs[x][y] == "G":
                creatures.append(Goblin(x, y))
                grid[x, y] = "."
                creatures[-1].check_neighbours()
            elif inputs[x][y] == "E":
                creatures.append(Elf(x, y))
                grid[x, y] = "."
                creatures[-1].check_neighbours()
            else:
                grid[x, y] = inputs[x][y]
                if grid[x, y] == "#":
                    basegrid[x, y] = True

    # To move, the unit first considers the squares that are in range and determines which of those squares it could
    # reach in the fewest steps. A step is a single movement to any adjacent (immediately up, down, left, or right)
    # open (.) square. Units cannot move into walls or other units. The unit does this while considering the current
    # positions of units and does not do any prediction about where units will be later. If the unit cannot reach
    # (find an open path to) any of the squares that are in range, it ends its turn. If multiple squares are in range
    # and tied for being reachable in the fewest steps, the square which is first in reading order is chosen.
    # For example:

    # Targets:      Inrange:      Reachable:    Nearest:      Chosen:
    # #######       #######       #######       #######       #######
    # #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
    # #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
    # #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
    # #######       #######       #######       #######       #######


    visualise_grid(creatures)
    war_is_over = False
    rounds = 0
    while not war_is_over:
        move_order = sorted(creatures, key=lambda x: x.coords)
        for creature in move_order:
            if not creature.alive:
                continue

            # Check we still have both species

            war_is_over = is_war_over(creatures)
            if war_is_over:
                break

            # Fight

            creature.check_neighbours()
            if (isinstance(creature, Elf) and "G" in creature.neighbourcheck) or (
                    isinstance(creature, Goblin) and "E" in creature.neighbourcheck):
                creature.attack()
                continue

            # Stuck

            if "." not in creature.neighbourcheck:
                continue

            # Move

            if isinstance(creature, Elf):
                opponents = [cc for cc in list(filter(lambda x: isinstance(x, Goblin), creatures))]
            else:
                opponents = [cc for cc in list(filter(lambda x: isinstance(x, Elf), creatures))]

            # Identify in-range targets

            inrange = []
            for opponent in opponents:
                opponent.check_neighbours()
                for neighbourcheck in enumerate(opponent.neighbourcheck):
                    if neighbourcheck[1] == ".":
                        inrange.append(opponent.neighbours[neighbourcheck[0]])

            # Determine chosen target by working out number of moves to all targets

            travelgrid = np.copy(basegrid)
            for creature_ in creatures:
                if creature_.alive:
                    travelgrid[creature_.x, creature_.y] = True

            searchqueue = queue.Queue()
            searchqueue.put(creature.coords)
            distgrid = search_grid(travelgrid, searchqueue)

            targets = []
            for x, y in inrange:
                if distgrid[x, y] < 999:
                    targets.append([distgrid[x, y], x, y])

            if len(targets) == 0:
                continue  # Targets all unreachable this move
            chosen = sorted(targets)[0][1:]

            # work out shortest route from chosen back to starting point, following reading order

            startval = distgrid[chosen[0], chosen[1]]
            searchdict = defaultdict(list)
            searchdict[startval].append(chosen)
            q = queue.Queue()
            q.put(chosen)
            while startval > 0:
                startval -= 1
                for _ in range(q.qsize()):
                    checkx, checky = q.get()
                    for dirx, diry in dir:
                        if distgrid[checkx + dirx, checky + diry] != startval or [checkx + dirx,
                                                                                  checky + diry] in q.queue:
                            continue
                        searchdict[startval].append([checkx + dirx, checky + diry])
                        q.put([checkx + dirx, checky + diry])

            # move

            moveto = sorted(searchdict[1])[0]
            creature.x = moveto[0]
            creature.y = moveto[1]
            creature.check_neighbours()

            # attack if now in range

            if (isinstance(creature, Elf) and "G" in creature.neighbourcheck) or (
                    isinstance(creature, Goblin) and "E" in creature.neighbourcheck):
                creature.attack()
                continue

        # remove any creatures that died during last round

        bring_out_your_dead()

        # if only one species of creature left, war has finished
        war_is_over = is_war_over(creatures)
        if war_is_over:
            break
        rounds += 1



    visualise_grid(creatures)
    bring_out_your_dead()

    hit_points = 0
    for creature in creatures:
        if creature.alive and creature.hit_points > 0:
            print(creature.id, creature.species, creature.hit_points)
            hit_points += creature.hit_points

    c = Counter(getattr(creature, 'species') for creature in creatures)

    for k, v in c.items():
        print("{} * {} remaining".format(y, k))

    print("Roundx", rounds)
    print("Hit points", hit_points)
    print("R*HP", (rounds) * hit_points)





if __name__ == "__main__":
    main()
