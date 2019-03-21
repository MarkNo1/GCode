from gcode import BluePrintManager


if __name__ == '__main__':
    # Start the manager in the current path
    manager = BluePrintManager()

    # Find all
    manager.find()


    # Load all
    manager.load()


    # Define Producer
    manager.define()


    # Generate all
    manager.generate()
