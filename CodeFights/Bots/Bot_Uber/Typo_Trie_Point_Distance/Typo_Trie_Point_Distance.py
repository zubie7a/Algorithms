from collections import OrderedDict as odict
import math 

class Trie(object):
    def __init__(self):
        self.children = {}
        self.final = False
    # Regular Trie inserting operation.
    def add(self, string):
        if len(string) > 0:
            child = Trie()
            if self.children.get(string[0]) is not None:
                child = self.children[string[0]]
            child.add(string[1:])
            self.children[string[0]] = child
        else:
            self.final = True
            
    def bottom(self):
        # Generate all combinations from this node onwards.
        res = []
        if self.final == True:
            # Only final nodes will start to accumulate backwards.
            res = [""]
        for key, child in self.children.items():
            arr = child.bottom()
            arr = [key + word for word in arr]
            res.extend(arr)
        return res        
        
    def search(self, address, typo, rev):
        # Non typo is whether the typo wildcard has already
        # been used. So do recursive calls by...
        res = []
        # 1. pretending have inserted a character, so don't
        # advance the current string but label typo, have to
        # do this for every character stored at this level.
        # This extra character in the mispelled word could
        # very well be at the end of the query.
        if typo == False:
            for key, child in self.children.items():
                arr = child.search(address, True, key + rev)
                arr = [key + word for word in arr]
                res.extend(arr)
        # 2. pretending to have replaced current character.
        # so need to advance the current string and label as
        # typo. Have to do this for every character stored
        # at this level, except for the same character.
        if typo == False and len(address) > 0:
            for key, child in self.children.items():
                if key == address[0]:
                    continue
                arr = child.search(address[1:], True, key + rev)
                arr = [key + word for word in arr]
                res.extend(arr)
        # 3. pretending to have deleted a character, so
        # just advance the current char and don't add it to the
        # result.
        if typo == False and len(address) > 0:
            delStr = address[1:]
            if len(delStr) > 0 and self.children.get(delStr[0]) is not None:
                child = self.children[delStr[0]]
                arr = child.search(delStr[1:], True, delStr[0] + rev)
                arr = [delStr[0] + word for word in arr]
                res.extend(arr)
        # 4. Its the same character, so just advance the current
        # character and add it to the result, maintaining the typo
        # status passed down so far.
        if len(address) > 0:
            if self.children.get(address[0]) is not None:
                child = self.children[address[0]]
                arr = child.search(address[1:], typo, address[0] + rev)
                arr = [address[0] + word for word in arr]
                res.extend(arr)
        if len(address) == 0:
            arr = self.bottom()
            arr = [word for word in arr]
            res.extend(arr)
        return res
    
def dist(xi, yi, points):
    # Its a x,y coordinate.
    if len(points) == 2:
        xf, yf = points
        return math.sqrt((xi-xf)**2 + (yi-yf)**2)
    # Its a x1,y1,x2,y2 line segment.
    # The closest point will be defined by a formula, but
    # that may fall outside of the segment. If its outside
    # then the closest point is either segment point end.
    if len(points) == 4:
        x1, y1, x2, y2 = points
        dy, dx = y2 - y1, x2 - x1
        # The line is not vertical or horizontal.
        if dy != 0 and dx != 0:
            m = dy/dx
            # ax + by + c = 0
            # y = mx + z
            # z = y - mx
            # mx - y + z = 0
            # a = m, b = -1, z = c
            c = y1 - m*x1
            a, b = m, -1
            # Location of closest x.
            px = (b*(b*xi - a*yi) - a*c)/(a**2 + b**2)
            # Location of closest y.
            py = (a*(-b*xi + a*yi) - b*c)/(a**2 + b**2)
            # If the point found fits in the line segment.
            if x1 <= px <= x2 and y1 <= py <= y2:
                return dist(xi, yi, [px, py])
            # Closest point doesn't fit in segment, so the
            # real closest one is either of the segment edges.
            else:
                d1 = dist(xi, yi, [x1, y1])
                d2 = dist(xi, yi, [x2, y2])
                return min([d1, d2])
        # Its a horizontal line.
        elif dy == 0:
            # Closest point will be at Y difference, if X
            # fits between the segment projection.
            if x1 <= xi <= x2:
                return abs(yi - y1)
            d1 = dist(xi, yi, [x1, y1])
            d2 = dist(xi, yi, [x2, y2])
            return min([d1, d2])
        # Its a vertical line.
        elif dx == 0:
            # Closest point will be at X difference, if Y
            # fits between the segment projection.
            if y1 <= yi <= y2:
                return abs(xi - x1)
            d1 = dist(xi, yi, [x1, y1])
            d2 = dist(xi, yi, [x2, y2])  
            return min([d1, d2])

def closestLocation(address, objects, names):
    # 1. Add names to the Trie.
    t = Trie()
    
    dists = odict()
    # 1. Create an OrderedDictionary for addresses, storing them
    # as lowercase, but keeping the original, and also storing
    # their coordinates.
    for i in range(len(names)):
        original = names[i]
        lower = original.lower()
        coords = objects[i]
        dists[lower] = (coords, original)
    
    # Add all lowercase names to the Trie.
    for name in dists.keys():
        t.add(name)
    
    # 2. Search for address. This will be a query
    # where either a single character can be replaced,
    # deleted or inserted only once. It will keep track
    # of a 'typo' flag to see if we have already used
    # the potential typo in the query.
    closest = set(t.search(address.lower(), False, ""))
    minDist, minName = float('inf'), ""
    for name in closest:
        coord, original = dists[name]
        d = dist(0,0,coord)
        if d < minDist:
            minDist = d
            minName = original 
    return minName
