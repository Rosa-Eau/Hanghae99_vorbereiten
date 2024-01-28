from flask import Flask, render_template, request
app = Flask(__name__)
import random
from collections import Counter
import requests
from datetime import datetime

@app.route('/')
def home():
    name = '오진선'
    lotto = [16, 18, 22, 43, 32, 11]

    def generate_lotto_numbers():
        # 1부터 45까지의 숫자 중에서 6개를 무작위로 선택
        random_lotto = random.sample(range(1, 46), 6)
        # 선택된 숫자들을 정렬
        random_lotto.sort()
        return random_lotto
    
        # 로또 번호 생성
    random_lotto = generate_lotto_numbers()
        
    def count_common_elements(list1, list2):
        # Counter를 사용하여 각 리스트의 요소 개수를 센다
        counter1 = Counter(list1)
        counter2 = Counter(list2)

        # 두 리스트에서 공통된 요소를 찾아 개수를 비교한다
        common_elements = counter1 & counter2
        return sum(common_elements.values())
        
    # 공통된 요소 개수 확인
    common_count = count_common_elements(lotto, random_lotto)
            
    # 결과 출력
    print("로또 번호: {}".format(random_lotto))
    context = {
        "name" : name,
        "lotto" : lotto,
        "random_lotto" : random_lotto,
        "common_count" : common_count,
    }
    print(context)
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}")
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]

    return render_template('movie.html', data=movie_list)

@app.route('/box')

def box():
    if request.args.get('q') :
        q = request.args.get('q')
    else :
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%Y%m%d")
        print(formatted_date)
        q = formatted_date
        
    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={q}"

    res = requests.get(URL)
    rjson = res.json()
    b_list = rjson.get("boxOfficeResult").get("weeklyBoxOfficeList")
    
    return render_template('box.html', data=b_list)

if __name__ == '__main__':  
    app.run(debug=True)