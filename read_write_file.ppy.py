class ManagedFile:
    def __init__(self, filename):
        print('initiating', filename)
        self.filename = filename

    def __enter__(self):
        print('entering ', self.filename)
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True


# No exception
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

print()

# Exception is raised, but the file can still be closed
with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')