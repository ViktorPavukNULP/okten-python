try:
    with open('emails.txt', 'r') as rfile:
        with open('gmails.txt', 'w') as wfile:
            for line in rfile:
                mail = line.split()[1]
                if mail.endswith('@gmail.com'):
                    wfile.write(mail+'\n')
except FileNotFoundError:
    print(FileNotFoundError)
except Exception:
    print(Exception)