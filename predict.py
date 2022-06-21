from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

#내용
loaded_model = load_model('best_model.h5')
tokenizer = Tokenizer()
max_len = 271

#전화번호
loaded_model_se = load_model('best_model_sender.h5')
tokenizer_se = Tokenizer()
max_len_se = 271

#내용
#from spam_model import spam_predict
def spam_predict(content):
    content_encoded = tokenizer.texts_to_sequences([content])   #받은 사용자 텍스트를 정수 인코딩
    print(content_encoded)
    content_pad_new = pad_sequences(content_encoded, maxlen = max_len) #받은 사용자 텍스트를 패딩
    predict_content = float(loaded_model.predict(content_pad_new)) #예측
    
    print("검증 데이터의 정확도는 %.4f 입니다. \n" % (predict_content))
    if(predict_content > 0.5):
        print("{:.2f}% 확률로 스미싱 문자입니다. \n".format(predict_content *100))
        return 1
    else:
        print("{:.2f}% 확률로 정상 메세지입니다.\n".format((1-predict_content)*100))
        return 0
#spam_predict("감사합니다. 일단 잠정적으로는 6월 22일 15시에 진행을 할 예정인데 확정되면 다시 한번 안내드리겠습니다.")
#스미싱: 광고오까네설연휴할인쿠폰전상품중복할인가능월까지무료수신거부


#전화번호
def spam_predict_sender(sender):
    content_encoded = tokenizer_se.texts_to_sequences([sender])  # 받은 사용자 텍스트를 정수 인코딩
    print(content_encoded)
    content_pad_new = pad_sequences(content_encoded, maxlen=max_len_se)  # 받은 사용자 텍스트를 패딩
    predict_content = float(loaded_model_se.predict(content_pad_new))  # 예측

    print("검증 데이터의 정확도는 %.4f 입니다. \n" % (predict_content))
    if (predict_content > 0.5):
        print("{:.2f}% 확률로 스미싱 전화번호 입니다. \n".format(predict_content * 100))
        return 1
    else:
        print("{:.2f}% 확률로 정상 전화번호 입니다.\n".format((1 - predict_content) * 100))
        return 0


#spam_predict("감사합니다. 일단 잠정적으로는 6월 22일 15시에 진행을 할 예정인데 확정되면 다시 한번 안내드리겠습니다.")
# 스미싱: 광고오까네설연휴할인쿠폰전상품중복할인가능월까지무료수신거부