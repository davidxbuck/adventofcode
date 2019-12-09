# pytest tests

from Advent2019_Intcode import Intcode


class TestIntcode():
    def test_instantiate(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        assert code.program[:-1000] == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_instantiate_noun_and_verb(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 33, 66)
        assert code.program[:-1000] == [1, 33, 66, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 0
        assert not code.terminated

    def test_cmd01_position(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert code.program[:-1000] == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [101, 9, 10, 49, 2, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [1001, 9, 10, 40, 2, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [1101, 9, 10, 19, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd01_relative11(self):
        code = Intcode([201, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.relative_base = 1
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd01()
        assert code.parm1
        assert not code.parm2
        assert not code.parm3
        assert code.program[:-1000] == [201, 9, 10, 80, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd02_position(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 4
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd02()
        assert code.program[:-1000] == [150, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [250, 9, 10, 3, 102, 5, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [132, 9, 10, 12, 1002, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [33, 9, 10, 12, 1102, 3, 11, 0, 99, 30, 40, 50]
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
        assert code.program[:-1000] == [3, 2, 5, 12, 1102, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 2
        assert not code.terminated

    def test_cmd05_position_jump_if_true_true(self):
        code = Intcode([5, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd05()
        assert code.program[:-1000] == [5, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 40
        assert not code.terminated

    def test_cmd05_position_jump_if_true_false(self):
        code = Intcode([5, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd05()
        assert code.program[:-1000] == [5, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 3
        assert not code.terminated

    def test_cmd06_position_jump_if_false_true(self):
        code = Intcode([6, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd06()
        assert code.program[:-1000] == [6, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 3
        assert not code.terminated

    def test_cmd06_position_jump_if_false_false(self):
        code = Intcode([6, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd06()
        assert code.program[:-1000] == [6, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 40
        assert not code.terminated

    def test_cmd07_less_than_true(self):
        code = Intcode([7, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd07()
        assert code.program[:-1000] == [7, 7, 10, 1, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd07_less_than_false(self):
        code = Intcode([7, 10, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd07()
        assert code.program[:-1000] == [7, 10, 10, 0, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd08_equals_true(self):
        code = Intcode([7, 7, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd08()
        assert code.program[:-1000] == [7, 7, 10, 0, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd08_equals_false(self):
        code = Intcode([7, 10, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        code.pointer = 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd08()
        assert code.program[:-1000] == [7, 10, 10, 1, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 4
        assert not code.terminated

    def test_cmd09_positional(self):
        code = Intcode([9, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50])
        assert code.relative_base == 0
        assert code.pointer == 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd09()
        assert code.program[:-1000] == [9, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50]
        assert code.pointer == 2
        assert code.relative_base == 13
        assert not code.terminated

    def test_cmd09_immediate(self):
        code = Intcode([109, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50])
        assert code.relative_base == 0
        assert code.pointer == 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd09()
        assert code.program[:-1000] == [109, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50]
        assert code.pointer == 2
        assert code.relative_base == 7
        assert not code.terminated

    def test_cmd09_relative(self):
        code = Intcode([209, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50])
        code.relative_base = 1
        assert code.pointer == 0
        operation = f'{code.program[code.pointer]:>05}'
        code.parm3, code.parm2, code.parm1 = map(int, tuple(operation[0:3]))
        code.cmd09()
        assert code.program[:-1000] == [209, 7, 10, 3, 2, 3, 11, 13, 99, 30, 40, 50]
        assert code.pointer == 2
        assert code.relative_base == 100
        assert not code.terminated

    def test_cmd99(self):
        code = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10)
        code.pointer = 8
        code.cmd99()
        assert code.program[:-1000] == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        assert code.pointer == 8
        assert code.terminated

    def test_prog_1(self):
        code = Intcode([1, 0, 0, 0, 99])
        result = code.run()
        assert result == (2, True)
        assert code.program[:-1000] == [2, 0, 0, 0, 99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_2(self):
        code = Intcode([2, 3, 0, 3, 99], 3)
        result = code.run()
        assert result == (2, True)
        assert code.program[:-1000] == [2, 3, 0, 6, 99]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_3(self):
        code = Intcode([2, 4, 4, 5, 99, 0], 4, 4)
        result = code.run()
        assert result == (2, True)
        assert code.program[:-1000] == [2, 4, 4, 5, 99, 9801]
        assert code.pointer == 4
        assert code.terminated

    def test_prog_4(self):
        code = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99], 1, 1)
        result = code.run()
        assert result == (30, True)
        assert code.program[:-1000] == [30, 1, 1, 4, 2, 5, 6, 0, 99]
        assert code.pointer == 8
        assert code.terminated

    def test_amplifiers1(self):
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        nextinput = 0
        for phase in [4, 3, 2, 1, 0]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 43210

    def test_amplifiers2(self):
        program = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
        nextinput = 0
        for phase in [0, 1, 2, 3, 4]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 54321

    def test_amplifiers3(self):
        program = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1,
                   32, 31, 31, 4, 31, 99, 0, 0, 0]
        nextinput = 0
        for phase in [1, 0, 4, 3, 2]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 65210

    def test_amplifiers4(self):
        program = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 30, 51, 76, 101, 118, 199, 280, 361, 442, 99999, 3, 9, 102,
                   5, 9, 9, 4, 9, 99, 3, 9, 102, 4, 9, 9, 1001, 9, 3, 9, 102, 2, 9, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9,
                   1002, 9, 3, 9, 1001, 9, 4, 9, 102, 5, 9, 9, 101, 3, 9, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 101, 5, 9,
                   9, 102, 4, 9, 9, 1001, 9, 3, 9, 1002, 9, 2, 9, 101, 4, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 1001, 9,
                   3, 9, 102, 5, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2,
                   9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002,
                   9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3,
                   9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4,
                   9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9,
                   4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001,
                   9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
                   1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9,
                   3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2,
                   9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101,
                   2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99,
                   3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4,
                   9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9,
                   4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99]
        nextinput = 0
        for phase in [2, 2, 2, 2, 2]:
            nextinput, terminated = Intcode(program, inp=[phase, nextinput], mode='run').run()
        assert nextinput == 289373649

    def test_relative_mode1(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        code = Intcode(program[:], mode='test')
        assert code.run() == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]

    def test_relative_mode3(self):
        program = [104, 1125899906842624, 99]
        code = Intcode(program[:], mode='run')
        assert code.run()[0] == 1125899906842624
