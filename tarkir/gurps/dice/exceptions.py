from ..exceptions import GurpsException


class DiceError(GurpsException):
    pass


class DiceParseError(DiceError, ValueError):
    pass
