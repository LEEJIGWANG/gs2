from flask import Flask, make_response, jsonify, request

import sender_test
import url_test
#import predict
import spam_model
app = Flask(__name__)
app.config['JSON_AS_ASCLL'] = False

@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request.is_json)
    data = request.get_json()
    print(data)

    URL = data["URL"] #json 파일에서 url만
    sender = data["sender"] # 전화번호만
    contents = data["contents"] # 내용만

    re_url = url_test.url_check(URL) #url를 URL_test 파일에 있는 함수 url_check 호출
    re_sender = sender_test.sender_check(sender) #전화번호를 sender_test 파일에 있는 함수 sender_check 호출
    re_constants = spam_model.spam_predict(contents)
    #re_constants = predict.spam_predict(contents) # spam_model의 spam_predict 호출

    print("URL 검사 결과 : " + str(re_url))
    print("sender 검사 결과 : " + str(re_sender))
    print("contents 검사 결과 : " + str(re_constants ))


    # 번호 and 내용 or URL == 1 : 스미싱
    if re_constants or (re_url and re_sender) == 1:
        print("스팸")
        return "1"
    elif re_constants or (re_url and re_sender) == 0 :
        print("정상")
        return "0"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
