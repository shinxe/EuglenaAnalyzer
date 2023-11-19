# **EuglenaAnalyzer**

Hello.
This program is made for detecting the head coordinates of euglena and count how many times did they rotated.

## Usage
<details open>
<summary>detect head</summary>

```python
import eanalyzer

#detect head coodinates
FILE_PATH = 'Here should be a file path of your YOLO segmantation tracking data txt'
head_coodinates = eanalyzer.detect_head.detect_head(FILE_PATH)

print(head_coodinates)
#[[x,y],[x,y],[x,y]]
```
detect_head() will return a 2D array(float)
</details>

<details open>
<summary>count rotations</summary>

```python
import eanalyzer

#detect head coodinates
COODINATES_LIST = 'Here should be a file path of head coodinates list'
# it means the return of previous section,head_coodinates
count = eanalyzer.count_rotations.count_rotations(COODINATES_LIST)

print(count)
#20
```
detect_head() will return a int value
</details>

## <div style='text-align:center'>License</div>


## <div style='text-align:center'>Contact</div>

[Discord](https://xalyfi.com/discord) a community for questions and discussions<br>
[shinxe](https://discordapp.com/users/1099992603073724547/) for private messages in discord