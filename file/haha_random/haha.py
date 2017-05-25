#coding=gb2312
#������������Ծ�
import shelve,random
#��������Ծ� 
quizs={'Hunan':'Changsha',
'Shaanxi':'Xi\'an',
'Tibet':'Lhasa',
'Xinjang':'Urumqi',
'Beijing':'Beijing',
'Hebei':'Shijiazhuang','Inner Mongolia':'Hohot',
'Jiangxi':'Nanchang','Guangdong':'Guangzhou',
'Guangxi':'Nanning','Jiangsu':'Nanjing',
'Zhejiang':'Hangzhou','Guizhou':'Guiyang','Yunnan':'Kunming'}

for quiznum in range(1,6):
    #д�����
    quizfile=open('quiz'+str(quiznum)+'.txt','w')
    quizfile.write('Name:\nDate:\nRemark:\n')
    quizfile.write(' '*20+'China capital quiz, Form '+str(quiznum)+' '*20+'\n')
    #ϴ�� ���ɲ�ͬ������
    allquest=list(quizs.keys())
    random.shuffle(allquest)
    fourquest=random.sample(allquest,4)#ѡ�����ĸ�����
    n=1
    for ques in fourquest:
        correct=quizs[ques]
        allanw=list(quizs.values())
        del allanw[allanw.index(correct)]
        wrong=random.sample(allanw,3)
        anwgroup=[correct] +wrong
        random.shuffle(anwgroup)
        quizfile.write('%s' % n+'. What\' s the capital of '+ques+' Province?\n')
        for i in range(0,4):
            quizfile.write('ABCD'[i]+'. '+anwgroup[i]+'\n')
        quizfile.write('\n\n')
        n=n+1
    quizfile.close()