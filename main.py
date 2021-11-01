import PySide6
from PySide6 import QtGui
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
from random import randrange
import random

from ui.f1randomizer_ui import Ui_MainWindow
# Import Qt-Material
import qt_material

tracks = {"Australia": "Albert Park Circuit",
          "Bahrain": "Bahrain International Circuit",
          "Vietnam": "Hanoi Street Circuit",
          "China": "Shanghai International Circuit",
          "Neatherlands": "Circuit Park Zandvoort",
          "Spain": "Circuit de Barcelona-Catalunya",
          "Monaco": "Circuit de Monaco",
          "Azerbaijan": "Baku City Circuit",
          "Canada": "Circuit Gilles-Villeneuve",
          "France": "Circuit Paul Ricard",
          "Austria": "Red Bull Ring",
          "Britain": "Silverstone Circuit",
          "Hungary": "Hungaroring",
          "Belgium": "Circuit de Spa-Francorchamps",
          "Italy": "Autodromo Nazionale Monza",
          "Singapore": "Marina Bay Street Circuit",
          "Russia": "Sochi Autodrom",
          "Japan": "Suzuka International Racing Course",
          "USA": "Circuit of the Americas",
          "Mexico": "Autódromo Hermanos Rodríguez",
          "Brazil": "Autódromo José Carlos Pace",
          "Abu Dhabi": "Yas Marina Circuit"
          }


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        qt_material.apply_stylesheet(app, theme="dark_red.xml")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("images/formula-1-logo.png"))
        self.setWindowTitle("F1-Randomizer")

        # Minimize window
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())

        # Close window
        self.ui.close_button.clicked.connect(lambda: self.close())

        # Function to move the window, because the window is borderless
        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow

        self.ui.generate_button.clicked.connect(lambda: self.generate())

    def generate(self):
        global tracks

        self.clear_result_widget()

        race_counter = self.ui.spinBox.value()
        row_counter = self.ui.track_widget.rowCount()
        column_counter = self.ui.track_widget.columnCount()
        track_list = list(tracks.keys())
        selected_tracks = []
        result_tracks = []

        for row in range(row_counter):
            if self.ui.track_widget.item(row, 0).checkState() == PySide6.QtCore.Qt.CheckState.Checked:
                selected_tracks.append(self.ui.track_widget.item(row, 1).text())

        if self.ui.multiple_tracks.checkState() != PySide6.QtCore.Qt.CheckState.Checked:

            if race_counter >= len(selected_tracks):

                # Random select from pre-selected tracks
                # Also remove pre-selected tracks from list
                while len(selected_tracks) > 0:
                    random_track = selected_tracks[randrange(len(selected_tracks))]
                    result_tracks.append(random_track)
                    selected_tracks.remove(random_track)
                    track_list.remove(random_track)

                # Calculate remaining
                remaining_value = race_counter - len(result_tracks)

                if remaining_value > len(track_list):
                    remaining_value = len(track_list)

                for value in range(remaining_value):
                    random_track = track_list[randrange(len(track_list))]
                    track_list.remove(random_track)
                    result_tracks.append(random_track)

                self.add_tracks(result_tracks)

            else:
                random.shuffle(selected_tracks)

                for value in range(race_counter):
                    result_tracks.append(selected_tracks[value])

                self.add_tracks(result_tracks)

        else:
            if race_counter > 22:

                while len(selected_tracks) > 0:
                    random_track = selected_tracks[randrange(len(selected_tracks))]
                    result_tracks.append(random_track)
                    selected_tracks.remove(random_track)

                for value in range(race_counter - len(result_tracks)):
                    result_tracks.append(track_list[randrange(len(track_list))])
                self.add_tracks(result_tracks)

            else:

                if race_counter >= len(selected_tracks):

                    # Random select from pre-selected tracks
                    # Also remove pre-selected tracks from list
                    while len(selected_tracks) > 0:
                        random_track = selected_tracks[randrange(len(selected_tracks))]
                        result_tracks.append(random_track)
                        selected_tracks.remove(random_track)

                    # Calculate remaining
                    remaining_value = race_counter - len(result_tracks)

                    for value in range(remaining_value):
                        random_track = track_list[randrange(len(track_list))]
                        track_list.remove(random_track)
                        result_tracks.append(random_track)

                    self.add_tracks(result_tracks)

                else:
                    random.shuffle(selected_tracks)

                    for value in range(race_counter):
                        result_tracks.append(selected_tracks[value])

                    self.add_tracks(result_tracks)

        # self.reset_track_list()

    def reset_track_list(self):

        row_counter = self.ui.track_widget.rowCount()

        for row in range(row_counter):
            if self.ui.track_widget.item(row, 0).checkState() == PySide6.QtCore.Qt.CheckState.Checked:
                self.ui.track_widget.item(row, 0).setCheckState(PySide6.QtCore.Qt.CheckState.Unchecked)

    def add_tracks(self, result_tracks):
        global tracks
        random.shuffle(result_tracks)
        for track in result_tracks:
            row_position = self.ui.result_table_widget.rowCount()
            self.ui.result_table_widget.insertRow(row_position)

            self.create_table_widget(row_position, 0, track, "result_table_widget")
            self.create_table_widget(row_position, 1, tracks.get(track), "result_table_widget")


    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()

        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtablewidgetitem.setText(text)

    def clear_result_widget(self):
        if self.ui.result_table_widget.rowCount() > 0:
            while self.ui.result_table_widget.rowCount() > 0:
                self.ui.result_table_widget.removeRow(0)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
