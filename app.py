from flask import Flask, request, make_response, json, render_template, jsonify
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web

application = Flask(__name__)
application.url_map.strict_slashes = False


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main_view.html')


@application.route('/main', methods=['POST'])
def main():
    params = json.loads(request.data, encoding='utf-8')
    print(params)
    # return "Hello, World"
    res = []
    # res = {}
    endDt = datetime.datetime.now()
    startDt = endDt + datetime.timedelta(days=-7)
    for code in params:
        df = web.DataReader(code,
                            'naver',
                            start=startDt.strftime('%Y-%m-%d'),
                            end=endDt.strftime('%Y-%m-%d'))
        df['Open'] = df['Open'].astype(float)
        df['Close'] = df['Close'].astype(float)
        df['High'] = df['High'].astype(float)
        df['Low'] = df['Low'].astype(float)
        # res[str(code)] = df["Close"].to_list()
        res.append(df["Close"].to_list())
    return make_response({"closePrice": res}, 200)


@application.route('/getDf', methods=['POST'])
def getDf():
    print(request)
    # print(request.get_data())
    params = json.loads(request.data, encoding='utf-8')
    code = params['code']
    # code = request.form['code']
    endDt = datetime.datetime.now()
    startDt = endDt + datetime.timedelta(days=-30)
    # pandas-datareader를 이용해서 naver부터 종목 코드에 해당하는 데이터를 받아옴.
    df = web.DataReader(code,
                        'naver',
                        start=startDt.strftime('%Y-%m-%d'),
                        end=endDt.strftime('%Y-%m-%d'))
    print(startDt.utcnow())
    print(df)
    df['Open'] = df['Open'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    res = jsonify({"open": df['Open'].to_list()})
    print(res)
    return make_response({"openPrice": df['Open'].to_list(),
                          "closePrice": df['Close'].to_list(),
                          "highPrice": df['High'].to_list(),
                          "lowPrice": df['Low'].to_list(),
                          "days": 30
                          },
                         200)
    # return jsonify({"open": df['Open'].to_list()})


if __name__ == "__main__":
    application.run("0.0.0.0", 8000, True)
    # application.run("0.0.0.0", 8000)
    # code = "005935"
    # endDt = datetime.datetime.now()
    # startDt = endDt + datetime.timedelta(days=-30)
    # df = web.DataReader(code,
    #                     'naver',
    #                     start=startDt.strftime('%Y-%m-%d'),
    #                     end=endDt.strftime('%Y-%m-%d'))
    # df = df.astype(np.float)
    # print(df['Close'].pct_change().fillna(0))
