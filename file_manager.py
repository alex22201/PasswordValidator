import os


class FileManager:

    @staticmethod
    def _validate_file(file_name: str) -> str:
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"File {file_name} not found")
        elif os.path.getsize(file_name) == 0:
            raise ValueError(f"File {file_name} is empty")
        return file_name

    def read_lines_from_file(self, file_name: str) -> list:
        validate_file = self._validate_file(file_name)
        with open(validate_file) as f:
            return [line.strip() for line in f]
