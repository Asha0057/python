class Animal:
    x=0
    def party(self):
        self.x=self.x+1
        print("so far",self.x)
an=Animal()
print(type(an))
print(dir(an))#returns list of attributes and methods associated with object
print(type(an.x))
print(type(an.party))
