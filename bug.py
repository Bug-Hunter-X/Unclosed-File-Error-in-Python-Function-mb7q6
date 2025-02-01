def function_with_unclosed_file(filename):
    file = open(filename, 'w')
    file.write('This file is not closed!')
    # Missing file.close() or using 'with open(...)'