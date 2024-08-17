import re

from file_manager import FileManager


class PasswordValidator:
    PATTERN: str = r'(\w) (\d+)-(\d+): (\w+)'
    file_manager = FileManager()

    @staticmethod
    def _is_valid_range(min_range: int, max_range: int) -> bool:
        return max_range > min_range

    def _is_valid_password(self, line: str) -> bool:
        match = re.match(self.PATTERN, line)
        if not match:
            return False
        char, min_count, max_count, password = match.groups()

        if not self._is_valid_range(int(min_count), int(max_count)):
            return False

        count = password.count(char)
        if count < int(min_count) or count > int(max_count):
            return False

        return True

    def get_count_valid_passwords_from_file(self, file_name: str) -> int:
        line_list: list = self.file_manager.read_lines_from_file(file_name)

        valid_passwords_count = 0
        for line in line_list:
            if self._is_valid_password(line.strip()):
                valid_passwords_count += 1

        return valid_passwords_count


if __name__ == "__main__":
    print(PasswordValidator().get_count_valid_passwords_from_file('test.txt'))
