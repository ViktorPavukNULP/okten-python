with open('emails.txt', 'r') as rfile:
    with open('gmails.txt', 'w') as wfile:
        for line in rfile:
            if line.split()[1].endswith('@gmail.com'):
                wfile.write(line)
