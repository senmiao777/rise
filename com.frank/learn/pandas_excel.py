# coding=utf-8
import pandas as pd
import numpy as np

np.set_printoptions(precision=6, edgeitems=2, linewidth=75, suppress=True, nanstr='nan', infstr='inf')
pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000, 'display.precision', 6, 'display.float_format',
              lambda x: '%.6' % x)


def _sort(s):
    raw_data = pd.read_excel(s)
    raw_data.sort_values(by=['uri', 'plantform'], inplace=True, ascending=[False, False])
    raw_data['占比(%)'] = (raw_data['eventnumber'] * 100) / (raw_data.groupby(['uri', 'plantform'])['eventnumber'].transform('sum'))
    pd.DataFrame(raw_data).to_excel(
        excel_writer='C:/Users/guojingfeng/Desktop/raw_data/test.xlsx',
        float_format='%.6f')


# https://pandas.pydata.org/pandas-docs/version/1.0.0/user_guide/indexing.html#indexing
def _sort2(s):
    pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000, 'display.float_format', lambda x: '%.6f' % x)
    raw_data = pd.read_excel(s);
    print(raw_data);
    data = raw_data.iloc[0].values
    print("获取到所有的值:\n{0}".format(data))  # 格式化输出
    print("index:\n{0}".format(raw_data.index))  # 格式化输出
    # 输出标题行
    # print("columns:\n{0}".format(raw_data.columns))  # 格式化输出
    # 输出第5行数据，数据从第0行开始，不包括标题行
    # print("loc:\n{0}".format(raw_data.loc[4]))  # 格式化输出
    # 输出第0~3行数据，不包括标题行
    # print("loc22s:\n{0}".format(raw_data.loc[0:3]))
    # 根据列名输出
    # print("loc22s:\n{0}".format(raw_data['plantform']))
    # 赋值处理
    # raw_data[['plantform']] = raw_data[['uri']]
    # print("loc2222:\n{0}".format(raw_data))

    # use this form to create a new column
    # raw_data['ratio'] = list(range(len(raw_data.index)))
    # 在指定位置添加新的一列
    # raw_data.insert(0,'tes',list(range(len(raw_data.index))))
    # 对tes列元素的每个值进行加一操作
    # raw_data[['tes']] = raw_data[['tes']] +1


    # 根据坐标访问cell数据raw_data.iloc[0, 3]
    # iloc_ = raw_data.iloc[0, 3]
    # print("loc2222:\n{0}".format(iloc_))

    # 根据坐标修改cell数据raw_data.iloc[0, 3]
    # raw_data.iloc[0, 3] = 'erwetewtt'
    # print("loc2222:\n{0}".format(raw_data.iloc[0, 3]))

    # 分组，统计
    # eventnumber__sum = raw_data.groupby(['uri', 'plantform'])['eventnumber'].sum()
    # print("eventnumber__sum:\n{0}".format(eventnumber__sum))


    # raw_data['ratio'] = (raw_data['eventnumber'] * 100) / (
    #     raw_data.groupby(['uri', 'plantform'])['eventnumber'].transform('sum'))

    # raw_data['ratio']=raw_data.groupby(['uri', 'plantform'])['eventnumber'].transform('sum')
    """
    transform = raw_data.groupby(['uri', 'plantform'])['eventnumber'].transform('sum')
    print("transform:\n{0}".format(transform))

       0     244298
       1          2
       2     244298
       3    2944476
       4     244298
       5    2944476
       6    2944476
       7     244298
    """
    print("loc2222:\n{0}".format(raw_data))
    pd.DataFrame(raw_data).to_excel(excel_writer='C:/Users/xxx/Desktop/raw_data/show11229.xlsx',
                                  float_format='%.6f')


print("zhixing", _sort('C:/Users/xxx/Desktop/raw_data/29771175.xlsx'))
