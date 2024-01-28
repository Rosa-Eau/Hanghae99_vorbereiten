import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 무작위로 선택
    lotto_numbers = random.sample(range(1, 46), 6)
    # 선택된 숫자들을 정렬
    lotto_numbers.sort()
    return lotto_numbers

if __name__ == "__main__":
    # 로또 번호 생성
    lotto_result = generate_lotto_numbers()
    
    # 결과 출력
    print("로또 번호: {}".format(lotto_result))
    
    from collections import Counter

def count_common_elements(list1, list2):
    # Counter를 사용하여 각 리스트의 요소 개수를 센다
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # 두 리스트에서 공통된 요소를 찾아 개수를 비교한다
    common_elements = counter1 & counter2

    # 결과 출력
    print("List1: {}".format(list1))
    print("List2: {}".format(list2))
    print("공통된 요소의 개수: {}".format(sum(common_elements.values())))

if __name__ == "__main__":
    # 예시 리스트
    list1 = [1, 2, 2, 3, 4, 5]
    list2 = [2, 3, 3, 4, 5, 5]

    # 공통된 요소 개수 확인
    count_common_elements(list1, list2)
