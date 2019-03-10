from gcode.blueprints.Manager import BluePrintManager


if __name__ == '__main__':
    # Start the manager in the current path
    bluem = BluePrintManager()

    # Find all
    bluem.find()

    # Load all
    bluem.load()

    # Show BluePrints
    bluem.show()

    # Generate all
    bluem.produce()
