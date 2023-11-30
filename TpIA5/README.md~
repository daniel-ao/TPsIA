In this tp we got the idea on how does the Apriory algortihm work, and in this tp I created the python script based on the codes that were given in the pdf, and I executed my code which worked fine. And in addidtion to that I used the functions given in the pdf which was the "output" function to create the new files in which I filled the results with automatically through my code. So when my script is executed two folders will be created using the output function which will have the transactions done and the results of the algorithm.
As I did another script with values I gave to the apriory algorithm to understand how does it work and now I'm gonna come with a small summary about how changing the values affect the algorithm.

When we change the values of the parameters in the Apriori algorithm, it can have the following effects:

min_support: This parameter determines the minimum support threshold for an itemset to be considered frequent. Changing min_support affects the number of frequent itemsets. Lowering it allows more itemsets to be considered frequent, resulting in more rules. Raising it filters out less common itemsets, leading to fewer but more significant rules.

min_confidence: Changing the min_confidence threshold affects the strength of the generated association rules. Lowering this value results in more rules, including weaker ones. Raising it filters out weaker rules and yields only high-confidence rules.

min_lift: The min_lift parameter controls the minimum lift threshold for association rules. Raising it will result in fewer but more significant rules, as only those with a higher lift are considered. Lowering it includes rules with lower lift values.

min_length: By specifying min_length, you set a minimum number of items required in an association rule. Changing this value affects the complexity and length of the rules generated. If you set it to a higher value, you'll get longer rules, which may be more specific.

Overall, adjusting these parameters allows you to fine-tune the Apriori algorithm to generate association rules that are most relevant to your specific dataset and analysis goals. The trade-off lies in finding the right balance between the number of rules and the quality of those rules. Experimentation with different parameter values is key to achieving this balance.

Example:

Imagine that we have the following database of transactions:

Transaction 1: {apple, orange, banana}
Transaction 2: {apple, banana, milk}
Transaction 3: {orange, milk, bread}
Transaction 4: {apple, milk, bread}
We can use the Apriori algorithm to find the frequent item sets and association rules in this database.

Frequent item sets

The following item sets are frequent with a minimum support threshold of 50%:

{apple, milk}
{apple, bread}
{milk, bread}

