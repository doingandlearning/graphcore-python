def banner(start, end) :
      return lambda msg: print("%s %s %s" % (start, msg, end))


bannerMsg = banner("[---", "---]")

bannerMsg("Hello")
bannerMsg("World")
