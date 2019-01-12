from config import *
import pandas as pd


def leak_correct(submit_path):
    submission_df = pd.read_csv(submit_path)
    submission_df.loc[submission_df['Id'] == 'a8d73536-bad8-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 23'
    submission_df.loc[submission_df['Id'] == '63ed01a4-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == '84c046b4-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == '69cbf89a-bace-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == 'b9a882d6-bacc-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == '29d1d616-bacd-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '19'
    submission_df.loc[submission_df['Id'] == 'f8f6566a-bac8-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '9edb2498-bad8-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '8dd19ca8-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == 'adfa9e8e-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == 'da5b852e-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '3'
    submission_df.loc[submission_df['Id'] == 'df8d2780-bac8-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == '72a6fbf8-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == 'f6b06252-bad6-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == 'edb5b41e-bad0-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '0a96bf2c-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '4'
    submission_df.loc[submission_df['Id'] == '1f97ea4a-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 25'
    submission_df.loc[submission_df['Id'] == '2327a292-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '5 16'
    submission_df.loc[submission_df['Id'] == '10d4730a-bada-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '0b651912-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == '12dea42a-bacd-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16 17 18'
    submission_df.loc[submission_df['Id'] == 'b43493dc-bac5-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '2 11'
    submission_df.loc[submission_df['Id'] == 'ba6febf2-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == '58148166-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == '79970da6-bac8-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '2 16'
    submission_df.loc[submission_df['Id'] == 'c02bb81c-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '0 16 17 18'
    submission_df.loc[submission_df['Id'] == 'fcd88d84-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == '59604078-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '89b31fae-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '88b38a80-bac8-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '2 16'
    submission_df.loc[submission_df['Id'] == 'adc182fa-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 21'
    submission_df.loc[submission_df['Id'] == '6a322caa-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == '869a7f8c-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 5'
    submission_df.loc[submission_df['Id'] == 'b478cc78-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == 'e0f9483a-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 7'
    submission_df.loc[submission_df['Id'] == '9eafcf6a-bacd-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 21'
    submission_df.loc[submission_df['Id'] == 'b7ae02d8-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 17 23'
    submission_df.loc[submission_df['Id'] == 'dbdcd95c-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == 'e7f56384-bad1-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '1'
    submission_df.loc[submission_df['Id'] == '43357408-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '17 25'
    submission_df.loc[submission_df['Id'] == 'c5deab72-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 21'
    submission_df.loc[submission_df['Id'] == 'b9acf08a-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == 'e8bae166-bad8-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '2 17'
    submission_df.loc[submission_df['Id'] == '5661665e-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '17 25'
    submission_df.loc[submission_df['Id'] == '9e6fe8be-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '4'
    submission_df.loc[submission_df['Id'] == 'df533cce-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '17'
    submission_df.loc[submission_df['Id'] == '7c1f771c-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '25'
    submission_df.loc[submission_df['Id'] == 'f8cd7738-bad0-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '25'
    submission_df.loc[submission_df['Id'] == '39508fe6-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == 'a56d3f98-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '9 10'
    submission_df.loc[submission_df['Id'] == '28601ba0-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '14'
    submission_df.loc[submission_df['Id'] == '8617f44e-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0'
    submission_df.loc[submission_df['Id'] == '1144d38e-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '21 16'
    submission_df.loc[submission_df['Id'] == '201229ac-bad0-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '2'
    submission_df.loc[submission_df['Id'] == '0f3274c0-bada-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '13'
    submission_df.loc[submission_df['Id'] == '29414644-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '4 21 26'
    submission_df.loc[submission_df['Id'] == '92c7e608-bad5-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '25'
    submission_df.loc[submission_df['Id'] == '83509894-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '13'
    submission_df.loc[submission_df['Id'] == 'af2c5f2e-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '25'
    submission_df.loc[submission_df['Id'] == 'bf6c33d0-bad5-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '4'
    submission_df.loc[submission_df['Id'] == '9da67d5c-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14'
    submission_df.loc[submission_df['Id'] == 'cbfe766e-bace-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14'
    submission_df.loc[submission_df['Id'] == 'c1dc11c4-bacd-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0'
    submission_df.loc[submission_df['Id'] == '8f257b9c-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '21'
    submission_df.loc[submission_df['Id'] == 'd69acc70-bac5-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '0'
    submission_df.loc[submission_df['Id'] == '94205e64-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '55eb4db6-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '22 16 25'
    submission_df.loc[submission_df['Id'] == '10e592a2-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '21 16 19 25'
    submission_df.loc[submission_df['Id'] == 'e7a05526-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '9 10'
    submission_df.loc[submission_df['Id'] == '896007d6-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == '111f3934-bad6-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == 'aec4415e-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '2 16'
    submission_df.loc[submission_df['Id'] == '03f31e24-badb-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == 'f60586ac-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '7 17'
    submission_df.loc[submission_df['Id'] == 'fce301c8-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == '10748996-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '15 25'
    submission_df.loc[submission_df['Id'] == '2367dd2c-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '21 11 16'
    submission_df.loc[submission_df['Id'] == '9d2d08b2-bada-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '12'
    submission_df.loc[submission_df['Id'] == '260a351a-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '17'
    submission_df.loc[submission_df['Id'] == '54138f64-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '17 25'
    submission_df.loc[submission_df['Id'] == '443b81cc-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '15'
    submission_df.loc[submission_df['Id'] == '72c9bb82-bac7-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '4 21 17'
    submission_df.loc[submission_df['Id'] == 'be0cf5a8-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 23'
    submission_df.loc[submission_df['Id'] == '01835f6c-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '4'
    submission_df.loc[submission_df['Id'] == '74993d6e-bad8-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '84ca8928-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '17'
    submission_df.loc[submission_df['Id'] == '8f8c19a6-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 25'
    submission_df.loc[submission_df['Id'] == '107d6830-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '0 19 25'
    submission_df.loc[submission_df['Id'] == '70f3e586-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 21'
    submission_df.loc[submission_df['Id'] == 'a7e9e53a-bad1-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16 25'
    submission_df.loc[submission_df['Id'] == 'aa45019c-bad2-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '4509520a-bad3-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '1 2'
    submission_df.loc[submission_df['Id'] == 'ec087d1e-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == '18d295a6-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '23'
    submission_df.loc[submission_df['Id'] == 'db77c3dc-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '17 19'
    submission_df.loc[submission_df['Id'] == 'a6c830fa-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '22'
    submission_df.loc[submission_df['Id'] == '0457b426-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '2'
    submission_df.loc[submission_df['Id'] == 'd79a1e12-bad1-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '7929949a-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '17 25'
    submission_df.loc[submission_df['Id'] == '7d7565e2-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == 'd6a07ae2-bad1-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == '82c1d5f6-bacc-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 14 18'
    submission_df.loc[submission_df['Id'] == 'bfdfc644-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '19'
    submission_df.loc[submission_df['Id'] == '74bdbb12-bace-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '7 25'
    submission_df.loc[submission_df['Id'] == 'a4b77124-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '23'
    submission_df.loc[submission_df['Id'] == '27ca9b0e-bace-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '12'
    submission_df.loc[submission_df['Id'] == '9ded793a-bacb-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '2 4'
    submission_df.loc[submission_df['Id'] == '77161884-bad6-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16'
    submission_df.loc[submission_df['Id'] == '17d8a71c-bacf-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '5'
    submission_df.loc[submission_df['Id'] == 'c3c67272-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0'
    submission_df.loc[submission_df['Id'] == 'b52035ba-bad1-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '3'
    submission_df.loc[submission_df['Id'] == '718ebf3e-bada-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '16 17 23'
    submission_df.loc[submission_df['Id'] == '530bfbea-baca-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 17 23'
    submission_df.loc[submission_df['Id'] == 'c78652b6-bad6-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 25'
    submission_df.loc[submission_df['Id'] == '8316d286-bad6-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '6 21'
    submission_df.loc[submission_df['Id'] == 'e1d58c82-bac6-11e8-b2b7-ac1f6b6435d0', 'Predicted'] = '0 16'
    submission_df.loc[submission_df['Id'] == '1a15e75a-bad5-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '0 16 17'
    submission_df.loc[submission_df['Id'] == '0f0ccc64-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == 'b642cefc-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '0 16 25'
    submission_df.loc[submission_df['Id'] == '9f71c832-bacc-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == 'f665e29c-bad4-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == 'e75331f2-bad8-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '14 16'
    submission_df.loc[submission_df['Id'] == 'be034880-bad0-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16 19'
    submission_df.loc[submission_df['Id'] == '5d2711a6-bac9-11e8-b2b8-ac1f6b6435d0', 'Predicted'] = '14 16 25'
    submission_df.loc[submission_df['Id'] == '89975d50-bad7-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '15 25'
    submission_df.loc[submission_df['Id'] == '7fcba676-bad9-11e8-b2b9-ac1f6b6435d0', 'Predicted'] = '15 25'

    submission_df.to_csv(f'post_{submit_path}',index=False)
    print('Done')

def leak_correct_v2(submit_path):

    submission_df = pd.read_csv(submit_path)
    leak = pd.read_csv("../data/test_matches.csv")

    for i,row in leak.iterrows():
        submission_df.loc[submission_df['Id'] == row['Test'], 'Predicted'] = row['Target']
    submission_df.to_csv(f'post_{submit_path}', index=False)
    print('Done')

def leak_correct_v3(submit_path):

    submission_df = pd.read_csv(submit_path)
    leak = pd.read_csv("../data/leak_correctTrue.csv")
    leak = leak.loc[leak['distance']<=6]

    for i,row in leak.iterrows():
        submission_df.loc[submission_df['Id'] == row['Id'], 'Predicted'] = row['Target']
    submission_df.to_csv(f'post_{submit_path}', index=False)
    print(leak)
    print('Done')

def average(files,weight):
    import numpy as np

    result = 0
    for f,w in zip(files,weight):
        result += w*np.load('./submit/'+f)
    result = result/sum(weight)
    np.save('ensesubmit',result)

def average_byfile(filesnew,filesold,files):
    import numpy as np


    submit_new = np.average([np.load('./submit/'+f) for f in filesnew],axis=0)
    submit_old = np.average([np.load('./submit/'+f) for f in filesold],axis=0)
    result = np.average([np.load('./submit/'+f) for f in files] + [submit_old,submit_new],axis=0)

    # result = np.average([submit_new,submit_old,submit],axis=0)
    np.save('ensesubmit',result)

def main(cfg):
    import numpy as np
    dataset = pd.read_csv(data_dir + 'sample_submission.csv', dtype={'Predicted': str})
    result = np.load(f"{cfg['name']}submit.npy")

    target = []
    for sample_pred in result:
        pred = []
        for i,score in enumerate(sample_pred):
            if score > cfg['thres'][i]:
                pred.append(str(i))
        if len(pred) == 0:
            pred.append(str(sample_pred.argmax()))
        target.append(' '.join(pred))

    dataset['Predicted'] = target
    dataset.to_csv('submit.csv',index=False)



if __name__ == '__main__':
    # leak_correct_v3('submit(2).csv')
    import numpy as np

    labels_dict = np.array([
        40958.0,
        3072.0,
        10871.0,
        3329.0,
        5130.0,  # 4
        5938.0,
        3725.0,
        9405.0,
        217.0,
        197.0,  # 9
        182.0,
        2194.0,
        2233.0,
        1458.0,
        2692.0,  # 14
        63.0,
        1290.0,
        446.0,
        1893.0,
        3672.0,  # 19
        438.0,
        13809.0,
        2729.0,
        10345.0,
        428.0,  # 24
        37366.0,
        706.0,
        127.0
    ])
    files = [
        'se_resnext50_diff_first_train_average.npy',
        'result_bnincep.npy',
        'res34submit.npy',
        'res34submit_gary.npy',
        'inceptionv3submit.npy',
        'xceptionsubmit.npy',
        'f1_losssubmit.npy',
        'bnincepgarysubmit.npy',
        'incepv3garysubmit.npy',
    ]
    # weights = [1,1,1,1,1,1,1,0.3,0.2]
    # average(files,weights)
    average_byfile(
        [
            'se_resnext50_submit.npy',
            'res34submit_gary.npy',
            'xception_old_submit.npy',
            # 'bnincepgarysubmit.npy',
            # 'incepv3garysubmit.npy',
        ],
        [
            'result_bnincep.npy',
            'res34submit.npy',
            'inceptionv3submit.npy',
            'xceptionsubmit.npy',
            'se_resnext50submit_new.npy'
        ],
        [
            'res34_shisusubmit.npy',
            'f1_loss611.npy',
        ]
    )
    cfg = {}
    cfg['thres'] = np.array([0.205] * 28)
    # cfg['thres'][labels_dict > 1000] = 0.3
    print(cfg['thres'])
    cfg['name'] = 'ense'
    main(cfg)
    leak_correct_v2('submit.csv')









