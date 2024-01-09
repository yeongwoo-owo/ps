## 문제
길이가 같은 두 큐가 있다. 하나의 큐에서 꺼낸 숫자는 다른 큐에 들어간다. 두 큐 안의 숫자의 합이 동일해지기 위한 최소 이동 횟수를 구해라.

[프로그래머스 - 두 큐의 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

## 풀이

### 큐를 이용한 풀이 
두 큐의 합이 동일하기 때문에 하나의 큐에 들어있는 숫자의 합은 모든 숫자의 합의 절반이다.
따라서 두 숫자의 합이 홀수인 경우에는 조건을 만족할 수 없다.
```python
target = sum(queue1 + queue2)
if target % 2 != 0:
    return -1
target //= 2
```

문제의 핵심 아이디어는 다음과 같다.
> 큐의 합이 target보다 작은 경우, 다른 큐에서 숫자를 받는다.
> 
> 큐의 합이 target보다 큰 경우, 다른 큐로 숫자를 보낸다.

파이썬의 List는 동적 배열이기 때문에, 배열 맨 앞의 원소를 꺼내는 연산은 **O(N)** 의 시간복잡도를 가진다. 
따라서 기본 리스트 대신 LinkedList를 이용해야 한다.

파이썬 collections 라이브러리의 deque 자료구조를 이용하면 O(1)의 시간복잡도로 맨 앞의 원소를 꺼내는 연산을 할 수 있다.

```python
queue1 = deque(queue1)
queue2 = deque(queue2)
```

문제의 핵심 아이디어를 구현한 코드는 다음과 같다. queue1에 들어가 있는 숫자의 합을 cur이라고 하면,
- cur > target인 경우, queue1에서 dequeue한 숫자를 queue2에 enqueue한다.
- cur < target인 경우, queue2에서 dequeue한 숫자를 queue1에 enqueue한다.
- cur == target인 경우, count를 반환한다.

> 매 연산마다 sum() 함수를 호출하면 시간초과가 발생한다.

```python
while count <= max_count:
    if cur > target:
        moved = queue1.popleft()
        queue2.append(moved)
        cur -= moved
    elif cur < target:
        moved = queue2.popleft()
        queue1.append(moved)
        cur += moved
    else:
        return count
    count += 1
return -1
```

이 반복문을 몇 번 실행해야 모든 상황을 다룰 수 있을까?

최악의 경우는 **하나의 큐의 뒤에서 두번째 숫자가 나머지 숫자의 합과 같은 경우 발생한다.**

예를 들어, queue1에 `[1, 1, 1, 1]`이 들어 있고, queue2에 `[1, 1, 7, 1]`이 들어있다고 가정하자.
target은 모든 숫자의 합의 절반인 7이다.

queue1을 기준으로 했을 때, 모든 수의 합이 7보다 작기 때문에 queue2에서 숫자를 꺼내서 집어넣는다.
- queue1: `[1, 1, 1, 1, 1]` 
- queue2: `[1, 7, 1]`

이후에도 모든 수의 합은 5로 7보다 작기 때문에 queue2에서 숫자를 꺼낸다.
- queue1: `[1, 1, 1, 1, 1, 1]`
- queue2: `[7, 1]`

마찬가지로 모든 수의 합은 6이므로 queue2에서 숫자를 꺼낸다.
- queue1: `[1, 1, 1, 1, 1, 1, 7]`
- queue2: `[1]`

이후에는 queue1의 숫자가 계속 queue2보다 크기 때문에 queue1의 숫자 1이 모두 queue2로 갈때까지 이 과정을 반복한다.
- queue1: `[7]`
- queue2: `[1, 1, 1, 1, 1, 1, 1]`

일반화해보면, 큐 하나의 길이를 n이라고 했을 때 최악의 경우는 `(n - 1) + (n + n - 1 - 1) = 3n - 3` 이다.
- `n - 1`: queue2에서 queue1로 이동한 숫자의 수
- `n`: 원래 queue1에 있던 숫자의 수
- `n - 1`: queue1에서 queue2로 이동한 숫자의 수
- `1`: 마지막에 queue1에 남아있는 숫자의 수

조건에 따라 두 큐의 길이가 같기 때문에, 최대 반복 횟수는 `len(queue1) * 3 - 3`이고, 
이 횟수를 넘는 경우 불가능한 경우로 -1을 반환하면 된다.

#### 코드
```python
from collections import deque


def solution(queue1, queue2):
    target = sum(queue1 + queue2)
    if target % 2 != 0:
        return -1
    target //= 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    count = 0
    cur = sum(queue1)
    max_count = len(queue1) * 3 - 3
    while count <= max_count:
        if cur > target:
            moved = queue1.popleft()
            queue2.append(moved)
            cur -= moved
        elif cur < target:
            moved = queue2.popleft()
            queue1.append(moved)
            cur += moved
        else:
            return count
        count += 1
    return -1
```

### 투포인터를 이용한 풀이
위의 풀이에서 queue1에서 나온 숫자는 queue2의 맨 뒤로 가고, queue2에서 나온 숫자는 queue1의 맨 뒤에 들어간다는 것을 알 수 있다.
이를 통해 마치 두 큐가 하나의 배열처럼 동작한다는 것을 연상할 수 있다.

이 아이디어를 통해 문제를 바꾸면 다음과 같다.
> 하나의 배열에서 연속된 구간의 합이 target인 경우를 찾아라.
 
배열의 연속된 부분을 이용하는 알고리즘에는 투포인터가 있다. 투포인터란 하나의 배열에 두 지점인 **start**, **end**를 지정하고,
원하는 조건의 부분 배열을 찾기 위해 두 포인터를 움직이는 알고리즘이다.

투포인터에 맞게 핵심 아이디어를 변경하면 다음과 같다.
> 두 포인터 사이 숫자들의 합이 target보다 큰 경우 start에 1을 더한다.
> 
> 두 포인터 사이 숫자들의 합이 target보다 작은 경우 end에 1을 더한다.

문제 상황을 재연하기 위해서 배열을 queue1 뒤에 queue2를 연결하는 형태로 지정했고, start를 queue1의 시작지점, end를 queue2의 시작지점으로 정했다.
```python
queue = queue1 + queue2

start = 0
end = len(queue1)
```
위의 예시와 동일한 queue1 = [1, 1, 1, 1], queue2 = [1, 1, 7, 1]을 이용하면 다음과 같은 상황이 된다.

- `< 1 1 1 1 > 1 1 7 1`

start와 end 사이의 합이 4로 target인 7보다 작기 때문에 end를 한 칸 옮긴다.

- `< 1 1 1 1 1 > 1 7 1`

마찬가지로 과정을 반복하면 다음과 같은 순서로 진행된다.

- `< 1 1 1 1 1 1 > 7 1`
- `< 1 1 1 1 1 1 7 > 1`
- `1 < 1 1 1 1 1 7 > 1`
- `1 1 < 1 1 1 1 7 > 1`
- `1 1 1 < 1 1 1 7 > 1`
- `1 1 1 1 < 1 1 7 > 1`
- `1 1 1 1 1 < 1 7 > 1`
- `1 1 1 1 1 1 < 7 > 1`

```python
while start < end < len(queue):
    if cur < target:
        cur += queue[end]
        end += 1
    elif cur > target:
        cur -= queue[start]
        start += 1
    else:
        return count
    count += 1
return -1
```

종료 조건에서 `start < end`인 경우는 하나의 숫자가 나머지 숫자의 합보다 큰 경우를 의미한다. 
`end < len(queue)`인 경우는 모든 배열을 순회해도 원하는 조건을 만족하는 부분 배열을 찾지 못함을 의미한다.
두 경우는 원하는 조건이 없기 때문에 `-1`을 반환하면 된다.

주의해야 할 점은 해당 알고리즘에서 **end가 왼쪽으로 이동하는 일은 존재하지 않는다**는 것이다.
따라서 두 큐의 순서가 바뀌면 원하는 조건을 찾을 수 없다.

이 방법을 해결하기 위해서 간단하게 queue1을 뒤에 한번 더 더해주면 된다. 
```python
queue = queue1 + queue2 + queue1

start = 0
end = len(queue1)
```

#### 코드
```python
def solution(queue1, queue2):
    target = sum(queue1 + queue2)
    if target % 2 != 0:
        return -1
    target //= 2

    queue = queue1 + queue2 + queue1

    start = 0
    end = len(queue1)

    count = 0
    cur = sum(queue1)
    while start < end < len(queue):
        if cur < target:
            cur += queue[end]
            end += 1
        elif cur > target:
            cur -= queue[start]
            start += 1
        else:
            return count
        count += 1

    return -1
```

## 고찰
문제의 핵심 아이디어 자체는 복잡하지 않고, 문제에 주어진 큐를 그대로 이용해서 해결할 수 있어서 어렵지 않은 문제라고 생각한다.
하지만 반복문의 종료 조건을 생각해내는 과정이 조금 복잡할 수 있다고 생각했다.

> 프로그래머스의 테스트 케이스가 부족해서 queue1의 숫자가 queue2로 이동했다가 다시 queue1로 이동하는 경우를 고려하지 않아도 정답 처리된다.
> - 입출력 예시 2번을 보면, queue1: `[1, 2, 1, 2]` queue2: `[1, 10, 1, 2]`인 경우 정답이 7이다. 
> - 투포인터를 이용한 풀이에서 위의 조건을 고려하지 않고 queue1을 뒤에 추가하지 않은 코드는 **queue1과 queue2를 서로 바꾸었을 때 -1**이라는 오답이 나온다.
> - 하지만 채점 결과 정답으로 처리된다.