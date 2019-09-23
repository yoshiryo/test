from fastapi import FastAPI
import uvicorn
import MySQLdb

connector = MySQLdb.connect(
    user='root',
    passwd='',
    host='localhost',
    db='test_db')

cursor = connector.cursor()
cursor.execute("select * from emp")
result = cursor.fetchall()
cursor.close
connector.close

app = FastAPI()

@app.get("/")

def root():
    for row in result:
        return {row[1]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=80)
