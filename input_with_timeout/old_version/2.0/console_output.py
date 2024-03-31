try:
    Self = __import__('typing').Self
except ImportError:
    Self = "typing.Self"
finally:
    import sys
    Any  = __import__('typing').Any


class Endl(object):
    pass

class Cout(object):
    def __lshift__(self, other: Any) -> Self:
        sys.stdout.write("\r\n" if isinstance(other, Endl) else str(other))
        sys.stdout.flush()
        return self
    
cout = Cout()
endl = Endl()

# ------ #

if __name__ == "__main__":
    cout << "Hello, World!" << endl
