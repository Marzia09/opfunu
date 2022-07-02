#!/usr/bin/env python
# Created by "Thieu" at 11:16, 02/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import opfunu
import numpy as np

## Test CEC2010 F1
print("====================F1")
problem = opfunu.cec_based.F12010(ndim=100)
x = np.ones(100)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F2
print("====================F2")
problem = opfunu.cec_based.F22010(ndim=100)
x = np.ones(100)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F3
print("====================F3")
problem = opfunu.cec_based.F32010(ndim=100)
x = np.ones(100)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F4
print("====================F4")
problem = opfunu.cec_based.F42010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F5
print("====================F5")
problem = opfunu.cec_based.F52010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F6
print("====================F6")
problem = opfunu.cec_based.F62010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F7
print("====================F7")
problem = opfunu.cec_based.F72010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F8
print("====================F8")
problem = opfunu.cec_based.F82010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F9
print("====================F9")
problem = opfunu.cec_based.F92010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F10
print("====================F10")
problem = opfunu.cec_based.F102010(ndim=105)
x = np.ones(105)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F11
print("====================F11")
problem = opfunu.cec_based.F112010(ndim=120)
x = np.ones(120)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F12
print("====================F12")
problem = opfunu.cec_based.F122010(ndim=125)
x = np.ones(125)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2010 F13
print("====================F13")
problem = opfunu.cec_based.F132010(ndim=125)
x = np.ones(125)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


















