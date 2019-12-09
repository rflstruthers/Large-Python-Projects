class Organism():
    spec = 'Homosapien'
    comp = 'Carbon-based'
    leg = 2
    arm = 2
    
    def attributes(self):
        msg = ''
        msg += ("Species:\t{}".format(Organism.spec))
        msg += ("\nComposition:\t{}".format(Organism.comp))
        msg += ("\nAppendages:\t{} legs, {} arms".format(Organism.leg,Organism.arm))
        return msg

human = Organism()
print(human.attributes())
