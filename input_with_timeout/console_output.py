from sys.stdout import write, flush

Self = 'typing.Self'
Any  = object()

class Endl(object):
    pass

class Cout(object):
    def __lshift__(self, other: Any) -> Self:
        write("\r\n" if isinstance(other, Endl) else str(other))
        flush()
        return self
    
cout = Cout()
endl = Endl()

# ------ #

if __name__ == "__main__":
    cout << "Hello, World!" << endl
