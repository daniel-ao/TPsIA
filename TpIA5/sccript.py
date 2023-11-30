from apyori import apriori
f = open('corpus.txt', 'r', encoding="utf-8")

def normalize(text):
    return text.strip('\n').replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("-", "")
stopwords = {'the', 'a', 'of', 'for', 'in', 'and', 'de', 'et', 'pour'}

transactions = []
for line in f:
    if len(line) > 1 and not line.startswith("#"):
        words = normalize(line).split()
        items = set()
        for word in words:
            if word not in stopwords:
                items.add(word)
        if len(items)!=0:
            transactions.append(sorted(items))

'''
Pour vérifier qu'elles ont bien été traitées.


for transaction in transactions:
    print(transaction)

'''
#print("Number of transactions:", len(transactions))

results = apriori(transactions, min_support=0.01, min_confidence=0.7,
min_lift=1.2, min_length=2)


# Here I created a new file named Res.Txt where I added the results line by line of the content of the file "results"
output = open("Res.txt", "w")

output.write("Introduction à l'Intelligence Artificielle\n")

output.write("TD5: Règles d'association\n")

for r in results:
    output.write(str(r) + "\n")  # Write each result to the file with a newline character

output.close()


# Here I am gonna create a new file named "Transactions" in which I'm gonna add the transactions done followed by the number of transactions done.
output = open("Transactions.txt", "w")

output.write("Number of transactions: " + str(len(transactions)) + "\n")

output.write("The transactions done:\n")
for transaction in transactions:
    output.write(str(transaction) + "\n")
output.close()

