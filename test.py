import pickle
import preprocessing

preprocessing.generate_data()
print("done.")

with open(b'network.p','rb') as f:
    data = pickle.load(f)

for author in data.authors:
    if author.instituted is not None:
        print(author.instituted)
