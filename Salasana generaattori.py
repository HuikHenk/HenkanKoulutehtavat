import random, string
print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int
                             (input("Syötä salasanan pituus: ")))))