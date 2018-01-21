#https://leetcode.com/submissions/detail/116935014/ 
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}        
        self.lru = {}
        self.count = 0
        
    def _lru(self):
        minor =  sys.maxint
        lru_key = -1
        for k,v in self.lru.iteritems():            
            if v < minor:
                minor =  v
                lru_key = k
        return lru_key
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        founded = self.cache.get(key, -1)            
        if founded > -1:
            self.count += 1
            self.lru[key] = self.count
        
        return founded
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """        
        #just adjust if is not an update
        if self.cache.get(key, -1) == -1 and len(self.cache) == self.capacity:
            lru_key = self._lru()
            self.cache.pop(lru_key, 0)
            self.lru.pop(lru_key, 0)
                
        self.cache[key] = value
        self.count += 1
        self.lru[key] = self.count 
           
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)