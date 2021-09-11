import random
import uuid

class ObfuscateProtect:
    """
    Main class used to obfuscate strings to protect researchers and other users to reading sensitive or unpleasant
    strings, but also allowing for an easy API to still view unique text.
    """

    # Two modes are currently supported, UUID and Color/ Word Strings
    _modes = {
        1: "uuid",
        2: "color/ word string"
    }

    # A dictionary that holds all of the strings that have been obfuscated so far
    _dict_of_used_strings = {}

    # The default mode used, set in the constructor.
    _default_mode = None

    def __init__(self, default_mode=1):
        """
        The constructor. Sets the default mode.
        """
        self._default_mode = default_mode

    def obfuscate(self, text, mode=1, verbose=False, should_lower = True):
        """
        The main obfuscator class. Takes the text to be obfuscated and an optional mode and if a log statement should
        be printed on the obfuscation process.
        """

        obfuscated_text = None

        # Check if a valid mode has been selected
        if mode not in self._modes.keys():
            raise Exception("Invalid mode: '{}' was provided. Valid modes: {}".format(mode, self._modes))

        # An optional flag witch by default makes all text lower case
        if should_lower == True:
            text = text.lower()

        # Choose the appropriate obfuscation technique for the mode
        if mode == 1:
            obfuscated_text = self._get_uuid(text)
        elif mode == 2:
            obfuscated_text = self._get_color_word_string(text)

        # If verbose has been set then print information on the obfuscation
        if verbose == True:

            if text in self._dict_of_used_strings.keys():
                print("Plain text '{}' existed previously. Using old value '{}'.".format(text, obfuscated_text))
            else:
                print("Plain text '{}' obfuscated to '{}', using mode '{}'.".format(text, obfuscated_text,
                                                                                    self._modes[mode]))

    def _get_color_word_string(self, text):
        """
        This function is used to retrieve a color/ word string based on the text.
        """

        if text in self._dict_of_used_strings.keys():
            # text already in dictionary
            obfuscated_text = self._dict_of_used_strings[text]
        else:
            color_choice = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Pink", "Maroon", "Purple",
                            "Teal"]
            word_choice = ["WARLORD", "CHAIR", "CUP", "FLOWER", "MAN", "CAT", "DOG", "man", "mountain", "state",
                           "ocean",
                           "country", "building", "cat", "airline", "house", "ocean", "Uncle", "bird", "photograph",
                           "banana",
                           "eyes", "light", "sun", "suitcase", "bed", "cat", "movie", "train", "country", "book",
                           "phone",
                           "match", "speaker", "clock", "pen", "violin", 'Adult', 'Aeroplane', 'Air',
                           'Aircraft-Carrier',
                           'Airforce', 'Airport', 'Album', 'Alphabet', 'Apple', 'Arm', 'Army', 'Baby', 'Baby',
                           'Backpack',
                           'Balloon', 'Banana', 'Bank', 'Barbecue', 'Bathroom', 'Bathtub', 'Bed', 'Bed', 'Bee', 'Bible',
                           'Bible', 'Bird', 'Bomb', 'Book', 'Boss', 'Bottle', 'Bowl', 'Box', 'Boy', 'Brain', 'Bridge',
                           'Butterfly', 'Button', 'Cappuccino', 'Car', 'Car-race', 'Carpet', 'Carrot', 'Cave', 'Chair',
                           'Chess-Board', 'Chief', 'Child', 'Chisel', 'Chocolates', 'Church', 'Church', 'Circle',
                           'Circus',
                           'Circus', 'Clock', 'Clown', 'Coffee', 'Coffee-shop', 'Comet', 'Compact Disc', 'Compass',
                           'Computer',
                           'Crystal', 'Cup', 'Cycle', 'Data', 'Base', 'Desk', 'Diamond', 'Dress', 'Drill', 'Drink',
                           'Drum',
                           'Dung', 'Ears', 'Earth', 'Egg', 'Electricity', 'Elephant', 'Eraser', 'Explosive', 'Eyes',
                           'Family',
                           'Fan', 'Feather', 'Festival', 'Film', 'Finger', 'Fire', 'Floodlight', 'Flower', 'Foot',
                           'Fork',
                           'Freeway', 'Fruit', 'Fungus', 'Game', 'Garden', 'Gas', 'Gate', 'Gemstone', 'Girl', 'Gloves',
                           'God',
                           'Grapes', 'Guitar', 'Hammer', 'Hat', 'Hieroglyph', 'Highway', 'Horoscope', 'Horse', 'Hose',
                           'Ice',
                           'Ice-cream', 'Insect', 'Jet-fighter', 'Junk', 'Kaleidoscope', 'Kitchen', 'Knife',
                           'Leather-jacket',
                           'Leg', 'Library', 'Liquid', 'Magnet', 'Man', 'Map', 'Maze', 'Meat', 'Meteor', 'Microscope',
                           'Milk',
                           'Milkshake', 'Mist', 'Money', 'Monster', 'Mosquito', 'Mouth', 'Nail', 'Navy', 'Necklace',
                           'Needle', 'Onion', 'PaintBrush', 'Pants', 'Parachute', 'Passport', 'Pebble', 'Pendulum',
                           'Pepper',
                           'Perfume', 'Pillow', 'Plane', 'Planet', 'Pocket', 'Post-office', 'Potato', 'Printer',
                           'Prison',
                           'Pyramid', 'Radar', 'Rainbow', 'Record', 'Restaurant', 'Rifle', 'Ring', 'Robot', 'Rock',
                           'Rocket',
                           'Roof', 'Room', 'Rope', 'Saddle', 'Salt', 'Sandpaper', 'Sandwich', 'Satellite', 'School',
                           'Sex',
                           'Ship', 'Shoes', 'Shop', 'Shower', 'Signature', 'Skeleton', 'Slave', 'Snail', 'Software',
                           'Solid',
                           'Space-Shuttle', 'Spectrum', 'Sphere', 'Spice', 'Spiral', 'Spoon', 'Sports-car',
                           'Spot-Light',
                           'Square', 'Staircase', 'Star', 'Stomach', 'Sun', 'Sunglasses', 'Surveyor', 'Swimming-Pool',
                           'Sword',
                           'Table', 'Tapestry', 'Teeth', 'Telescope', 'Television', 'Tennis racquet', 'Thermometer',
                           'Tiger',
                           'Toilet', 'Tongue', 'Torch', 'Torpedo', 'Train', 'Treadmill', 'Triangle', 'Tunnel',
                           'Typewriter',
                           'Umbrella', 'Vacuum', 'Vampire', 'Videotape', 'Vulture', 'Water', 'Weapon', 'Web',
                           'Wheelchair',
                           'Window', 'Woman', 'Worm', 'X-ray']

            word = word_choice[random.randint(0, len(word_choice) - 1)]
            color = color_choice[random.randint(0, len(color_choice) - 1)]
            word = word.replace("-", "")

            obfuscated_text = "{}-{}".format(color, word).upper()

            # Checks for text collisons
            while obfuscated_text in self._dict_of_used_strings.values():
                word = word_choice[random.randint(0, len(word_choice) - 1)]
                color = color_choice[random.randint(0, len(color_choice) - 1)]
                word = word.replace("-", "")

                obfuscated_text = "{}-{}".format(color, word).upper()

        # Add new text to dictionary
        self._dict_of_used_strings[text] = obfuscated_text
        return obfuscated_text

    def _get_uuid(self, text):
        """
        This function retrieves a unique UUID for a given piece of text.
        """

        if text in self._dict_of_used_strings.keys():
            # text already in dictionary
            obfuscated_text = self._dict_of_used_strings[text]
        else:
            # make new UUID
            obfuscated_text = uuid.uuid4().hex
            # stops uuid collisions
            while obfuscated_text in self._dict_of_used_strings.values():
                obfuscated_text = uuid.uuid4().hex

            # Add new text to dictionary
            self._dict_of_used_strings[text] = obfuscated_text

        return obfuscated_text
