# coding=utf-8
# itertools ��ʹ��
import itertools
natuls = itertools.count(1) # ���λ1�����޵�����
end = itertools.takewhile(lambda x: x <= 10, natuls)  # �����˷�Χ
for n in end:
    print(n)
# chain���� ���ӣ�
for c in itertools.chain('ABC', 'XYZ'):
        print(c)
# groupby : �����ڵ��ظ���Ԫ������������һ��
for key, group in itertools.groupby('AAABBBCCaaaAAAa', lambda x: x.upper()):
    print(key, list(group))
