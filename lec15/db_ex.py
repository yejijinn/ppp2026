#고쳐야함!!

from tinydb import TinyDB, Query


def count_via_db():

    db = TinyDB('lec15/db.json')
    db.insert({"name":"counter", 'value':1})
    # db.insert({'int': 1, 'char': 'a'})
    # db.insert({'int': 1, 'char': 'b'})

    User = Query()
    # print(db.search(User.int == 1))
    print(db.search(User.name == "counter"))

    if db.search(User.name == "counter") is not None:
        v= db.search(User.name =="counter")[0]["value"]
        db.update({"value":v+1},User.name =='counter')
    else:
        db.insert({"name":"counter", 'value':1})

    print(db.search(User.name == "counter"))


def main():
    count_via_db()
    

if __name__ == "__main__":
    main()