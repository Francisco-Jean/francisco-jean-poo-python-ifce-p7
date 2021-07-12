class Cliente:
    def __init__(self, id1, nome, codigo, cnpjcpf, tipo):
        self._id = id1
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo, self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string

    def get_usuarioID(self):
        return self._id

    def get_tipoUsuario(self):
        return self._tipo

    def get_usuarioCodigo(self):
        return self._codigo

    def get_nomeUsuario(self):
        return self._nome

    def get_cnpfcpfUsuario(self):
        return self._cnpjcpf

    def set_nomeUsuario(self, nome):
        self._nome = nome

    def set_cnpjcpfUsuario(self, cnpjcpf):
        self._cnpjcpf = cnpjcpf
