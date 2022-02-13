def get_txt (file_path):
        with open(file_path, 'r') as txtf:
            text = txtf.read().replace("\n", " ")
            return text
