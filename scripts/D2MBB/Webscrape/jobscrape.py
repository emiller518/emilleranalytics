from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import mysql.connector
import time
import random

dbconn = mysql.connector.connect(
        host="localhost", user="emiller", passwd="Soccer-479", database="hogswith_strosembb")


def getjobs(link, site, keyword):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    source = urlopen(req).read()
    soup = BeautifulSoup(source, "html.parser")
    time.sleep(random.randint(0, 60))
    if site == 'hoopdirt':
        jobtable = soup.find_all("table", {"class": "posts"})[0]
        job = jobtable.find_all("tr")
        for i in job[1:]:
            link = i.find("a")['href']
            org = i.find("a", href=True).contents[0]
            position = i.find_all('td')[1].text
            posted = i.find_all('td')[2].text
            d = datetime.strptime(posted, '%B %d, %Y')
            addjobtodb([link, org, position, d.strftime('%Y-%m-%d'), keyword])

    elif site == 'teamwork':
        links = soup.find_all('a', {"class": "result-item__link"})
        for i in links:
            if 'subscriptions' not in i['href']:
                link = 'https://www.teamworkonline.com' + i['href']
                position = i.find('h3', {'class': 'base-font'}).text
                org = i.find('img')['alt']
                posted = datetime.today().strftime('%Y-%m-%d')
                addjobtodb([link, org, position, posted, keyword])


def addjobtodb(jobdetails, mydb=dbconn):
    mycursor = mydb.cursor()
    sql = "INSERT IGNORE INTO jobemail VALUES (%s, %s, %s, %s, %s, 0);"
    val = (str(jobdetails[0]), str(jobdetails[1]), str(jobdetails[2]), str(jobdetails[3]), str(jobdetails[4]))
    mycursor.execute(sql, val)
    mydb.commit()


def unsentjobs(mydb=dbconn):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('SELECT * from jobemail where sentflag = 0')
    myresult = mycursor.fetchall()
    if myresult is not None:
        return myresult
    else:
        return None


def updatesentflag(mydb=dbconn):
    mycursor = mydb.cursor()
    sql = "UPDATE jobemail SET sentflag = 1 WHERE sentflag = 0;"
    mycursor.execute(sql)
    mydb.commit()

        
time.sleep(random.randint(0, 3600))
       
hoopdirt = 'https://hoopdirt.com/job/'

data = 'https://www.teamworkonline.com/jobs-in-sports?utf8=%E2%9C%93&employment_opportunity_search[query]=data'
developer = 'https://www.teamworkonline.com/jobs-in-sports?utf8=%E2%9C%93&employment_opportunity_search[query]=developer'
engineer = 'https://www.teamworkonline.com/jobs-in-sports?utf8=%E2%9C%93&employment_opportunity_search[query]=engineer'
software = 'https://www.teamworkonline.com/jobs-in-sports?utf8=%E2%9C%93&employment_opportunity_search[query]=software'

tampa = 'https://www.teamworkonline.com/jobs-in-sports?utf8=employment_opportunity_search[location][name]=Tampa%2C+FL&employment_opportunity_search[location][country]=United+States&employment_opportunity_search[location][latitude]=27.9429&employment_opportunity_search[location][longitude]=-82.462'
orlando = 'https://www.teamworkonline.com/jobs-in-sports?utf8=%E2%9C%93&employment_opportunity_search%5Bquery%5D=&employment_opportunity_search%5Blocation%5D%5Bname%5D=Orlando%2C+FL&employment_opportunity_search%5Blocation%5D%5Badministrative_division%5D=&employment_opportunity_search%5Blocation%5D%5Bcountry%5D=United+States&employment_opportunity_search%5Blocation%5D%5Blatitude%5D=28.5179&employment_opportunity_search%5Blocation%5D%5Blongitude%5D=-81.3074&employment_opportunity_search%5Bexclude_united_states_opportunities%5D=0&employment_opportunity_search%5Bcategory_id%5D=&commit=Search&employment_opportunity_search%5Bcareer_level_id%5D='
miami = 'https://www.teamworkonline.com/jobs-in-sports?employment_opportunity_search%5Bcareer_level_id%5D=&employment_opportunity_search%5Bcategory_id%5D=&employment_opportunity_search%5Bexclude_united_states_opportunities%5D=0&employment_opportunity_search%5Blocation%5D%5Badministrative_division%5D=&employment_opportunity_search%5Blocation%5D%5Bcountry%5D=United+States&employment_opportunity_search%5Blocation%5D%5Blatitude%5D=25.942&employment_opportunity_search%5Blocation%5D%5Blongitude%5D=-80.2456&employment_opportunity_search%5Blocation%5D%5Bname%5D=Miami+Gardens%2C+FL&employment_opportunity_search%5Bquery%5D=&page=2'

getjobs(hoopdirt, 'hoopdirt', 'hoopdirt')
getjobs(data, 'teamwork', 'data')
getjobs(developer, 'teamwork', 'developer')
getjobs(engineer, 'teamwork', 'engineer')
getjobs(tampa, 'teamwork', 'tampa')
getjobs(orlando, 'teamwork', 'orlando')
getjobs(miami, 'teamwork', 'miami')

send = unsentjobs()
if len(send) > 0:

    mail_content = '''Here is the list of new job postings:
    <br/> <br/>
    <table>
      <tr align="left">
        <th>Organization</th>
        <th>Position</th>
        <th>Post Date</th>
        <th>Keyword</th>
        <th>Posting</th>
      </tr>
    '''

    for i in send:
        mail_content = mail_content + '<tr>' + '<td>' + i[1] + '</td> <td>' + str(i[2]) + '</td> <td>' + str(i[3]) + "</td> <td>"+ str(i[4]) + "</td> <td><a href='" + i[0] + "'>Link</a></td></tr>"
    mail_content = mail_content + '</table>'

    sender_address = 'sportsjobalertspy@gmail.com'
    sender_pass = 'MiamiDolphins10$'
    receiver_address = 'millertime23@gmail.com'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'There are new sports jobs available!'

    message.attach(MIMEText(mail_content, 'html'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    updatesentflag()
