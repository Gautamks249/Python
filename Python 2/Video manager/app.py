
import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute('''
    create table if not exists videos(
        id integer primary key,
        name text not null,
        time text not null
    )
''')



def list_videos():
    print("\nListing all videos :- \n")
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)
        print(f"{"-"*50}")
def add_video(name, time):
    cursor.execute("insert into videos (name, time) values (?, ?)", (name, time))
    conn.commit()
    print("video added")

def update_video(id, name, time):
    cursor.execute("update videos set name = ?, time = ? where id = ?", (name, time, id))
    print("video details updated")
    conn.commit()

def delete_video(id):
    cursor.execute("delete from videos where id = ?", (id,))
    print("video deleted")



def main():
    while True:
        print("\nYoutube manager app with db")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")

        choice = input("\nEnter your choice(1/2/3/4/5) : ")

        if choice == "1":
            list_videos()

        elif choice == "2" :
            print("\nAdding new video :- ")
            name = input("\nEnter video name : ")
            time = input("Enter video time : ")
            add_video(name, time)

        elif choice == "3":
            print("Updating Video details :- ")
            id = input("\nEnter video id to update : ")
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            update_video(id, name, time)

        elif choice == "4":
            print("\nDeleting video : -")
            id  = input("\nEnter video id to delete : ")
            delete_video(id)

        elif choice == "5":
            print("\n!! EXIT !!\n")
            break

        else:
            print("\n!! INVALID INPUT !!\n")

    conn.close()

if __name__ == "__main__":
    main()