import csv  
import sys
import os

class Editor:
    def __init__(self):
        self.data = []
        self.edit_data = []

    def get_file(self, input_file_name):
        try:
            file = open(input_file_name, 'r')
        except FileNotFoundError:
            print("Error: no file!")
            for f in os.listdir('.'):
              if os.path.isfile(f):
                print(f)
                sys.exit()
        
        with open(input_file_name) as file:
            for line in file.readlines():
                text = line.split(';')
                text = [n.replace('\n', '') for n in text]
                self.data.append(text)
    
    def data_to_edit(self, changes):
        for command in changes:
            commands = command.split(",")
            self.edit_data.append(commands)

    def make_edit(self):
        for x in self.edit_data:
            i = int(x[0])
            j = int(x[1])
            text = x[2]
            self.data[i][j] = text

    def save_new_file(self, output_file_name):
        with open(output_file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for item in self.data:
                writer.writerow(item)