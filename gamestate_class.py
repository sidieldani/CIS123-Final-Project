# This class contains the information that will be saved and loaded, both locally and to GoFile through their API.
import game_text

class Game_state:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.ship = False
        self.crew_fmate = False
        self.crew_pilot = False
        self.crew_quartermaster = False
        self.crew_mechanic = False
        self.body_health = 3
        self.mind_health = 3
        self.last_location = 'game_text.a0_init_location()'

        self.save_info = f'''{self.first_name}
        {self.last_name}
        {str(self.ship)}
        {str(self.crew_fmate)}
        {str(self.crew_pilot)}
        {str(self.crew_quartermaster)}
        {str(self.crew_mechanic)}
        {str(self.body_health)}
        {str(self.mind_health)}
        {str(self.last_location)}'''        #turns all save data into a str for writing
