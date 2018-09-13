import praw
import time
import sched
import calendar
import datetime
start_time = calendar.timegm(time.gmtime())

reddit = praw.Reddit(client_id='',client_secret='',password='',user_agent='', username='')
print(reddit.user.me())
s=sched.scheduler(time.time, time.sleep)

def getPosts():
    start_time=calendar.timegm(time.gmtime())
    titles = []
    #Does a check for new submissions, if none then continue... Make sure you have a colon at the end :
    for submission in reddit.subreddit('BuildAPCSales').new():
        #print('starttime')
        #print(start_time)
        #print('posttime')
        #print(submission.created_utc)
        #checks to see if there are new submissions since last check or start of program
        if submission.created_utc < start_time:
            continue

        start = submission.title.find('$')
        end = submission.title.find(' ',start)
        price = submission.title[start:end]
        #adds to title array
        titles.append(submission.title+','+submission.url+','+str(datetime.datetime.fromtimestamp(submission.created))+','+price)
        print('added '+ submission.title)
        print('starttime')
        print(start_time)
        print('posttime')
        print(submission.created_utc)
    #Just a print check of when loop occurs
    print('Checked\n')
    #Writes to file
    with open('data.txt', 'a') as file:
        for x in titles:
            file.write(x+'\n')
    titles = []
    start_time =calendar.timegm(time.gmtime())
    s.enter(60,1,getPosts)

s.enter(60,1,getPosts)
s.run()
#do not set delay to less than 60 or script will get multiple posts
