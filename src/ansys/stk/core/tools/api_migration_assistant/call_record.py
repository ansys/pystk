"""Information for a specific call captured while recording."""


class CallRecord:
    """Capture the information for a specific call."""

    def __init__(
        self,
        filename,
        type_name,
        member_name,
        lineno,
        end_lineno,
        col_offset,
        end_col_offset,
    ):
        """Construct a new CallRecord."""
        self.filename = filename
        self.type_name = type_name
        self.member_name = member_name
        self.lineno = lineno
        self.end_lineno = end_lineno
        self.col_offset = col_offset
        self.end_col_offset = end_col_offset

    def __eq__(self, other):
        """Compare this object with another object for equality."""
        if isinstance(other, CallRecord):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        """Return the hash value for the object."""
        return hash(
            (
                self.filename,
                self.type_name,
                self.member_name,
                self.lineno,
                self.end_lineno,
                self.col_offset,
                self.end_col_offset,
            )
        )

    def __lt__(self, other):
        """Define the behavior of the less-than operator (<) for this class."""
        if isinstance(other, CallRecord):
            return (
                self.filename,
                self.lineno,
                self.col_offset,
                self.end_lineno,
                self.end_col_offset,
            ).__lt__(
                (
                    other.filename,
                    other.lineno,
                    other.col_offset,
                    other.end_lineno,
                    other.end_col_offset,
                )
            )
        return NotImplemented
