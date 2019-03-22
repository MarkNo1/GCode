from gcode import BluePrintManager
import sys
import os


if __name__ == '__main__':
    # Start the manager in the current path

    starting_path = sys.argv[1]
    print(sys.argv)
    print('Changign to ', starting_path)

    manager = BluePrintManager(starting_path)

    # Find all
    manager.find()

    # Load all
    manager.load()

    # Define Producer
    manager.define()


    # Generate all
    manager.generate()
