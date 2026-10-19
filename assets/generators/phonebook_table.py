#Based on https://dev.to/dataformathub/transform-csv-data-to-html-tables-for-web-display-a-comprehensive-guide-443

import csv

def csv_to_html_table(csv_file_path):
    html_string = "<table id=\"phone\" border=\"1\">\n"
    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Read header
        header = next(reader)
        html_string += "    <thead>\n        <tr>\n"
        for col_name in header:
            html_string += f"            <th>{col_name}</th>\n"
        html_string += "        </tr>\n    </thead>\n"
        # Read data rows
        html_string += "    <tbody>\n"
        for row in reader:
            html_string += "        <tr>\n"
            for cell in row:
                if cell.isdigit():
                    html_string += f"            <td><input type=\"number\", maxlength=\"1\",size=\"1\">/{cell}</td>\n"
                elif cell.lower() in ['true','false']:
                    html_string += f"            <td><input type=\"checkbox\"></td>\n"
                else:
                    html_string += f"            <td>{cell}</td>\n"
            html_string += "        </tr>\n"
        html_string += "    </tbody>\n"
    html_string += "</table>"
    return html_string

# Example usage:
csv_file = '../data/phone.csv'
html_output = csv_to_html_table(csv_file)

# print(html_output)

# To save to an HTML file:
with open('../../phones.html', 'w') as f:
    f.write("""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>Phonebook</title>
        <!-- datatables -->
        <link rel="stylesheet" href="https://cdn.datatables.net/v/dt/dt-3.1.4/datatables.min.css">
        <script src="https://cdn.datatables.net/v/dt/dt-3.1.4/datatables.min.js"></script>

        <script>
        DataTable.Dom.s(document).on('ready', () => {
            new DataTable('#phone', {
                order: [7, 'asc'],
                pageLength: -1
            })
        });
        </script>
    </head>
    <body>

    
    """
    )
    f.write(html_output)
    f.write("</body>")