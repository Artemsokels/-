from fastapi import FastAPI
import uvicorn
goods = [{'item_id': 1,'name':'ЧЛЕН ЧЁРНЫЙ','size':'XXL','length':25},{'item_id':2,'name':'Член розовый','size':'M','length':15}]

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000)