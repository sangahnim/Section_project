from flask import Flask
from flask_app.routes.main_route import bp as main_bp # route에다가 blueprint등록하기위한거!!

app = Flask(__name__) # 이 앱이 실행된다면 폴더인 flask_app이 __name__이 됨!
app.register_blueprint(main_bp) # route에다가 blueprint등록하기 위해서@ 

@app.route('/', methods=['POST']) # =>127.0.0.1:5000 + /->127.0.0.1:5000/
# methods=['POST']를 넣지 않으면 url에서 return값을 받아오는건 가능하지만, 보내는건 안됨.Fla 그래서 보내는거랑 동일하게 하기 위해 methods=['POST']를 쓰는거임! 이건 postman에서 확인가능!!!!

def index():
    return 'Hello Flask', 200 # 200은 전달하지 않아도 됨. 만약에 return에 500만 하면 에러가뜸. type error라고 뜨는데, str, dict, typle 셋 중 하나가 와야한다는거임. {'Hello':'Flask'}이런 식으로 쓰면 json형식으로 나옴!! 

@app.route('/user/', defaults={'user_id':0})
# routing endpoint라고 하는데 user/다음 여기에 뭐가 와야하는거임!!! user/까지만오면 아무것도 안나옴!!이걸 나오기 위해서는 default를 설정해주면됨!! 하나로 하기 보다는 나눠서 해줌!! route를 많이 사용하게 될테니 라우트를 만듦!! 

@app.route('/user/<user_id>') 
def user_index(user_id):
    return f'Here is your id {user_id}'


if __name__ == '__main__':
    app.run(debug=True)

