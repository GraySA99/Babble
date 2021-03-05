
import sys
from program import Program

if __name__ == '__main__':
    
    try:
        print(sys.argv[1])
    except IndexError:
        print('Please enter a Babble file')
        sys.exit(-1)
    
    program = Program(sys.argv[1])
    program.run()