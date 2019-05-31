import json
import datetime
import codecs

# with open('./log.text','a',encoding = 'utf-8') as f:
#     d = json.load(f)
#     ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
#     thetime = datetime.datetime.new().strftime(ISOTIMEFORMAT)
#     # for i in d.values():
#     #     print (i)
#     f.write(thetime)

#     f.close()
ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
thetime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

with codecs.open('./log.text', 'a', 'utf-8') as log:
    log.write(thetime+'\t')
    log.write('签到失败')
    log.write('\n')
    log.close()




# http://p.istudy.ga:8081/student/course_detail.html?id=133&caid=102&callback=courseLearn
# http://p.istudy.ga:8081/student/course_detail.html?id=136&caid=16&callback=courseLearn
# http://p.istudy.ga:8081/student/course_detail.html?id=139&caid=17&callback=courseLearn
# http://p.istudy.ga:8081/student/course_detail.html?id=146&caid=34&callback=courseLearn

# driver.find_element_by_partial_link_text('Conti')

# //*[@id='grade_table_length']/label/select


//*[@id="grade_table"]/tbody/tr[1]/td[5]/a[1]