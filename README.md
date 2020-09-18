# IntroductionToAlgorithms
## insertion_sort
```python
def insertion_sort(array):
    """ simple insertion sort """
    for i in range(1, len(array)):
        key = array[i].lower()
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

    return array

```
I try to sort book "Eugene Onegin"

result:
```
words count:  42984
size array:  382624
unique words:  7922
first 50 words:  ['the', 'project', 'gutenberg', 'ebook', 'eugene', 'on', 'guine', 'onegin', 'by', 'aleksandr', 'sergeevich', 'pushkin', 'translated', 'by', 'henry', 'spalding', 'this', 'ebook', 'is', 'for', 'the', 'use', 'of', 'anyone', 'anywhere', 'at', 'no', 'cost', 'and', 'with', 'almost', 'no', 'restrictions', 'whatsoever', 'you', 'may', 'copy', 'it', 'give', 'it', 'away', 'or', 're', 'use', 'it', 'under', 'the', 'terms', 'of', 'the']
====================  START insertion_sort  ====================
START:  2020-06-02 09:02:43.834782
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
FINISH:  2020-06-02 09:03:48.731126
RESULT:  0:01:04.896344
====================  START sorted  ====================
START:  2020-06-02 09:03:48.731154
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
FINISH:  2020-06-02 09:03:48.731916
RESULT:  0:00:00.000762
```
