### Tanja Crijns s4204999 - Exercises week 3: Evaluation
The following list of Rs and Ns represent relevant (R) and nonrelevant (N) returned documents in a ranked list of 20 documents retrieved in response to a query from a collection of 10,000 documents. The top of the ranked list is on the left of the list. This list shows 6 relevant documents. Assume there are 8 relevant documents in total in the collection. <br/>

R R N N N  N N N R N  R N N N R  N N N N R

---

#### 1. Calculate Precision, Recall and F1 for this result list
Precision: <br/># retrieved relevant documents / # retrieved documents<br/>
`6/20 = 0,3`<br/><br/>
Recall: <br/># retrieved relevant documents / # relevant documents <br/>
`6/8 = 0,75`<br/><br/>
f1: <br/>2 \* (precision \* recall / precision + recall)<br/>
`2 * (0,3 * 0,75 / 0,3 + 0,75) = 0,4285714`

---

#### 2. Calculate Average Precision
Average precision:<br/>
`(1/1 + 2/2 + 3/9 + 4/11 + 5/15 + 6/20) / 8 = 0,4163`<br/>
Which is based on the following table:

| |k|R|P|
|---|:---:|:---:|:---:|
|x | 1 | 1/8 | 1/1|
|x | 2 | 2/8 | 2/2|
| | 3 | 2/8 | 2/3|
| | 4 | 2/8 | 2/4|
| | 5 | 2/8 | 2/5|
| | 6 | 2/8 | 2/6|
| | 7 | 2/8 | 2/7|
| | 8 | 2/8 | 2/8|
|x | 9 | 3/8 | 3/9|
| | 10 | 3/8 | 3/10|
|x | 11 | 4/8 | 4/11|
| | 12 | 4/8 | 4/12|
| | 13 | 4/8 | 4/13|
| | 14 | 4/8 | 4/14|
|x | 15 | 5/8 | 5/15|
| | 16 | 5/8 | 5/16|
| | 17 | 5/8 | 5/17|
| | 18 | 5/8 | 5/18|
| | 19 | 5/8 | 5/19|
|x | 20 | 6/8 | 6/20|

---

#### 3. Draw the Precision-Recall graph
![Precision-Recall Graph](http://i.imgur.com/JTl0FOQ.png)<br/><br/><br/>
---
#### 4. Assume that R=1 and N=0
- ###### Calculate CG@20
![](http://i.imgur.com/0gb92Wf.png)<br/>
For this problem: CG(L): `1 + 1 + 1 + 1 + 1 + 1 = 6`


- ###### Calculate DCG@20
![](http://i.imgur.com/TSl0NxJ.png)<br/>
For this problem: DCG(L): `1 + 1 + 1/2log(9) + 1/2log(11) + 1/2log(15) + 1/2log(20) = 3,092`



- ###### Calculate nDCG@20
![](http://i.imgur.com/gjWH4hJ.png)<br/>
Where iDDG = the DCG for the ideally ranked list. We have 8 relevant documents; in an ideal list, those documents will be returned first. There is no further ranking for those 8 documents, they are equally relevant.
The iDCG is `16,3`, which makes the nDCG(L): `3,09/16,3 = 0,19`.
