from gcode import BluePrintManager
from gcode.primitive import pwd
import sys


if __name__ == '__main__':
    # Start the manager in the current path
    if len(sys.argv) > 1:
        starting_path = sys.argv[1]
    else:
        starting_path = pwd()

    manager = BluePrintManager('0-5', starting_path)

    # Find all
    manager.find()

    # Load all
    manager.load()

    # Define Producer
    manager.define()


    # Generate all
    manager.generate()
