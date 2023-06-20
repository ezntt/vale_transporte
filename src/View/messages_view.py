class ViewMessages:

    def print_data(self, message):
        print(message)

    def print_list(self, rows):
        for i, row in enumerate(rows):
            print(f"{i + 1}. {row}")
