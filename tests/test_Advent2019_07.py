# pytest tests

from types import GeneratorType
from Advent2019_Intcode import Intcode


class TestIntcode():
    def test_instantiate(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        assert code.program == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_instantiate_noun_and_verb(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 33, 66)
        assert code.program == [1, 33, 66, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_cmd01_position(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert code.program == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd01_immediate1(self):
        code = Intcode([101, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert code.parm1
        assert not code.parm2
        assert not code.parm3
        assert code.program == [101, 9, 10, 49, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd01_immediate2(self):
        code = Intcode([1001, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert not code.parm1
        assert code.parm2
        assert not code.parm3
        assert code.program == [1001, 9, 10, 40, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd01_immediate3(self):
        code = Intcode([1101, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert code.parm1
        assert code.parm2
        assert not code.parm3
        assert code.program == [1101, 9, 10, 19, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd02_position(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd02()
        assert code.program == [150, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert not code.terminated

    def test_cmd02_immediate1(self):
        code = Intcode([1, 9, 10, 3, 102, 5, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd02()
        assert code.parm1
        assert not code.parm2
        assert not code.parm3
        assert code.program == [250, 9, 10, 3, 102, 5, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert not code.terminated

    def test_cmd02_immediate2(self):
        code = Intcode([1, 9, 10, 12, 1002, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd02()
        assert not code.parm1
        assert code.parm2
        assert not code.parm3
        assert code.program == [132, 9, 10, 12, 1002, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert not code.terminated

    def test_cmd02_immediate3(self):
        code = Intcode([1, 9, 10, 12, 1102, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd02()
        assert code.parm1
        assert code.parm2
        assert not code.parm3
        assert code.program == [33, 9, 10, 12, 1102, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert not code.terminated

    def test_cmd03(self):
        code = Intcode([3, 2, 10, 12, 1102, 3, 11, 0, 99, 30, 40, 50], inp=[5])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd03()
        assert code.inp == [5]
        assert not code.parm1
        assert not code.parm2
        assert not code.parm3
        assert code.program == [3, 2, 5, 12, 1102, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 2
        assert not code.terminated

    def test_cmd05_position_jump_if_true_true(self):
        code = Intcode([5, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd05()
        assert code.program == [5, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 40
        assert not code.terminated

    def test_cmd05_position_jump_if_true_false(self):
        code = Intcode([5, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd05()
        assert code.program == [5, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 3
        assert not code.terminated

    def test_cmd06_position_jump_if_false_true(self):
        code = Intcode([6, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd06()
        assert code.program == [6, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 3
        assert not code.terminated

    def test_cmd06_position_jump_if_false_false(self):
        code = Intcode([6, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd06()
        assert code.program == [6, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 40
        assert not code.terminated

    def test_cmd07_less_than_true(self):
        code = Intcode([7, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd07()
        assert code.program == [7, 7, 10, 1, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd07_less_than_false(self):
        code = Intcode([7, 10, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd07()
        assert code.program == [7, 10, 10, 0, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd08_equals_true(self):
        code = Intcode([7, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd08()
        assert code.program == [7, 7, 10, 0, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd08_equals_false(self):
        code = Intcode([7, 10, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd08()
        assert code.program == [7, 10, 10, 1, 2, 3, 11, 0, 99, 30, 40, 50]
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
        assert result == (2, True)
        assert code.program == [2, 0, 0, 0, 99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_2(self):
        code = Intcode([2, 3, 0, 3, 99], 3)
        result = code.run()
        assert result == (2, True)
        assert code.program == [2, 3, 0, 6, 99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_3(self):
        code = Intcode([2, 4, 4, 5, 99, 0], 4, 4)
        result = code.run()
        assert result == (2, True)
        assert code.program == [2, 4, 4, 5, 99, 9801]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_4(self):
        code = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99], 1, 1)
        result = code.run()
        assert result == (30, True)
        assert code.program == [30, 1, 1, 4, 2, 5, 6, 0, 99]
        assert code.pointer == 8
        assert code.terminated

    def test_amplifiers1(self):
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        nextinput = 0
        for phase in [4,3,2,1,0]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 43210

    def test_amplifiers2(self):
        program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        nextinput = 0
        for phase in [0,1,2,3,4]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 54321

    def test_amplifiers3(self):
        program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        nextinput = 0
        for phase in [1,0,4,3,2]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 65210

    def test_amplifiers4(self):
        program = [3,8,1001,8,10,8,105,1,0,0,21,30,51,76,101,118,199,280,361,442,99999,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1002,9,3,9,1001,9,4,9,102,5,9,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,101,5,9,9,102,4,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
        nextinput = 0
        for phase in [2,2,2,2,2]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 289373649

    # def test_amplifiers_feedback1(self):
    #     program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    #     nextinput = 0
    #     terminated = False
    #     while not terminated:
    #         print(nextinput)
    #         for phase in [9,8,7,6,5]:
    #             nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
    #     assert nextinput == 139629729