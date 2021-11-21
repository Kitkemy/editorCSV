import sys
from edit_csv import Editor

input_file_name = sys.argv[1:][0]
output_file_name = sys.argv[1:][1]
changes = sys.argv[1:][2:]

editor = Editor()

editor.get_file(input_file_name)
#print(editor.data)
editor.data_to_edit(changes)
#print(editor.edit_data)
editor.make_edit()
#print(editor.data)
editor.save_new_file(output_file_name)
