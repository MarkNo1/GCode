from gcode import BluePrintManager


if __name__ == '__main__':
    # Start the manager in the current path
    manager = BluePrintManager()

    # Find all
    manager.find()

    # Load all
    manager.load()

    # Show BluePrints
    #manager.show()

    # Generate all
    manager.produce()
