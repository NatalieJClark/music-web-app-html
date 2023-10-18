class AlbumParametersValidator():
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def is_valid(self):
        return self.is_title_valid() and self.is_release_year_valid()
    
    def is_title_valid(self):
        if self.title is None or self.title == "":
            return False
        return True

    def is_release_year_valid(self):
        try:
            int(self.release_year)
            return True
        except:
            return False

    def generate_errors(self):
        errors = []
        if not self.is_title_valid():
            errors.append("Title can't be blank")
        if not self.is_release_year_valid():
            errors.append("Release Year can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)