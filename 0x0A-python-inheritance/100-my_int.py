#!/usr/bin/python3

class MyInt(int):
    # Overrides == operator
    def __eq__(self, other):
        return not super().__eq__(other)
        
    # Overrides != operator
    def __ne__(self, other):
        return not super().__ne__(other)
