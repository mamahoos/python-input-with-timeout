from sys import stdout

Self = 'typing.Self'
Any  = object()

class Endl(object):
    pass

class Cout(object):
    def __lshift__(self, other: Any) -> Self:
        stdout.write("\r\n" if isinstance(other, Endl) else str(other))
        stdout.flush()
        return self
    
cout = Cout()
endl = Endl()

# ------ #

if __name__ == "__main__":
    cout << "Hello, World!" << endl
