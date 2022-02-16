def banner(start, end) :
      return lambda msg: print("%s %s %s" % (start, msg, end))


bannerMsg = banner("[---", "---]")
altMsg = banner("***", "!!!!")

bannerMsg("Hello")
bannerMsg("World")
altMsg("Alt  message")
