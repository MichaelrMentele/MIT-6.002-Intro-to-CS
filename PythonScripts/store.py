class Store:
  open = 5
  close = 3
  
  def hours(self):
    import string  
    return "We're open from " + self.format(open) + "to " + self.format(close)