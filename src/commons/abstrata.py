from abc ABC,

class Abstrata(ABC):
    def __init__(self, fr_path_al, fr_path_disc, to_path):
        self.fr_path_al = fr_path_al
        self.fr_path_disc = fr_path_disc
        self.to_path = to_path

    @abstractmethod # não vai implementar esse método, vai ser implementado por quem herdar esse método.
    def processa():
        return 1
