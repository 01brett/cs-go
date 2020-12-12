"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# `with` is Python's context manager that handles teardown for us
with open("foo.txt") as f:
    print(f.read())

#
# Alternative way to read but docs don't recommend
#
# f = open('foo.txt')
# print(f.read())
# f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# non-context manager style -> note the need to close()
# b = open("bar.txt", "w")
# b.write("This is not much\nThough, I cannot complain\nKeep me in your prayers")
# b.close()

# `with` context manager
with open("bar.txt", "w") as b:
    b.write("This is not much\nThough, I cannot complain\nKeep me in your prayers")
