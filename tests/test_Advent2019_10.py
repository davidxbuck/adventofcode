# pytest tests
import numpy as np

from Advent2019_10 import Day10


class TestDay10():
    def test_instantiate(self):
        test = Day10('../tests/test_Advent2019_10a.txt')
        grid = ['.#..#',
                '.....',
                '#####',
                '....#',
                '...##']
        grid = [list(x) for x in grid]
        gridarray = np.array(grid).transpose()
        boolgrid = (gridarray == "#")
        assert (gridarray[3, :] == list('..#.#')).all()
        assert (gridarray[:, 2] == list('#####')).all()
        assert (boolgrid[:, 2] == [True, True, True, True, True]).all()
        assert (test.asteroid_map == gridarray).all()
        assert (test.boolean_asteroid_map == boolgrid).all()

