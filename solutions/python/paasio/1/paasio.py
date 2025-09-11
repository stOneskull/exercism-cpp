import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.opers_read = self.opers_write = 0
        self.bytes_read = self.bytes_write = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        line = super().readline()
        if not line:
            raise StopIteration
        self.opers_read += 1
        self.bytes_read += len(line)
        return line

    def read(self, size=-1):
        bytes_read = super().read(size)
        self.opers_read += 1
        self.bytes_read += len(bytes_read)
        return bytes_read

    @property
    def read_bytes(self):
        return self.bytes_read

    @property
    def read_ops(self):
        return self.opers_read

    def write(self, b):
        bytes_write = super().write(b)
        self.bytes_write += bytes_write
        self.opers_write += 1
        return bytes_write

    @property
    def write_bytes(self):
        return self.bytes_write

    @property
    def write_ops(self):
        return self.opers_write


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.socket = socket
        self.opers_read = self.opers_write = 0
        self.bytes_read = self.bytes_write = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        packet = self.socket.recv(bufsize, flags)
        self.opers_read += 1
        self.bytes_read += len(packet)
        return packet

    @property
    def recv_bytes(self):
        return self.bytes_read

    @property
    def recv_ops(self):
        return self.opers_read

    def send(self, data, flags=0):
        bytes_write = self.socket.send(data, flags)
        self.opers_write += 1
        self.bytes_write += bytes_write
        return bytes_write

    @property
    def send_bytes(self):
        return self.bytes_write

    @property
    def send_ops(self):
        return self.opers_write
