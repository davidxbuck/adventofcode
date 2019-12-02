import pytest

from Advent2019_02 import Intcode


class TestIntcode():
    def test_instantiate(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        assert code.program == [1, 0, 0, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_instantiate_noun_and_verb(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 33, 66)
        assert code.program == [1, 33, 66, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated


    def test_cmd1(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.cmd1()
        assert code.program == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_cmd2(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        code.cmd2()
        assert code.program == [150, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd99(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 8
        code.cmd99()
        assert code.program == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert code.terminated

    def test_prog_1(self):
        code = Intcode([1, 0, 0, 0, 99])
        result = code.run()
        assert result == 2
        assert code.program == [2, 0, 0, 0, 99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_2(self):
        code = Intcode([2,3,0,3,99], 3)
        result = code.run()
        assert result == 2
        assert code.program == [2,3,0,6,99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_3(self):
        code = Intcode([2,4,4,5,99,0], 4, 4)
        result = code.run()
        assert result == 2
        assert code.program == [2,4,4,5,99,9801]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_4(self):
        code = Intcode([1,1,1,4,99,5,6,0,99], 1, 1)
        result = code.run()
        assert result == 30
        assert code.program == [30,1,1,4,2,5,6,0,99]
        assert code.pointer == 8
        assert code.terminated
