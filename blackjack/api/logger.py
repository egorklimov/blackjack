import abc


class Logger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info(self) -> None:
        pass

    @abc.abstractmethod
    def debug(self) -> None:
        pass

    @abc.abstractmethod
    def error(self) -> None:
        pass
