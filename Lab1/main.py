import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import GUI
import os, stat, shutil


class Driver(QMainWindow, GUI):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.base(self)
        self.button_command()


    def button_command(self):
        self.start_but.clicked.connect(self.start)
        self.finish_but.clicked.connect(self.finish)
        self.pwd_but.clicked.connect(self.pwd)
        self.cd_but.clicked.connect(self.cd)
        self.ls_but.clicked.connect(self.ls)
        self.mkdir_but.clicked.connect(self.mkdir)
        self.rmdir_but.clicked.connect(self.rmdir)
        self.vi_but.clicked.connect(self.vi)
        self.rmfile_but.clicked.connect(self.rmfile)


    def new_path(self):
        global path_list, dirs, files, indx, directories, start_work_directory, len_work_path
        path_list, dirs, files, indx = [], [], [], 0
        len_work_path = len(first_work_path)

        for path, directory, file in os.walk(top=f"{first_work_path}/{start_work_directory}"):

            path_list.append(path)
            dirs.append(directory)
            files.append(file)
        print("New PATH created!")


    start_indx = 0


    def start(self):
        global directories, all_directory, work_directory, last_work_directory, first_work_path
        work_directory = "Dir0/"
        last_work_directory = r"Dir1/Dir2/Dir3/Dir4"

        directories = work_directory + last_work_directory
        if Driver.start_indx == 0:
            all_directory = os.getcwd()

        first_work_path = all_directory.replace(last_work_directory, '')
        print(first_work_path)
        try:
            os.makedirs(directories)
        except FileExistsError:
            pass


        for i in range(5):
            file = open(f"Dir{i}/dir{i}.txt", "w+")
            os.chdir(f"Dir{i}")
            file.write(f"Directory{i}")
            file.close()
        os.chmod(first_work_path ,stat.S_IRWXU)
        Driver.new_path(self)
        Driver.start_indx += 1


    def finish(self):
        global work_directory
        try:
            shutil.rmtree(path_list[indx][:len_work_path + 1] + work_directory)
        except FileNotFoundError:
            sys.exit()
        sys.exit()


    def pwd(self):
        global path_list, indx
        print("Lenght of firt working directory: ", len_work_path)

        if self.blocker.isChecked():
            self.pwd_entry.clear()
            self.pwd_entry.setText("Permission denied!")
        else:
            self.pwd_entry.clear()
            self.pwd_entry.setText(path_list[indx][len_work_path + 1::])


    def ls(self):
        global dirs, files, indx

        if self.blocker.isChecked():
            self.ls_entry.clear()
            self.ls_entry.setText("Permission denied!")
        else:
            self.ls_entry.clear()
            self.ls_entry.setText(f"{dirs[indx]} {files[indx]}")


    def cd(self):
        global indx, path_list

        if self.blocker.isChecked():
            self.cd_entry.clear()
            self.cd_entry.setText("Permission denied!")
        else:
            txt = path_list[indx][:len_work_path + 1] + self.cd_entry.text()
            if txt in path_list:
                os.chdir(txt)
                self.cd_entry.setText("Ready!")
                indx = path_list.index(txt)
            else:
                self.cd_entry.setText("PATH error!")


    def mkdir(self):
        global path_list
        mkdir_txt = path_list[indx][:len_work_path + 1] + self.mkdir_entry.text()

        if self.rooter.isChecked():
            if mkdir_txt not in path_list:
                os.mkdir(mkdir_txt)
                self.mkdir_entry.clear()
                self.mkdir_entry.setText("Ready!")
                Driver.new_path(self)

            else:
                self.mkdir_entry.clear()
                self.mkdir_entry.setText("PATH error!")

        else:
            self.mkdir_entry.clear()
            self.mkdir_entry.setText("Permission denied!")


    def rmfile(self):
        global files, indx
        rmfile_txt = path_list[indx][:len_work_path + 1] + self.rmfile_entry.text()

        if self.rooter.isChecked():
            if rmfile_txt.split("/")[-1] in files[indx]:
                os.remove(rmfile_txt)
                self.rmfile_entry.clear()
                self.rmfile_entry.setText("Ready!")
                Driver.new_path(self)

            else:
                self.rmfile_entry.clear()
                self.rmfile_entry.setText("PATH error!")
                print(rmfile_txt.split("/")[-1])
                print(files)

        else:
            self.rmfile_entry.clear()
            self.rmfile_entry.setText("Permission denied!")


    def rmdir(self):
        global path_list
        rmdir_txt = path_list[indx][:len_work_path + 1] + self.rmdir_entry.text()

        if self.rooter.isChecked():
            if rmdir_txt in path_list:
                shutil.rmtree(rmdir_txt)
                self.rmdir_entry.clear()
                self.rmdir_entry.setText("Ready!")
                Driver.new_path(self)

            else:
                self.rmdir_entry.clear()
                self.rmdir_entry.setText("PATH error!")

        else:
            self.rmdir_entry.clear()
            self.rmdir_entry.setText("Permission denied!")


    def vi(self):
        global path_list, files, indx
        name = path_list[indx][:len_work_path + 1] + self.vi_entry.text()
        content = self.vi_txt_entry.toPlainText()

        if self.rooter.isChecked():
            if name not in files[indx]:
                os.chdir(path_list[indx])
                with open(name, 'x') as f:
                    f.write(content)
                self.vi_entry.clear()
                self.vi_entry.setText("Ready!")
                self.vi_txt_entry.clear()
                self.vi_txt_entry.insertPlainText("Ready!")
                Driver.new_path(self)
            else:
                self.vi_entry.clear()
                self.vi_entry.setText("PATH error!")
                self.vi_txt_entry.clear()
                self.vi_txt_entry.insertPlainText("PATH error!")

        else:
            self.vi_entry.clear()
            self.vi_entry.setText("Permission denied!")
            self.vi_txt_entry.clear()
            self.vi_txt_entry.insertPlainText("Permission denied!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Driver()
    root.show()
    sys.exit(app.exec())
