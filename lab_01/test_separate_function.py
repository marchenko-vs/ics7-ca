from interpolation import *


EPS = 1e-3


def test_separate_function_1():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -0.304
    assert abs(separate_function(main_table['x'][2:4],
                                 main_table['y'][2:4]) - result) <= EPS


def test_separate_function_2():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -0.868
    assert abs(separate_function(main_table['x'][3:5],
                                 main_table['y'][3:5]) - result) <= EPS


def test_separate_function_3():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -1.296
    assert abs(separate_function(main_table['x'][4:6],
                                 main_table['y'][4:6]) - result) <= EPS


def test_separate_function_4():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -1.532
    assert abs(separate_function(main_table['x'][5:7],
                                 main_table['y'][5:7]) - result) <= EPS


def test_separate_function_5():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -1.128
    assert abs(separate_function(main_table['x'][2:5],
                                 main_table['y'][2:5]) - result) <= EPS


def test_separate_function_6():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -0.856
    assert abs(separate_function(main_table['x'][3:6],
                                 main_table['y'][3:6]) - result) <= EPS


def test_separate_function_7():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = -0.472
    assert abs(separate_function(main_table['x'][4:7],
                                 main_table['y'][4:7]) - result) <= EPS


def test_separate_function_8():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = 0.363
    assert abs(separate_function(main_table['x'][2:6],
                                 main_table['y'][2:6]) - result) <= EPS


def test_separate_function_9():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = 0.512
    assert abs(separate_function(main_table['x'][3:7],
                                 main_table['y'][3:7]) - result) <= EPS


def test_separate_function_10():
    main_table = {'x': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                  'y': [0.707, 0.924, 1.0, 0.924, 0.707, 0.383, 0.0]}
    result = 0.149
    assert abs(separate_function(main_table['x'][2:7],
                                 main_table['y'][2:7]) - result) <= EPS
