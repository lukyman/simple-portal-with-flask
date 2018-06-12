import random
import string

class RandomString:

    def generate(self, length):

        if type(length) is not int:
            return null
        characters = string.ascii_uppercase+string.digits
        code  = ''.join([random.choice(characters) for c in xrange(length)])
        return code        
