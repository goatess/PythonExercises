import calculator as calc
import operations.addition as add
import operations.substraction as subs
import operations.multiplication as mult
import operations.division as div
import sys
import pprint

def main():
    pprint.pprint(sys.path)   #   sys.path.append()

    op1 = add.Addition()
    print("suma:", op1.plus(2,2))
    op2 = subs.Substraction()
    print("resta:",op2.minus(5, 3))
    op3 = mult.Multiplication()
    print("multiplicación:",op3.times(4, 2))
    op4 = div.Division()
    print("división:",op4.divideBy(4, 2))
    
if __name__ == '__main__':
    main()