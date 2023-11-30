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

# Run the Apriori algorithm with your chosen parameters
results = apriori(transactions, min_support=0.01, min_confidence=0.5,
min_lift=1, min_length=2)

# Here I created a new file named MyRes.Txt where I added the results line by line of the content of the file "results"
output = open("MyRes.txt", "w")

for r in results:
    output.write(str(r) + "\n")  # Write each result to the file with a newline character

output.close()


# Here I am gonna create a new file named "Transactions" in which I'm gonna add the transactions done followed by the number of transactions done.
output = open("MyTransactions.txt", "w")

output.write("Number of transactions: " + str(len(transactions)) + "\n")

output.write("The transactions done:\n")
for transaction in transactions:
    output.write(str(transaction) + "\n")
output.close()
