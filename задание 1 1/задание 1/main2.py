from fastapi import FastAPI
import uvicorn
goods = [{'item_id': 1,'name':'ЧЛЕН ЧЁРНЫЙ','size':'XXL','length':25},{'item_id':2,'name':'Член розовый','size':'M','length':15}]

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/products")
async def func_1(): # +
    global goods
    return goods

@app.get("/api/products/{item_id}")
async def func_2(item_id: int):  # +
    global goods
    for i in goods:
        if i['item_id'] == item_id:
            return i
    return 'искомого значения нет'

@app.post("/api/products/new")      #+
async def func_3(item_id:int,name:str,size:str,length:int):
    global goods
    for i in goods:
        if i['item_id'] == item_id:
            return f'номер {item_id} уже существует'
    a = {'item_id': item_id, 'name': name, 'size': size, 'length': length}
    goods.append(a)
    return goods

@app.put("/api/products/edit/{item_id}")
async def func_4(item_id:int,name:str = None ,size:str = None,length:int = None):
    global goods
    for i in goods:
        if i['item_id'] == item_id:
            if name:
                i['name'] = name
            if size:
                i['size'] = size
            if length:
                i['length'] = length
            return i
    return 'нет элемента'

@app.delete("/api/products/delete/{item_id}")
async def func_5(item_id:int):
    global goods
    for i in goods:
        if i['item_id'] == item_id:
            goods.pop(goods.index(i))
            return goods
    return 'Элемента нет'


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000)
