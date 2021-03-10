import sys
 
# total arguments
checkout =  sys.argv[1]
git reset --hard checkout
print("Total arguments passed:", checkout)
