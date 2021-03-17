from libqtile import layout

class ThreeColumns(layout.Columns):
    defaults = [
        ("main_ratio", .5,
         "The percent of the screen-space the main window should occupy "
         "by default")
    ]

    def __init__(self, **config):
        layout.Columns.__init__(self, **config)
        self.add_defaults(ThreeColumns.defaults)
        self.num_columns = 3

    def add(self, client):
        super().add(client)

        if len(self.columns) == 3:
            main_width = 300 * self.main_size / 100
            other_width = (300 - main_width) / 2
            self.columns[0].width = other_width
            self.columns[1].width = main_width
            self.columns[2].width = other_width
            self.group.layout_all()

    def remove(self, client):
        super().remove(client)

        if 0 < len(self.columns) < 3:
            for col in self.columns:
                col.width = 100
            self.group.layout_all()

    def add_column(self, prepend=False):
        if len(self.columns) < 2:
            return super().add_column(True)

        if len(self.columns) == 2:
            return super().add_column(False)

        return super().add_column(prepend)
