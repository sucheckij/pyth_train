from lib.classes.worker import *


def exportToHtmil(wrk: Worker):
    plik = rf'files/{wrk.fname}_{wrk.lname}.html'
    template = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>wrk.fname</title>
</head>
<body>    
    <table border="1">
        <tr><th>imie</th><th>nazwisko</th><th>dział</th><th>stanowisko</th></tr>
        <tr><td>{wrk.fname}</td><th>{wrk.lname}</th>
            <th>{wrk.job}</th></tr>
    </table>
</body>
</html>
    """
    with open(plik, 'w', encoding='utf-8') as p:
        p.write(template)
